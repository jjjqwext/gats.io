# -*- coding: utf8 -*-
import ssl
import gc
from threading import Thread
import websocket, json
import time, random, socks5
import requests

FFALINK = ''

servers = requests.post('https://io-8.com/find_instances',data = {"game": 'gats.io' }).json()
for srv in servers:
	if srv['region'] == 'Europe' and srv['game_type'] == 'FFA':
		FFALINK = srv['url']
		print(srv['url'])
		break

proxxx = '''
1.1.1.1:1111
2.2.2.2:2222
etc.''' #you need proxies to run this script

def sss():
	ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
	prox = random.choice(proxxx.split('\n'))
	header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', "Origin":"https://gats.io"}
	try:
		ws.connect('wss://'+FFALINK,header = header, origin= "https://gats.io", http_proxy_port=prox.split(":")[1],http_proxy_host=prox.split(":")[0],proxy_type="socks4", timeout = 5)
		ws.send('s,5,3,1',websocket.ABNF.OPCODE_BINARY)
		#ws.send('k,6,1',websocket.ABNF.OPCODE_BINARY)
		while 1==1:
			ws.send('c,1 hello world 0')
			time.sleep(0.5)
			ws.send('c,0 hello world 1')
			time.sleep(0.5)
			
	except Exception as exc:			
		ws.close()
		del ws

def rn():
	while 1==1:
		w = Thread(target = sss)
		w.start()
		time.sleep(0.001)

rn()
