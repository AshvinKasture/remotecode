import socket
import os
import pyautogui as pag

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1024

server.bind(('192.168.29.184', port))

print(f"bind to {socket.gethostname()}")

server.listen(50)


while True:
    (client, address) = server.accept()
    print(f"connected to {address}")
    while True:
        try:
            data = client.recv(1024)
            if data != b'':
                message = data.decode('utf-8').strip()
                print(message)
                if message == 'exit':
                    break
                elif message == 'video':
                    pag.hotkey('ctrl', 'e')
                    # print('here')
                    # pag.moveTo(500, 500)
                    # pag.rightClick()
                elif message == 'audio':
                    pag.hotkey('ctrl', 'd')
        except Exception as ex:
            client.send(str(ex))
