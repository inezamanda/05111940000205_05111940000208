import socket
import sys

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)



try:
    while True:
        message = input("Enter command: ")
        messages = message.split()
        if messages[0] == "unduh":
            client_socket.send(messages[1].encode('utf-8'))
            l = client_socket.recv(1024)
            print(l)
            if (l.decode('utf-8') == "File tidak ditemukan"):
                print(l.decode('utf-8'))
            else:
                # i = 0 
                file = open(messages[1], "wb")
                l = client_socket.recv(1024)
                while l: 
                    file.write(l)
                    if (len(l) < 1024):
                        break
                    else: 
                        l = client_socket.recv(1024)
                    # print("loop" + str(i))
                    # i+=1
                file.close()
        else: 
            print ("Command tidak dikenali")

except KeyboardInterrupt:
    print("Disconnnected from " + str(client_socket.getpeername()))
    client_socket.close()
    sys.exit(0)