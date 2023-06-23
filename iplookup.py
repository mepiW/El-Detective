import colorama
from colorama import Fore
import requests
colorama.init(autoreset=True)

def searchIP():
    ip = input(f"\n{Fore.GREEN}Enter target ip address: ")

    shodan = f"https://internetdb.shodan.io/{ip}"
    location = f"https://api.iplocation.net/?ip={ip}"

    rshodan = requests.get(shodan)
    rlocation = requests.get(location)

    rshodan = rshodan.json()
    rlocation = rlocation.json()

    country = rlocation["country_name"]
    isp = rlocation["isp"]

    for i in rshodan:
        if i == "cpes" or i == "vulns" or i == "tags":
            continue
        else: 
            print(f"\n{Fore.YELLOW} -- {i.upper()}: {str(rshodan[i])}")

    print(f"\n{Fore.YELLOW} -- COUNTRY: {country}")
    print(f"\n{Fore.YELLOW} -- ISP: {isp}")
