"""
instagram-5letter-username-finder

This project is dedicated to the public domain under the Creative Commons Zero (CC0) 1.0 Universal License.
You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

Full license text: https://creativecommons.org/publicdomain/zero/1.0/legalcode
"""



print("\033[1;33;40m  ~ Pяσɢяαммεя • KEVIN • -> @K3S63 | Cнαиияℓ :  @pythontoolgod ~")
print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ")
print()


from pyfiglet import Figlet


V = '\033[1;36;40m'
F = '\033[1;32m'
Z = '\033[1;31m'
S = '\033[1;33m'
B = '\x1b[38;5;208m'
print ("\033[1;36;40m")
fig = Figlet(font='poison')
logo = fig.renderText(f'K3S63')
print(logo)

import webbrowser
webbrowser.open("https://t.me/pythontoolgod")


import os
import asyncio
import random
try:
    import string
    import aiohttp
except ModuleNotFoundError as Patrek:
    os.system(f'pip install {Patrek.name}')
green_console = "\033[92m"
red_console = "\033[91m"
yellow_console = "\033[93m"
token = input('\033[1;32mTELEGRAM TOKEN : ')
telegram_user_id = input('\033[1;31mTELEGRAM ID : ')
async def generate_username(length=4):
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    separator = random.choice(['.', '_'])
    index = random.randint(1, length - 1)
    username_with_separator = username[:index] + separator + username[index:]
    return username_with_separator
async def create_instagram_account(session):
    while True:
        username = await generate_username()
        headers = {
            "Host": "i.instagram.com",
            "cookie": "mid=Y16iBgABAAFggfUYwajggkGFz-hs",
            "x-ig-capabilities": "AQ==",
            "cookie2": "$Version=1",
            "x-ig-connection-type": "WIFI",
            "user-agent": "Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip"
        }
        data = {
            "password": "zxcvbm1@",
            "device_id": "android-2793e055-2a92-4df2-890f-f88f52538de5",
            "guid": "2793e055-2a92-4df2-890f-f88f52538de5",
            "email": "zodhokxbsbdbsbsksbs@gmail.com",
            "username": username
        }
        async with session.post("https://i.instagram.com/api/v1/accounts/create/", headers=headers, data=data) as response:
            json_response = await response.json()
            error_type = json_response.get('error_type')
            if error_type == 'needs_upgrade':
                print(f'{green_console}GooD UserName : {username}   BY @pythontoolgod')
                await send_telegram_message(username)
            elif error_type == 'taken':
                print(f'{red_console}BaD UserName : {username}')
            else:
                print(f'{yellow_console}{error_type} : {username}')
async def send_telegram_message(username):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {
            "chat_id": telegram_user_id,
            "text": username
        }
        await session.get(url, params=params)
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [create_instagram_account(session) for _ in range(10)]
        await asyncio.gather(*tasks)
asyncio.run(main())
