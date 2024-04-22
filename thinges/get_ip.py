import requests
from bs4 import BeautifulSoup

responce = requests.get("https://2ip.ru")
soup = BeautifulSoup(responce.text, "lxml")
ip = soup.find("div", class_ = "ip").text.strip()
print(ip)
input("Press enter to contine..")