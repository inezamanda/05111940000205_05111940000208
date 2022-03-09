import socket
import sys
import select
import os.path
from time import sleep

# Constants
HOST = "localhost"
PORT = 5000
BUFFER_SIZE = 1024
DATASET = './dataset'

server_address = (HOST, PORT)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

def send_file(file_name):
    file_path = f"{DATASET}/{file_name}"
    if os.path.isfile(file_path):
        file = open(file_path, "rb")
        sock.send("File is found".encode('utf-8'))
        sleep(0.05)
        data = file.read(BUFFER_SIZE)
        while True:
            sock.send(data)

            # syarat file 1MB
            if(len(data) > BUFFER_SIZE):
                data = file.read(BUFFER_SIZE)
            else:
                break
        file.close()
        print(f'SENDING --> Server is sending file { file_name }')
    else:
        print(f'ERROR --> Server failed to send file {file_name}')
        sock.send("File is not found".encode('utf-8'))

try:
    print("START SERVER")
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            
            else:            	
                print("Kamu dimana?" + str(sock.getpeername()))
                filename = sock.recv(BUFFER_SIZE).decode('utf-8')
                print(filename)
                send_file(filename)

except KeyboardInterrupt:  
    print('Server Closed')      
    server_socket.close()
    sys.exit(0)