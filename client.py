# Importación de bibliotecas
import socket
import os
from os import listdir
from os.path import isfile, join
import random
import time
import pandas as pd


contador = -1
fileList = []
fileList2 = []
#fileList = []
def upload(path, port):
#    di = {}
#    di["path"] = path
#    di['servidor'] = port
#    fileList.append(di)

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
    file = open(path, 'rb')
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

    # Concatenamos cabecera
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

#def getFile():
#    for file in fileList:
#        download(file.path, file.port)

def download(nombre_archivo, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    header = """\
    {verbo_http} {ruta} HTTP/1.1\r
    Content-Type: {content_type}\r
    Host: {host}\r
    Connection: close\r
    \r\n\r\n
    """
    header_encode = header.format(
        verbo_http="GET",
        ruta=str(nombre_archivo),
        content_type="application/x-www-form-urlencoded",
        host=str('localhost') + ":" + str(port),
    ).encode()
    s.connect(('localhost', port))
    # Envío de datos
    s.sendall(header_encode)
    s.shutdown(socket.SHUT_WR)
    # IMPRIMIMOS
    print("Archivo:")
    data = s.recv(1024)
    response = b""
    while data:
        response = response + data
        data = s.recv(1024)
    # response = response.decode()
    parts = response.split(b'content=')
    header = parts[0].decode()
    filename = header.split("filename=")
    filename = filename[1].split('\r\n')
    filename = filename[0].split('\n\t\t\t')
    filename = filename[0]
    print(filename)
    os.makedirs(os.path.dirname('descargas/'), exist_ok=True)
    file = open('descargas/'+filename, 'wb')
    img = parts[1]
    file.write(img)
    file.close()
    print("Descargado")
    s.close()

def randomBalancer():
    num = random.randint(0,2)
    return num

def hashBalancer(fileName):
    result = hash(fileName)
    index = result%3
    return index

def roundrobin():
    global contador
    contador+=1
    if (contador==3):
        contador=0
    return contador


def push_files(lb):
    
    servers = [46001, 46002, 46003]

    
    for g in range(1,4):
        print("Grupo ", g)
        path = 'grupo_' + str(g) + '/'
        for i in range(1,101):
            # Load Balancing
            file = path + "g" + str(g) + "_archivo_" + str(i)
            if(lb == 1):
                num = randomBalancer()
            elif(lb == 2):
                num = roundrobin()
            elif(lb == 3):
                num = hashBalancer(file)
            print("Server ",num+1, "-> File ", file)
            #fileList = []
            di = {}
            di["file"] = file
            di['servers'] = servers[num]
            # Contar el tiempo de cargas
            inicio = time.time()
            upload(file, servers[num])
            final = time.time()
            timef=final-inicio
            di['time'] = timef
            di['operation'] = 'upload'
            fileList.append(di)
            
        df = pd.DataFrame(fileList, columns = ['file','time','operation'])
        df.to_csv('upload.csv')

def pull():
    for key in fileList:
        print(key['file'] + " -> " + " del server con el puerto "+str(key['servers']))
        inicio = time.time()
        download(key['file'],key['servers'])
        final = time.time()
        timef=final-inicio
        di={}
        di['file'] = key['file']
        di['time'] = timef
        di['operation'] = 'download'

        fileList2.append(di)
        
    df = pd.DataFrame(fileList2, columns = ['file','time','operation'])
    df.to_csv('download.csv')


def main():
    flag = True
    while flag:
        print("\t¿Como desea distribuir la carga?")
        print("1\tHacer balanceo random")
        print("2\tHacer balanceo Round Robin")
        print("3\tHacer balanceo Hash")
        action = int(input("\t>"))
        
        if action == 1:
            print("\nDistribuyendo carga con balanceador aleatiorio...\n\n")
            push_files(action)
            flag = False
        elif action == 2:
            print("\nDistribuyendo carga con balanceador Round Robin...\n\n")
            push_files(action)
            flag = False
        elif action == 3:
            print("\nDistribuyendo carga con balanceador Hash...\n\n")
            push_files(action)
            flag = False
            
    print("\n\n\nDescargando archivos....")
    pull()
    
    print("Se han guardado los archivos con los tiempos de carga y descarga en el directorio actual.")

if __name__ == "__main__":
    main()
