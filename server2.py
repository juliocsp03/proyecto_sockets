import socket

s = socket.socket()

port = 8090

s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	c.send("kshgdivkdf".encode())
	c.close()
	break
	pass