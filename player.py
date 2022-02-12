import socket
import pygame
from seting import *

pygame.init()
step = 10
r = step
screen = pygame.display.set_mode((640, 480))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect(('localhost',10000))
x = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -r
            elif event.key == pygame.K_RIGHT:
                x = r
            elif event.key == pygame.K_UP:
                y = -r
            elif event.key == pygame.K_DOWN:
                y = r
    j = s.recv(1024)
    d = j.decode()


    s.send(str(x).encode())
    s.send(str(y).encode())
    print(d)
