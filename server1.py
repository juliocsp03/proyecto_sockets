import socket

s = socket.socket()

port = 8000

s.bind(('', port))

s.listen(5)

c, addr = s.accept()
while True:
	c.send("Recibido".encode())
	# data = c.recv(1024).decode()
	print(c)
	print(addr)
	print(c.recv(1024).decode())
	c.close()
	break
	pass

