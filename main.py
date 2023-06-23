import iplookup
import usernamelookup
import telnumlookup

import colorama
from colorama import Fore
colorama.init(autoreset=True)

print(f"""{Fore.GREEN}\n
               -+#=:::*#%@@@%+.              
             .#%@#    @@@@@@@@@:             
             *==:    =@@@@@@@@@@.            
            =*   .-=#@@@@@@@@@@@*            
            %*==++++++%@@@@@@@@@@.           
           .+#@@@@@@@@@@@@@@@@@@@=           
           +@%%##***+++++***###%@%-          
                                  .          
:-==++**####%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@+
:+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:  
    .:=+#@@@@@@@@@@@@@@@@@@@@@@@@@@+*:.      
         %@@@@@@@@@@@@@@@@@@@@@@@@=..        
          ===-:=*@@@@#+@@@@@@@@:*-:.           Created by: Matey Tsonev
           .:     .%= =@@@@@@@# ::           OSINT / Info. gathering tool
             .    =* --@@@@@@@:                   made for fun :-)
          .+@#.   .    @@@@@@+ +@*.          
         *@@@%=:     :=@@@@@@:=#@@@*.        
       -#@@@@%@*-.   =*@@@@@#*@%@@@@#-.      
  .-+##**@@@@@*@@+-:  .@@@%*%@*%@@@@#*##*-.  
 ::.     %@@@@@=#@#::-==-.*@%=%@@@@@     .:: 
         =@@@@@@++@@+   =@@+=@@@@@@+         
          %@@@@@@*:%@@=%@@-+@@@@@@@          
          -#%%@@@@* +@@@*.*@@@@@%#=          
               -@@@%..@- #@@@+               
               #@@@@@:%:%@@@@@               
              .@@@@@@@@@@@@@@@-              
               .=%@@@@@@@@@%+:               
                  :*@@@@@*:     
    """)
def main():   
    while True:
        print(f"{Fore.YELLOW}\n1. IPV4 LOOKUP\n")
        print(f"{Fore.YELLOW}2. USERNAME/EMAIL LOOKUP\n")
        print(f"{Fore.YELLOW}3. PHONE NUMBER LOOKUP\n")
        option = input(f"{Fore.YELLOW}Choose an option (1, 2, 3, q) ")
        
        if option == "q":
            exit()

        elif option == "1":
            iplookup.searchIP()
            endSession()

        elif option == "2":
            usernamelookup.searchUsernames()
            endSession()

        elif option == "3":
            telnumlookup.searchTelNums()
            endSession()


def endSession():
    choice = input(f"{Fore.RED}\nDo you wish to countinue? (y/n) ")
    choice = choice.lower()
    if choice == "y":
        main()
    if choice == "n":
        exit()

if __name__ == "__main__":
    main()