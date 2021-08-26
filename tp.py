import threading
import time
import socket


def print_cube(num):
    for i in range(num):
        time.sleep(0.2)
        print("Cube: {} = {}".format(i, i*i*i))


def print_square(num):
    for i in range(num):
        print("Square: {} = {}".format(i, i * i))
        time.sleep(0.5)


def getIP():
    return socket.gethostbyname(socket.gethostname())


def checkIPchange():
    global changeIP
    while True:
        ip = getIP()
        print(f'ip is {ip}')
        time.sleep(10)
        newIP = getIP()
        print(f'newIP is {newIP}')
        if ip != newIP:
            print('ip changed')
            changeIP = True
            break
        else:
            print('not changed')


changeIP = False


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(1000,))
    t1 = threading.Thread(target=checkIPchange)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
