# Importación de bibliotecas
import socket
import os

grupo = 1
port = 8000
for g in range(1):
    path = 'grupo_' + str(grupo) + '/'
    for x in range(100):
        # CREAMOS UN NUEVO SOCKET
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # DEFINIMOS EL PUERTO
        # path = "dirx/"
        # Petición HTTP
        header = """\
        {verbo_http} {ruta} HTTP/1.1\r
        Content-Type: {content_type}\r
        Content-Length: {content_length}\r
        Host: {host}\r
        Connection: close\r
        \r\n\r\n
        filename={filename}\r
        content="""

        # os.makedirs(os.path.dirname(path), exist_ok=True)
        # list_groups
        ruta_server = path
        # Variable y apertura del archivo
        file = open(path + 'g' + str(grupo) + '_archivo_' + str(x+1), 'rb')
        f_name = os.path.basename(file.name)
        f = file.read()
        # file = open('grupo_3/g3_archivo_77', 'rb')
        # Relleno de la petición
        header_encode = header.format(
        	verbo_http="PUT",
        	ruta=ruta_server,
            content_type="application/x-www-form-urlencoded",
            content_length=len(f),
            host=str('localhost') + ":" + str(port),
            filename=f_name
        ).encode()

        #Concatenamos cabecera
        payload = header_encode + f
        # Conexión
        s.connect(('localhost', port))
        # Envío de datos
        s.sendall(payload)
        # Cierre del archivo
        file.close()
        # IMPRIMIMOS
        # print(payload.decode())
        s.shutdown(socket.SHUT_WR)
        print(s.recv(1024).decode())
        # CERRAMOS LA CONEXIÓN
        s.close()
        if x + 1  == 100:
            grupo = grupo + 1

flag = True
while flag:
    print("\t¿Qué desea hacer?")
    print("1\tObtener listado de archivos")
    print("2\tObtener archivo")
    action = int(input("\t>"))
    if action == 1:
        print("Ingrese el numero de grupo:")
        num_g = int(input(">"))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8000
        header = """\
        {verbo_http} {ruta} HTTP/1.1\r
        Content-Type: {content_type}\r
        Host: {host}\r
        Connection: close\r
        \r\n\r\n
        """
        header_encode = header.format(
            verbo_http="GET",
            ruta='grupo_' + str(num_g),
            content_type="application/x-www-form-urlencoded",
            host=str('localhost') + ":" + str(port),
        ).encode()
        # Conexión
        s.connect(('localhost', port))
        # Envío de datos
        s.sendall(header_encode)
        s.shutdown(socket.SHUT_WR)
        # IMPRIMIMOS
        print(s.recv(1024).decode())
        # CERRAMOS LA CONEXIÓN
        s.close()
    elif action == 2:
        print("dslivh")