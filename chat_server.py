from ctypes.wintypes import PLARGE_INTEGER
from email import message, message_from_string
from http import client
import socket

#definiendo constantes a usar
HOST_IP= socket.gethostbyname(socket.gethostname());
HOST_PORT= 12345;
ENCODER = "utf-8";
BYTESIZE = 1024;

#creación del socket del servidor

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_socket.bind((HOST_IP, HOST_PORT));
server_socket.listen();

#aceptando cualquier conexión entrante y haciedole saber que esta conectado.
print("Servidor corriendo...");
client_socket, client_address = server_socket.accept();
client_socket.send("Estas conecyado al servidor... C:".encode(ENCODER));

#enviar/recibir mensajes
while True:
    #recibiendo información(mensajes) del cliente
    message = client_socket.recv(BYTESIZE).decode(ENCODER);

    #salir del socket cuando el cliente quiera, si no, se muestra el mensaje enviado por el cliente
    if message == "salir":
        client_socket.send("salir".encode(ENCODER));
        print("Finalizando servidor chaooo");
        break;
    else:
        print(f"{message}");
        message = input("Mensaje: ");
        client_socket.send(message.encode(ENCODER));

#cerrando el socket
server_socket.close();