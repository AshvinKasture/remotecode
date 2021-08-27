import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1024

client.connect(('192.168.29.184', port))

message = 'audio'

encodedMessage = message.encode('utf-8')

client.send(encodedMessage)

client.close()
