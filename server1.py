import socket

s = socket.socket()

port = 8080

s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	c.send("test_2".encode())
	c.close()
	break
	pass