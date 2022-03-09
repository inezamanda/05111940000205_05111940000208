import socketserver
import os.path
from time import sleep

from server.server_select import send_file

# Constant
BUFFER_SIZE = 1024
DATASET = './dataset'

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def send_file(self, file_name):
        file_path = f"{DATASET}/{file_name}"
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
            header = ("file-name: " + file_name + ",\nfile-size: " + str(file_size) + ",\n\n\n").encode('utf-8')

            file = open(file_name, "rb")
            self.request.send("File is found".encode('utf-8'))
            sleep(0.05)
            data = file.read(BUFFER_SIZE - len(header))
            data += header

            while True:
                self.request.send(data)

                # syarat file 1MB
                if(len(data) > BUFFER_SIZE):
                    data = file.read(BUFFER_SIZE)
                else:
                    break
            file.close()
            print(f'[SENDING] Server is sending file {file_name}')
        else:
            print(f'[ERROR] Server failed to send file { file_name }')
            self.request.send("File is not found".encode('utf-8'))

    def handle(self):
        while True:
            try:
                print("Kamu dimana?" + str(self.client_address))
                filename = self.request.recv(BUFFER_SIZE).decode('utf-8')
                print(filename)
                send_file(self, filename)
            except ConnectionAbortedError:
                print("Connection Aborted by client")
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

