import socket

ROBOT_IP="192.168.0.10"
PORT=30002
file_name="pallet.script"

tcp_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((ROBOT_IP, PORT))

try:
    with open(file_name) as f:
        script=f.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Não foi possível abrir o arquivo")

tcp_socket.sendall(script.encode("utf-8"))
tcp_socket.close()
