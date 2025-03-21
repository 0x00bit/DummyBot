import socket
import sys
import time
import logging
import threading

class Server():
    def __init__(self, ip, port):
        self.SERVER_IP = ip  # IP server
        self.SERVER_PORT = port  # Port server
        self.server_commands = ["/?","/help","/serverstatus"]  # Server commands
        self.connected_clients = {}  # Object socket connections
    
    def handleConnection(self, socket, address):
        print(f"Client connected: {address}")
        ip = address[0]
        print(ip)

    def startServer(self):
        """Function which instantiate the server and accept connections"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.SERVER_IP, self.SERVER_PORT))
        print(f"Server listening on {self.SERVER_IP}:{self.SERVER_PORT}")
        s.listen()
    
        try:
            while True:
                client_socket, address = s.accept()
                client_thread = threading.Thread(
                    target=self.handleConnection,
                    args=(client_socket, address), daemon=True).start()

        except Exception as Err:
            print(f"An error occurred: {Err}")
        
        except KeyboardInterrupt:
            print(f"The server was forced to shutdown")

        finally:
            s.close()


teste = Server("localhost", 1337)
teste.startServer()
            