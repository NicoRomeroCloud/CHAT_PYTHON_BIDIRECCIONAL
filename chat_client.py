from email import message, message_from_binary_file
from http import client
from pickle import BYTEARRAY8
import socket;

#definiendo constantes a usar
DEST_IP = socket.gethostbyname(socket.gethostname());
DEST_PORT = 12345;
ENCODER = "utf-8";
BYTESIZE = 1024;

#creando el socket de conexión cliente/servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
client_socket.connect((DEST_IP, DEST_PORT));

#enviar/recibir mensajes
while True:
    #recibir info del servidor
    message = client_socket.recv(BYTESIZE).decode(ENCODER);

    #salir, si no, mostrar mensaje
    if message == "salir":
        client_socket.send("salir".encode(ENCODER));
        print("Finalizando chat...adiós");
        break;
    else:
        print(f"{message}");
        message = input("Mensaje: ");
        client_socket.send(message.encode(ENCODER));

#cerrando el socket del cliente
client_socket.close();