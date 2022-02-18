# IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import socket

# CREAMOS UN NUEVO SOCKET
s = socket.socket()
# DEFINIMOS EL PUERTO
port = 8000
# CREAMOS LA VARIABLE DE LA CABECERA
header = """\
PUT / HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""
# VARIABLE DEL BODY DE LA PETICIÓN
body = "Test to server".encode()
header_encode = header.format(
    content_type="application/x-www-form-urlencoded",
    content_length=len(body),
    host=str('localhost') + ":" + str(port)
).encode()

payload = header_encode + body
# CREAMOS UNA CONEXIÓN CON LOCALHOST EN EL PUERTO DEFINIDO
s.connect(('localhost', port))
s.sendall(payload)
print(payload.decode())
print(s.recv(1024).decode())

s.close()
