import socket

s = socket.socket()

port = 8000

s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	c.send("Recibido compa".encode())
	print(c.recv(1024).decode())
	c.close()
	break
	pass