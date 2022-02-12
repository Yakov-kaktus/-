import socket
import time

socket_g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_g.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
socket_g.bind(('localhost', 10000))
socket_g.setblocking(0)
socket_g.listen(5)
p_s = []
while True:
    try:
        new_socket,addr=socket_g.accept()
        socket_g.setblocking(0)
        p_s.append(new_socket)
        time.sleep(1)
    except:
        print("нету никого")
    try:
        for s in p_s:
            d = s.recv(1024)
            j = d.decode()
            print(j)
    except:
        print("нет послания")
    for s in p_s:
        try:
            s.send("послание с сервера".encode())
        except:
            p_s.remove(s)
            s.close()
    time.sleep(1)
Socket.close()
