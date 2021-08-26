import socket
import os
import pyautogui as pag
import time
import threading

socket.setdefaulttimeout(10)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def getIP():
    return socket.gethostbyname(socket.gethostname())


def checkIPchange():
    global socketThread, threadGoing
    while True:
        ip = getIP()
        print(f'ip is {ip}')
        time.sleep(10)
        newIP = getIP()
        print(f'newIP is {newIP}')
        if ip != newIP:
            print('ip changed')
            threadGoing = False
            socketThread.join()
            socketThread.start()
        else:
            print('not changed')


def startSockets():
    global threadGoing
    ip = getIP()
    port = 1024

    server.bind((ip, port))

    print(f"bind to {ip}")

    server.listen(100)

    while threadGoing:
        (client, address) = server.accept()
        print(f"connected to {address}")
        while threadGoing:
            try:
                data = client.recv(1024)
                if not data:
                    print('disconnected')
                    break
                if data != b'':
                    message = data.decode('utf-8').strip()
                    print(message)
                    if message == 'exit':
                        client.send('exited'.encode('utf-8'))
                        break
                    elif message == 'video':
                        pag.hotkey('ctrl', 'e')
                    elif message == 'audio':
                        pag.hotkey('ctrl', 'd')
            except Exception as ex:
                client.send(str(ex))


threadGoing = True

socketThread = threading.Thread(target=startSockets)
ipThread = threading.Thread(target=checkIPchange)

socketThread.start()
ipThread.start()
