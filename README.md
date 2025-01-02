# Auto-typer

ideal for KVM's where paste is not an option but the host machine has access to a vnc client type connection.


## Setup

### Linux

### Install pip
```bash
apt-get install python3-pip -y
```

- Requires: Python3 installed and pip
```bash
pip install -r requirements.txt
```

### Windows

1) Download any [Python3 version](https://www.python.org/downloads/)
- Ensure you check the option "Add Python to PATH" during installation.
2) Open command prompt and verify python is installed
```cmd
python --version
```

You should expect the python version to output if this is not correct python did not install and add to PATH 

3) Install pip if it's not already installed.
```cmd
python -m ensurepip 
```
4) install required packages
```cmd
pip install -r requirements.txt
```





# Usage
## Running on Windows from source
```cmd
python main.py
```

## Running on Linux from source
```shell
python3 main.py
```

## Hotkey Program Usage

1) Follow the on-screen instructions

- You can click set-hotkey and a popup will say it's ready to setup the hotkey, press OK
- Now click your desired hotkey which will act as your PASTE Key.

2) Type your text into the input text box that you want to paste
3) Press your Hotkey and it will auto-type this Similar to how Paste works.