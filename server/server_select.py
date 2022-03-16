import socket
import select
import sys
import os.path
from time import sleep


server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

DATASET = './dataset'

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            
            else:
                print("Waiting for " + str(sock.getpeername()))
                filename = sock.recv(1024).decode('utf-8')
                file_path = f"{DATASET}/{filename}"
                print(file_path)  
                
                # i = 0     	    
                
                if os.path.exists(file_path): 
                    file = open(file_path, "rb")
                    sock.send("File ditemukan".encode('utf-8'))
                    sleep(0.05)
                    l = file.read(1024)
                    while l:
                        sock.send(l)
                        if (len(l) < 1024):
                            break
                        else: 
                            l = file.read(1024)
                    file.close()
                    print("Server ready!")
                else: 
                    sock.send("File tidak ditemukan".encode())

except KeyboardInterrupt:   
    print("Closed")     
    server_socket.close()
    sys.exit(0)