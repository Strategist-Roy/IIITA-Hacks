from flask import Flask, render_template, request
import socket
import os
import netifaces as ni
import sys

app = Flask(__name__)

@app.route("/send")
def send():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ni.ifaddresses('eno1')[2][0]['addr']
	port = 6790
	sock.bind((host, port))
	sock.listen(5)
	conn, addr = sock.accept()
	fp = open('sendtest', 'rb')
	byte = fp.read(1024)
	while (byte):
		conn.send(byte)
		byte = fp.read(1024)
	fp.close()
	conn.close()
	return "Transfered successfully"

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		port = 4999
	else:
		port = int(sys.argv[1])
	app.run(debug=True, port=port)

