import socket
import sys

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024

server_address = (HOST, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

def send_msg(msg):
    message = msg.encode('utf-8')
    client_socket.send(message)

def receive(msg):
    file = open(msg, "wb")
    while True:
        data = client_socket.recv(BUFFER_SIZE)
        file.write(data)
        if(len(data) >= BUFFER_SIZE):
            data = client_socket.recv(BUFFER_SIZE)
        else:
            break
    file.close
    print("Download success Yeyy")

try:
    print("To download a file please enter command 'unduh <file_name>'")
    while True:
        command = input(">> ")
        messages = command.split()
        if messages[0].__eq__("unduh"):
            send_msg(messages[1])
            data = client_socket.recv(BUFFER_SIZE)
            print(data)

            if (data.decode('utf-8').__eq__("File is not found")):
                print(data.decode('utf-8'))
            else:
                receive(messages[1])
        else: 
            print ("Command not recognized")

except KeyboardInterrupt:
    print("Disconnnected from " + str(client_socket.getpeername()))
    client_socket.close()
    sys.exit(0)