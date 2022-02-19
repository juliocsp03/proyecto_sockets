import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000

s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	os.makedirs(os.path.dirname('serv_test/'), exist_ok=True)
	data = c.recv(1024)
	file = open('serv_test/img_serv.jpg', 'wb')
	while data:
		file.write(data)
		data = c.recv(1024)
	file.close()
	print(c)
	print(addr)
	print(c.recv(1024).decode())
	c.send("Recibido".encode())
	c.close()
	break
	pass

s.close()