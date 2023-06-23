import webbrowser
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def searchTelNums():
    num = input(f"\n{Fore.GREEN}Enter phone number of the target: ")
    url = f"https://whocalld.com/search?p={num}"
    
    webbrowser.open(url)