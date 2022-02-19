# IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import socket
import os
# CREAMOS UN NUEVO SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# DEFINIMOS EL PUERTO
port = 8000
# path = "dirx/"
# CREAMOS LA VARIABLE DE LA CABECERA
header = """\
{verbo_http} {ruta} / HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""

# os.makedirs(os.path.dirname(path), exist_ok=True)
file = open('test/img.jpg', 'rb')
ruta_server = "dirx/filex"

# VARIABLE DEL BODY DE LA PETICIÓN
# v1 = file.read()
# body = v1.encode()
# header_encode = header.format(
# 	verbo_http="PUT",
# 	ruta=ruta_server,
#     content_type="application/x-www-form-urlencoded",
#     content_length=len(body),
#     host=str('localhost') + ":" + str(port)
# ).encode()

# payload = header_encode + body
# payload = body
# CREAMOS UNA CONEXIÓN CON LOCALHOST EN EL PUERTO DEFINIDO
s.connect(('localhost', port))
# ENVIAMOS EL PAYLOAD AL SERVIDOR
# s.sendall(payload)
s.sendfile(file)
# IMPRIMIMOS
# print(payload.decode())
print(s.recv(1024).decode())
# CERRAMOS LA CONEXIÓN
s.close()
file.close()
