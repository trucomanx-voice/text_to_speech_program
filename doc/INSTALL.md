# 1. Installing

## 1.0. Dependencies

The main dependencies of the package are:

* `Flask` ​​for the server
* `gtts` for text-to-speech
* `pydub` for audio playback
* `requests` for the client to interact with the server

## 1.1. Install package from git

If you want to create a tar.gz package from source and install:

```bash
pip install --upgrade pkginfo twine packaging

git clone https://github.com/trucomanx-voice/text_to_speech_program.git
cd text_to_speech_program/src
python -m build
pip install dist/text_to_speech_program-*.tar.gz
```

Execute `which tts-program-server` to see where it was installed, probably in `/home/USERNAME/.local/bin/tts-program-server`.

## 1.2. Install package from pip

To install the package from [pypi](https://pypi.org/project/text-to-speech-program), follow the instructions below:


```bash
pip install --upgrade text-to-speech-program
```

Execute `which tts-program-server` to see where it was installed, probably in `/home/USERNAME/.local/bin/tts-program-server`.


### 1.2.1. Install the package from pip and add to the Linux service

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx-voice/text_to_speech_program/main/install_linux_service.sh | sh
```

After the last code, the program server starts at with the operating system.
Now the next commands are accepted (Use them if necessary).

## 1.3. If a Service is Installed on Linux

### 1.3.1. Start server service in linux
**You only need to start the server if it has been stopped or is disabled from starting with Linux boot**.

```bash
sudo systemctl start tts-program-server
```

### 1.3.2. Stop server service in linux

```bash
sudo systemctl stop tts-program-server
```

### 1.3.3. Disable service at linux startup

```bash
sudo systemctl disable tts-program-server
```

### 1.3.4. Show journal of service

```bash
journalctl -u tts-program-server  -f
```

