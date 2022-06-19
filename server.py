# Author Name: Casey Hawkins
# Description: Server portion of Client/Server chat. Only allows one connection at a time.
# Sources: Computer Networking: A Top-Down Approach, 7th ed., Kurose, J.
# Sources: https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# Sources: https://www.geeksforgeeks.org/simple-chat-room-using-python/
# Sources: Programming Project: Sockets and HTTP http_server.py and connect_socket.py files

import socket

# Flag set to False. When "/q" is detected, set flag to True
connectionClosed = False

# Startup server on localhost at port 7777
serverSocket = socket.socket()
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
port = 7777
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((hostName, port))

# Listen for requests from clients. Max 1 queued connection
serverSocket.listen(1)
print("\nServer listening on: localhost (", ipAddress, ") on port: ", port, "\n")

# Accept client request
connectionSocket, addr = serverSocket.accept()
print("Connected by (", addr[0], ",", addr[1], ")\n")
print("Waiting for message...")

# Decode received message from client
message = connectionSocket.recv(1024)
message = message.decode()
# If message received is "/q", then quit connection
if message == "/q":
    connectionSocket.send(message.encode())
    connectionSocket.close()
    serverSocket.close()
    connectionClosed = True
else:
    # Print client message
    print("Client", ":", message)
    print("Type /q to quit")
    print("Enter message to send...")

    # Respond to client message
    message = input(str("Server: "))
    if message == "/q":
        connectionSocket.send(message.encode())
        connectionSocket.close()
        serverSocket.close()
        connectionClosed = True
    else:
        connectionSocket.send(message.encode())
    
    # If connectionClosed flag is not set, continue loop until broken by "/q" message
    while not connectionClosed:
        message = connectionSocket.recv(1024)
        message = message.decode()
        if message == "/q":
            connectionSocket.send(message.encode())
            break
        print("Client", ":", message)
        message = input(str("Server: "))
        if message == "/q":
            connectionSocket.send(message.encode())
            break
        connectionSocket.send(message.encode())

# Close connectionSocket and serverSocket
connectionSocket.close()
serverSocket.close()