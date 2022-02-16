#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True: # <-- this isn't boilerplate
   c, addr = s.accept()     # Establish connection with client.
   
   # Above this is boilerplate ---------
   
   print("Please enter a message: ", end="")
   message = input()
   print('Got connection from ' + str(addr[1]))
   c.send(message.encode())
   c.close()                # Close the connection
