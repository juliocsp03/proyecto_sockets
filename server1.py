import socket
import os
from os import listdir
from os.path import isfile, join

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000

s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	data = c.recv(1024)
	request = b""
	while data:
		# file.write(data)
		request = request + data
		data = c.recv(1024)
	parts = request.split(b'content=')
	header = parts[0].decode()
	header_parts = header.split()
	verbo_http = header_parts[0]
	uri = header_parts[1]
	if (verbo_http == 'PUT' or verbo_http == 'POST'):
		filename = header.split("filename=")
		os.makedirs(os.path.dirname('s1/'+uri+'/'), exist_ok=True)
		filename = filename[1].split('\r\n')
		filename = filename[0]
		file = open('s1/'+uri+filename, 'wb')
		img = parts[1]
		file.write(img)
		file.close()
		c.send("Recibido".encode())
	elif verbo_http == 'GET':
		# print(uri)
		files = [f for f in listdir('s1/'+uri) if isfile(join('s1/'+uri, f))]
		print(len(files))
		c.send("Errorororo".encode())
	# print(header)
	c.close()
	# break

s.close()