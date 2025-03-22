import socket
import threading
from bot import Bot


class Server():
    def __init__(self, ip, port):
        self.SERVER_IP = ip  # IP server
        self.SERVER_PORT = port  # Port server
        self.bot = Bot()
        self.server_commands = {"/?": self.helpCommand,
                                "/help": self.helpCommand,
                                "/start": self.helpCommand,
                                "/serverstatus": print("Not available yet")}
        self.connected_clients = {}  # Object socket connections
        self.special_characters = """!@#$%^&*()-+?_=,<>/\"\'"""  # sanatization

    def helpCommand(self, chatid):
        """This function is the /help of the telegram bot"""
        text = """Welcome to my bot, here is a list of valid commands:
        /help, /start, /?: Returns a list of valid commands;
        /serverstatus: Return the status of the running server."""

        self.bot.sendMessages(chatid, text)

    def validadeCommand(self, command):
        """validade the command and the format"""
        if ":" in command:
            parts = command.split(":", 1)
            if len(parts) == 2 and parts[1] not in self.special_characters:
                return parts[1]

        return None

    def interpretCommands(self, socket, address):
        print(f"Client connected: {address}")
        # parameter = None

        try:
            while True:
                command, chatid = self.bot.GetMessages()
                if not command or not chatid:
                    continue  # Restart the cycle until to get a new msg

                print(f"Received command: {command} from chat {chatid}")

                if command in self.server_commands.keys():
                    self.server_commands[command](chatid)
                    continue
        except Exception as err:
            print(f"An error occurred: {err}")

    def startServer(self):
        """Function which instantiate the server and accept connections"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.SERVER_IP, self.SERVER_PORT))
        print(f"Server listening on {self.SERVER_IP}:{self.SERVER_PORT}")
        s.listen()

        try:
            while True:
                client_socket, address = s.accept()
                ip = address[0]
                self.connected_clients[(ip, address[1])] = socket
                client_thread = threading.Thread(
                    target=self.interpretCommands,
                    args=(client_socket, address), daemon=True).start()

        except Exception as Err:
            print(f"An error occurred: {Err}")

        except KeyboardInterrupt:
            print("The server was forced to shutdown")

        finally:
            s.close()


server = Server('localhost', 1337)
server.startServer()
