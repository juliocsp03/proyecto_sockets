import socket

s = socket.socket()

port = 8070

s.bind((socket.gethostname(), port))

s.listen(5)

while True:
	c, addr = s.accept()
	c.send("test".encode())
	c.close()
	break
	pass