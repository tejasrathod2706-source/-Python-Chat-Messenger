import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

username = input("Choose a username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()