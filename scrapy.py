import requests
from pycenter import center
from colorama import Fore
from requests import get

with open("ScrapyResult/http_proxy.txt", 'r+') as f:
		f.truncate(0)
		
with open("ScrapyResult/socks4_proxy.txt", 'r+') as f:
		f.truncate(0)
		
with open("ScrapyResult/socks5_proxy.txt", 'r+') as f:
		f.truncate(0)

scrapy = f"""{Fore.RED}  
  ______                               
 / _____)                              
( (____   ____  ____ _____ ____  _   _ 
 \____ \ / ___)/ ___|____ |  _ \| | | |
 _____) | (___| |   / ___ | |_| | |_| |
(______/ \____)_|   \_____|  __/ \__  |
                          |_|   (____/ {Fore.RESET}    {Fore.BLUE}github.com/Vodkarm/Scrapy{Fore.RESET}"""

print(center(scrapy))
print("")

menu = """
+----------+--------+
| Numerics | Choice |
+----------+--------+
| 1        | HTTP   |
| 2        | Socks4 |
| 3        | Socks5 |
| 4        | Exit   |
+----------+--------+"""

print(Fore.BLUE + center(menu))
print("")
c = input(Fore.BLUE + " > What's the type to scrap: ")
if c == "1":
	r = requests.get("https://api.proxyscrape.com/v2/?requests=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
  	with open("ScrapyResult/http_proxy.txt", "w") as f:
	  	f.write(r.text)
		print(f"[{Fore.GREEN}SUCESS{Fore.RESET}] Scrapy have sucessfully added proxies to ScrapyResult/http_proxies.txt")

if c == "2":
	r = requests.get("https://api.proxyscrape.com/v2/?requests=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
  	with open("ScrapyResult/socks4_proxy.txt", "w") as f:
	  	f.write(r.text)
		print(f"[{Fore.GREEN}SUCESS{Fore.RESET}] Scrapy have sucessfully added proxies to ScrapyResult/socks4_proxies.txt")
		

if c == "3":
	r = requests.get("https://api.proxyscrape.com/v2/?requests=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
  	with open("ScrapyResult/socks5_proxy.txt", "w") as f:
	  	f.write(r.text)
		print(f"[{Fore.GREEN}SUCESS{Fore.RESET}] Scrapy have sucessfully added proxies to ScrapyResult/socks5_proxies.txt")

if c == "4":
	print(Fore.BLUE + "Please give a star on github :)")
