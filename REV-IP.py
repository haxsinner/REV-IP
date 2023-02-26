import os
import re
import threading
import sys,time
from colorama import Fore

def grey(str):    
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)    
try:
    grey(Fore.LIGHTBLUE_EX+'\nChecking Requirements.....')
    time.sleep(0.5)
    import requests 
    import colorama
    grey(Fore.LIGHTGREEN_EX+'\nAll Available, Go Main Tools.....')
    time.sleep(0.5)
except:
    os.system('pip install requests') 
    os.system('pip install colorama')
    grey(Fore.LIGHTGREEN_EX+'\nAll Available, Go Main Tools.....')
    time.sleep(0.5)

import requests

os.system('cls' if os.name == 'nt' else 'clear')

s = requests.Session()

ua = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' #user gent
	}

names = []

banner = """
8888888b.  8888888888 888     888      8888888 8888888b.  
888   Y88b 888        888     888        888   888   Y88b 
888    888 888        888     888        888   888    888 
888   d88P 8888888    Y88b   d88P        888   888   d88P 
8888888P"  888         Y88b d88P         888   8888888P"  
888 T88b   888          Y88o88P          888   888        
888  T88b  888           Y888P           888   888        
888   T88b 8888888888     Y8P          8888888 888                                                                                                                                                            """
def reverse():
	try:
		print(Fore.CYAN+banner)
		grey(Fore.BLUE+"Author:Mr.Grey Hacker\n")
		grey(Fore.LIGHTYELLOW_EX+"Indian "+Fore.WHITE+"Cyber "+Fore.GREEN+"Force\n")
		print("")
		site = input(Fore.LIGHTCYAN_EX+'\nEnter Domain List Text File Path:')
		line = open(site,'r').read().splitlines()
		print("")
		for site in line:
			if site.startswith("http://"):
				site = site.replace("http://", "")
			if site.startswith("https://"):
				site = site.replace("https://", "")
			response = s.get("https://rapiddns.io/sameip/" + site + "?full=1#result", headers=ua).content.decode("utf-8")
			pattern = r"</th>\n<td>(.*?)</td>"
			results = re.findall(pattern, response)
			print(Fore.RED+"root@cyberXforce:~$ " +Fore.LIGHTGREEN_EX+
         site + " - [ " + str(len(results)) + " ]")

			for line in results:
				line = line.strip() 
				if line.startswith("www."):
					line = "" + line[4:]
				if line not in names:
					names.append(line)
					with open('output.txt', 'a+') as f:
						f.write(line + "\n") 

	except:
		print(Fore.LIGHTRED_EX+banner)
		print(Fore.LIGHTYELLOW_EX+"Author:Mr.Grey Hacker")
		print(Fore.LIGHTYELLOW_EX+"Indian Cyber Force\n")
		pass

t = threading.Thread(target=reverse)
t.start()
