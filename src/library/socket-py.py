import socket
import uuid

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    node = uuid.getnode()
    macHex = uuid.UUID(int=node).hex[-12:]
    mac = []
    for i in range(len(macHex))[:]:
        print(macHex[i:i+2])
        mac.append(macHex[i:i+2])
    mac = ':'.join(mac)
    print(f'IP: {ip}, MAC: {mac}')

# IP: 127.0.0.1, MAC: 1e:00:fb:0a:af:86