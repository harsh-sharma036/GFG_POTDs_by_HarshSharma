#Group Details
# Harsh Sharma (202111034)
# Ishita Agarwal (202111039)

# client 
import socket
import threading

# Client class
class ChatClient:
    def __init__(self, nickname, host='127.0.0.1', port=55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = nickname

        # Start receiving and sending messages
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

        self.send_thread = threading.Thread(target=self.send_messages)
        self.send_thread.start()

    # Receive messages from the server
    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("Error! Disconnected from the server.")
                self.client.close()
                break

    # Send messages to the server
    def send_messages(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('utf-8'))

# Start the client
if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    client = ChatClient(nickname)
