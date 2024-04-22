import requests
import json

ip = input("Enter victims ip: ")
res = requests.get(f"http://ip-api.com/json/{ip}").json()
ures = json.dumps(res, indent = 2)
print(ures)
input("Press enter to contine..")