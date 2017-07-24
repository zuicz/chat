import socket
import time

host = '127.0.0.1'
port = 4444

clients=[]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quit = False
print ('Добро пожаловать.')

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        if 'Quit' in str(data):
            quit = True
        if addr not in clients:
            clients.append(addr)
        
        print (time.ctime(time.time()) + str(addr) + ' ' + str(data))
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()