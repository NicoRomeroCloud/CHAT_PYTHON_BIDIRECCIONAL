#chat server side  
from ctypes.wintypes import PLARGE_INTEGER
from email import message, message_from_string
from http import client
import socket

#define constans to be used

HOST_IP= socket.gethostbyname(socket.gethostname());
HOST_PORT= 12345;
ENCODER = "utf-8";
BYTESIZE = 1024;

#create a server socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_socket.bind((HOST_IP, HOST_PORT));
server_socket.listen();

#Accept any incoming connection and let them know they are connected
print("Servidor corriendo...");
client_socket, client_address = server_socket.accept();
client_socket.send("Estas conecyado al servidor... C:".encode(ENCODER));

#sen/recieve messages
while True:
    #Recieve information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER);

    #quit if the client socket wants to quit, else display the message
    if message == "quit":
        client_socket.send("quit".encode(ENCODER));
        print("Finalizando chaooo");
        break;
    else:
        print(f"{message}");
        message = input("Mensaje: ");
        client_socket.send(message.encode(ENCODER));

#CLOSE THE SOCKET
server_socket.close();