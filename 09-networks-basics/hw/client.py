import socket
import sys
import threading
import time

key = 2080
exit = False
join = False


def read_sock(name, socket):
    while not exit:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                decrypt = ""
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif not k or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)

        except:
            pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost', 9090)
sock.connect(server)
sock.setblocking(0)

alias = input('Name:')

rT = threading.Thread(target=read_sock, args=('RecvThred', sock))
rT.start()

while not exit:
    if not join:
        sock.sendto((alias + ' join chat').encode('utf-8'), server)
        join = True
    else:
        try:
            message = input()

            crypt = ""
            for i in message:
                crypt += chr(ord(i) ^ key)
            message = crypt

            if message != "":
                sock.sendto((alias + ":" + message).encode("utf-8"), server)

        except:
            sock.sendto((alias + 'left chat').encode("utf-8"), server)
            exit = True

rT.join()
sock.close()