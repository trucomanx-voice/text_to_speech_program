# Text to Speech Program

This package provides a text-to-speech server, using `gtts` and `pydub`, and a client program to interact with the server.

## Install from pip
To install the package from [pypi](https://pypi.org/project/text-to-speech-program), follow the instructions below:

### With pip

```bash
pip install --upgrade text-to-speech-program
```

Execute `which tts-program-server` to see where it was installed, probably in `/home/USERNAME/.local/bin/tts-program-server`. Then, execute `tts-program-server` to start the server.

### With pipx (recommended for desktop applications)

```bash
pipx install text-to-speech-program
```

If you need to upgrade later: `pipx upgrade text-to-speech-program`

## Install from pip and add to the Linux service
Adding to Linux service

```bash
pipx install text-to-speech-program
curl -fsSL https://raw.githubusercontent.com/trucomanx-voice/text_to_speech_program/main/install_linux_service.sh | sh
```

## Start the server
If the program server was not added to the Linux service, then to start the text-to-speech server, use the command below:

```bash
tts-program-server
```

## Sending a DICT from string:
Adding a text-to-speech task.

```bash
tts-program-client senddict '{ 
    "text": "Some text to convert. OK", 
    "language": "en", 
    "split_pattern": ["."], 
	"speed": 1.25 
}'
```

## More information
More information can be found in [doc/README.md](doc/README.md)

