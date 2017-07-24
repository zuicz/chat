import socket
import threading
import time

host = str(input("Host -> "))
port = int(input("Port -> "))

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.reсvfrom(1024)
                print (str(data))
        except:
            pass
        finally:
            tLock.release()


server = (host, port)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=('RecvThread', s))
rT.start()

alias = input("Nickname: ")
message = input(alias + '-> ')
while message != 'q':
    if message != '':
        s.sendto((alias + ": " + message).encode(), server)
    tLock.acquire()
    message = input(alias + '-> ')
    tLock.release()
    time.sleep(0.2)
shutdown = True
rT.join()
s.close()