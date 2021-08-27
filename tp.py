import socket
import ifaddr

print("Running...")

# socket.setdefaulttimeout(60)


def getAllIPs():
    allIPs = []
    adapters = ifaddr.get_adapters()
    for adapter in adapters:
        for ip in adapter.ips:
            if ip.network_prefix == 24:
                allIPs.append(ip.ip)
    return allIPs


print(getAllIPs())

exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())
PORT = 1024
server.bind((IP, PORT))
print(f'Bind to {IP}:{PORT}')

server.listen(10)


while True:
    (client, addr) = server.accept()
    print(f'Connected to {addr}')
    client.send('You are connected to server'.encode('utf-8'))
    while True:
        data = client.recv(1024)
        if not data:
            break
        msg = data.decode('utf-8').strip()
        if msg == 'exit':
            break
        else:
            print(msg)
