#char client side

from email import message, message_from_binary_file
from http import client
from pickle import BYTEARRAY8
import socket;



#DIFENE CONSTANS TO BE USED
DEST_IP = socket.gethostbyname(socket.gethostname());
DEST_PORT = 12345;
ENCODER = "utf-8";
BYTESIZE = 1024;

#Create a client socket and connect the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
client_socket.connect((DEST_IP, DEST_PORT));

#Send/Recive messages
while True:
    #recieve information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER);

    #Quit if the connected server wants to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER));
        print("Finalizando chat...adiós");
        break;
    else:
        print(f"{message}");
        message = input("Mensaje: ");
        client_socket.send(message.encode(ENCODER));


#Close de client socket
client_socket.close();