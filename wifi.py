# Done by fantome
# For any query contact hackingghost2002@gmail.com


import subprocess
import time
import colorama
from colorama import Fore
print(Fore.GREEN + "   =====================================   ")
print("")
print("")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||====================||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print(Fore.RED + "          ||                    ||")
print("")
print("")
print(Fore.GREEN + "   =====================================   ")

subprocess.call(["sudo iwconfig"], shell=True)
interface = input(Fore.CYAN + "Enter the interface name : ")

print(Fore.BLUE + "Here the Process")
print("")
print("Managed >> Monitor -- 1")
print("Monitor >> Managed -- 2")
print("")

n = int(input(">>> "))
def ip(interface):
    if n == 1:   
        try:
            subprocess.call (["sudo", "ifconfig", interface, "down"])
            time.sleep(2)
            subprocess.call (["sudo", "iwconfig", interface, "mode", "monitor"])
            time.sleep(2)
            subprocess.call (["sudo", "ifconfig", interface, "up"])
            print(Fore.GREEN + "[+] Success: Interface changed to monitor mode")
            print(Fore.WHITE + "")
        except Exception:
            print(Fore.RED + "[-] Error: Failed to change the interface to monitor mode")    
    elif n == 2:
        try:
            subprocess.call (["sudo", "ifconfig", interface, "down"])
            time.sleep(2)
            subprocess.call (["sudo", "iwconfig", interface, "mode", "managed"])
            time.sleep(2)
            subprocess.call (["sudo", "ifconfig", interface, "up"])
            print(Fore.GREEN + "[+] Success: Interface changed to managed mode")
            print(Fore.WHITE + "")
        except Exception:
            print(Fore.RED + "[-] Error: Failed to change the interface to monitor mode") 
    else:
        print(Fore.RED + "[-] Erroe: Enter the CORRECT value :( ")
ip(interface)
