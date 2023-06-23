import colorama
from colorama import Fore
import webbrowser
colorama.init(autoreset=True)

def searchUsernames():
    username = input(f"\n{Fore.GREEN}Enter username of the target: ")
    url = f"https://www.google.com/search?q={username}*com"
    
    webbrowser.open(url)