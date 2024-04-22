from colorama import Fore
import os
import requests

def send_req(amount, url):
    for _ in range(amount):
        res = requests.get(url = url)
        print(f"Sent packet, status code: {res.status_code}")
    print("thread exitted")

while True:
    print(f"{Fore.CYAN}lolbatas legal illegal tools (0.1 beta){Fore.RESET}\n")
    print("thinges:")
    print("1. dos")
    print("2. get your own ip")
    print("3. ip lookup")
    print("4. get websites ip")
    ans = input("enter your \"thinges\":")

    if ans == "1":
        exec(open("thinges/dos.py", "r").read())
        os.system('cls' if os.name=='nt' else 'clear')
    elif ans == "2":
        exec(open("thinges/get_ip.py", "r").read())
        os.system('cls' if os.name=='nt' else 'clear')
    elif ans == "3":
        exec(open("thinges/get_ip_info.py", "r").read())
        os.system('cls' if os.name=='nt' else 'clear')
    elif ans == "4":
        exec(open("thinges/web_ip.py", "r").read())
        os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("The command you entered didnt exist! Probably a typo or spelling issue.")
