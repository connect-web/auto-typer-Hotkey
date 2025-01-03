# Auto-typer

- Designed for Windows hosts Operating systems, Linux support is not yet added
- Your KVM / Virtual Machine can be any distribution but this software runs on the machine 1 layer up and can paste into Virtual Machines by emulating a Keyboard device.

#### Use cases
Ideal for KVM's where paste is not an option but the host machine has access to a vnc client type connection.


## Installation

### Windows from pre compiled executable
1) [Visit releases Page for Windows](https://github.com/connect-web/auto-typer-Hotkey/releases/tag/0.1)
2) Download main.exe
3) Click run and now you can refer to [Usage](#usage-screenshots)

### Windows from source

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

4) Download auto-typer files as a .ZIP and extract to folder
5) Navigate to /windows/ directory, You will see main.py and requirements.txt in this directory.
6) Open Command prompt or powershell here and run the following:
7) install required packages
```cmd
pip install -r requirements.txt
```

- The Windows installation is now complete, you can now run it

## Running

## Running on Windows from source
```cmd
python main.py
```


## Hotkey Program Usage

1) Follow the on-screen instructions

- You can click set-hotkey and a popup will say it's ready to setup the hotkey, press OK
- Now click your desired hotkey which will act as your PASTE Key.

2) Type your text into the input text box that you want to paste
3) Press your Hotkey and it will auto-type this Similar to how Paste works.



## Usage Screenshots

- In the provided screenshots, I setup the hotkey to auto-type the text in the box to **Tab Key**
- I recommend using the **Caps lock key** because tab types the tab character first which may not be useful for most use cases

### Set Hotkey
- Click Set Hotkey button
<img src="./imgs/1%20-%20setup%20hotkey.png">

### Hotkey confirmation setup Dialog
- Press OK
<img src="./imgs/2%20-%20Setup%20hotkey%20Popup%20Dialog.png">

### Choose your auto-typer key
- Recommended **Press CAPS LOCK** (Tab is not a good key to use)
<img src="./imgs/3%20-%20Select%20key.png">

## Choose input text and use the auto-typer
- I typed abc123321\n into my input text
- Opened notepad
- Pressed the hotkey and it typed the content:
```
    abc123321123\n
```
<img src="./imgs/4%20-%20Test%20auto%20typing.png">
