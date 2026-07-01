#!/usr/bin/python3
import argparse
import requests
import json
import sys
import os

from . import config
import text_to_speech_program.about as about

def send_json_from_dict(server_url,data):
    # Enviar solicitação POST ao servidor
    response = requests.post(f'{server_url}/add_task', json=data)

    if response.status_code == 200:
        print(f"Task sent successfully! ID: {response.json()['id']}")
        return response.json()['id'];
    else:
        print("Error submitting task.")
        return None

def send_json_from_file(server_url,filepath):
    # Verificar se o arquivo existe
    if not os.path.isfile(filepath):
        print(f"File {filepath} not found.")
        return None

    # Carregar o conteúdo do arquivo JSON
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error reading JSON file {filepath}.")
        return None

    return send_json_from_dict(server_url,data);


def remove_task(server_url,task_id):
    # Enviar solicitação DELETE ao servidor
    response = requests.delete(f'{server_url}/remove_task/{task_id}')

    if response.status_code == 200:
        print(response.json()["message"])
        return response.json()["message"]
    else:
        print("Error removing task:",task_id)
        return None



def main():

    Config = config.load_config()
    
    prog_client_name = about.__program_client__

    parser = argparse.ArgumentParser(
        prog=prog_client_name,
        description="Client CLI for sending tasks to the TTS server",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=f"""
    Examples:
      {prog_client_name} host
      {prog_client_name} port
      {prog_client_name} config

      {prog_client_name} send file.json

      {prog_client_name} senddict '{{"text": "Hi","language":"en", "split_pattern": ["."],"speed":1.25 }}'

      {prog_client_name} remove d9b17a60-4370-4d13-86a8-f258a37fdbf6
    """
    )

    parser.add_argument("--host", help="Override server host")
    parser.add_argument("--port", type=int, help="Override server port")

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("host", help="Show server host")
    sub.add_parser("port", help="Show server port")
    sub.add_parser("config", help="Show config file path")

    send = sub.add_parser("send", help="Send JSON file to server")
    send.add_argument("filepath")

    senddict = sub.add_parser("senddict", help="Send JSON string to server")
    senddict.add_argument("data")

    remove = sub.add_parser("remove", help="Remove task by ID")
    remove.add_argument("task_id")

    args = parser.parse_args()
    
    host = args.host if args.host else Config["host"]
    port = args.port if args.port else Config["port"]
    
    if port <= 0 or port > 65535:
        print("Invalid port number")
        sys.exit(1)

    SERVER_URL = f"http://{host}:{port}"

    if args.command is None:
        parser.print_help()
        sys.exit(2)

    if args.command == "send":
        send_json_from_file(SERVER_URL, args.filepath)

    elif args.command == "senddict":
        try:
            data_dict = json.loads(args.data)
        except json.JSONDecodeError:
            print("Invalid JSON string.")
            sys.exit(1)

        send_json_from_dict(SERVER_URL, data_dict)

    elif args.command == "remove":
        remove_task(SERVER_URL, args.task_id)

    elif args.command == "host":
        print(host)

    elif args.command == "port":
        print(port)

    elif args.command == "config":
        config_path, _ = config.get_config_path()
        print(config_path)

# Iniciar o servidor Flask
if __name__ == "__main__":
    main();
 
