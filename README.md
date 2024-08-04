# Instagram 5-Letter Username Finder

This project is a tool to find untaken 5-character Instagram usernames, which are considered rare these days. The script generates usernames and checks their availability on Instagram, and it notifies you via Telegram if a good username is found.

## Features

- Generates random 5-character Instagram usernames.
- Checks the availability of the generated usernames on Instagram.
- Notifies via Telegram when a good username is found.

## Requirements

- Python 3.7+
- `aiohttp` library
- `pyfiglet` library

## Installation

### On Termux (Android)

1. **Install Termux** from the Google Play Store or F-Droid.
2. **Update package list and install Python**:
    ```bash
    pkg update
    pkg install python
    ```
3. **Install Git**:
    ```bash
    pkg install git
    ```
4. **Clone the repository**:
    ```bash
    git clone https://github.com/k3s63/instagram-5letter-username-finder.git
    cd instagram-5letter-username-finder
    ```
5. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### On Windows

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/), ensuring that you add Python to your PATH during installation.
2. **Open Command Prompt**:
    - Press `Win + R`, type `cmd`, and press Enter.
3. **Clone the repository**:
    ```cmd
    git clone https://github.com/k3s63/instagram-5letter-username-finder.git
    cd instagram-5letter-username-finder
    ```
4. **Install the required packages**:
    ```cmd
    pip install -r requirements.txt
    ```

### On Kali Linux

1. **Open Terminal**.
2. **Update package list and install Python**:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip git
    ```
3. **Clone the repository**:
    ```bash
    git clone https://github.com/k3s63/instagram-5letter-username-finder.git
    cd instagram-5letter-username-finder
    ```
4. **Install the required packages**:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. **Obtain Your Telegram Bot Token**:
   - Create a new Telegram bot using [@BotFather](https://t.me/BotFather) if you don't already have one.
   - Note down the bot token provided by BotFather.

2. **Get Your Telegram User ID**:
   - Start a chat with [@userinfobot](https://t.me/userinfobot) on Telegram.
   - Send the `/start` command to the bot.
   - The bot will provide your user ID. Note this ID.

3. **Run the Script**:
    ```bash
    python 5lfinderbyk3s63.py
    ```
  

4. **Enter Your Telegram Bot Token and Your Telegram User ID** when prompted by the script.

## License

This project is dedicated to the public domain under the Creative Commons Zero (CC0) 1.0 Universal License. You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

Full license text: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/legalcode)

## Contact

- Programmer: KEVIN ([@K3S63](https://t.me/K3S63))
- Channel: [@pythontoolgod](https://t.me/pythontoolgod)
