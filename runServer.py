# coding=utf-8
import sys
import logging
from websocket_server import WebsocketServer

def new_client(client, server):
    print("Client(%d) has joined." % client['id'])

def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])

def response(client, server, message):
    print("Client(%d) said: %s" % (client['id'], message))
    result = textParse(message)
    server.send_message(client, result)

def textParse(text):
	header = []
	for i in range(9): header.append(str(i+1))
	header.append('a')
	header.append('b')
	head = text.split('--')[0]
	text = text.split('--')[1:]
	from connectData import response
	if head in header: 
		return response.switch(head,text)
	else: return '[Error:1] Fault Request'

server = WebsocketServer(9999, host='127.0.0.1', loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(response)
server.run_forever()