import socket
import pyautogui as pag

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.29.184', 1024))


server.listen(10)

(client, address) = server.accept()

print(f"connected to {address}")

msg = ''

while True:
    data = client.recv(1024)
    msg = data.decode('utf-8').strip()
    print(msg)
    exec(msg)
