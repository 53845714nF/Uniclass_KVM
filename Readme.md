# Uniclass KVM

This Python program allows you to switch on a KVM (Keyboard, Video, and Mouse) switch using your computer's USB port.
The program sends a USB signal to the KVM switch to between two computers.

## Requirements

- Python 3
- PyUSB package

## Installation

Install Python 3 from the official Python website.
Install the PyUSB package by running the following command in your terminal or command prompt:

```
pip install pyusb
```

## Usage

Connect your KVM switch to your computer's USB port.
Run the program by the command "uniclass".

The program will send a USB signal to the KVM switch to switch between Coomputers.

## Troubleshooting

If the program does not detect the KVM switch, make sure it is connected to your computer's USB port and that the PyUSB package is installed correctly.
If you encounter any errors, try running the program with administrative privileges.

## Disclaimer

This Python program is provided as-is without any warranty or guarantee of functionality. Use at your own risk.

## Build

` python3 setup.py --command-packages=stdeb.command bdist_deb`
