# Author Name: Casey Hawkins
# Description: Client portion of Client/Server chat.
# Sources: Computer Networking: A Top-Down Approach, 7th ed., Kurose, J.
# Sources: https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# Sources: https://www.geeksforgeeks.org/simple-chat-room-using-python/
# Sources: Programming Project: Sockets and HTTP http_server.py and connect_socket.py files

import socket

# Flag set to False. When "/q" is detected, set flag to True
connectionClosed = False

# Connect to localhost at port 7777
clientSocket = socket.socket()
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
port = 7777
clientSocket.connect((hostName, port))
print("\nConnected to: localhost (", ipAddress, ") on port: ", port, "\n")

# Enter message to send to server
print("Type /q to quit")
print("Enter message to send...")
message = input(str("Client: "))
# If message to send is "/q", then send message and quit connection
if message == "/q":
    clientSocket.send(message.encode())
    clientSocket.close()
    connectionClosed = True
else:
    # Send message to server
    clientSocket.send(message.encode())
    # Decode and receive message from server
    message = clientSocket.recv(1024)
    message = message.decode()
    if message == "/q":
        clientSocket.send(message.encode())
        clientSocket.close()
        connectionClosed = True
    else:
        print("Server", ":", message)

    # If connectionClosed flag is not set, continue loop until broken by "/q" message
    while not connectionClosed:
        message = input(str("Client: "))
        if message == "/q":
            clientSocket.send(message.encode())
            break
        clientSocket.send(message.encode())
        message = clientSocket.recv(1024)
        message = message.decode()
        if message == "/q":
            clientSocket.send(message.encode())
            break
        print("Server", ":", message)

clientSocket.close()