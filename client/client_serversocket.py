import socket
import sys

HOST, PORT = "localhost", 9999
BUFFER_SIZE = 1024

def send_msg(msg):
    message = msg.encode('utf-8')
    client.send(message)

def receive(data, msg):
    idx = 0
    file = open(msg, "wb")
    head, tail = data.split(b'\n\n\n',1)
    print(head.decode() + '\n\n\n')
    while True:
        if(idx == 0):
            file.write(tail)
        else:
            file.write(data)
        if(len(data) > BUFFER_SIZE):
            data = client.recv(BUFFER_SIZE)
        else:
            break
        i += 1
    file.close
    print("Download success Yeyy\n")

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # Connect to server and send data
    client.connect((HOST, PORT))
    try:
        while True:
            print("To download a file please enter command 'unduh <file_name>'")
            command = input(">> ")
            messages = command.split()
            if messages[0].__eq__("unduh"):
                send_msg(messages[1])
                data = client.recv(BUFFER_SIZE)
                print(data)

                if (data.decode('utf-8').__eq__("File is not found")):
                    print(data.decode('utf-8'))
                else:
                    data = client.recv(BUFFER_SIZE)
                    receive(data, messages[1])
            else: 
                print ("Command not recognized")

    except KeyboardInterrupt:        
        print("Disconnnected from " + str(client.getpeername()))
        client.close()
        sys.exit(0)
