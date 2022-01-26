from tkinter import *
import time
t = Tk()
c = Canvas(t, width=1500, height=1000)
t.title("go!")
c.pack() 
o = PhotoImage(file="gh.png")
j = c.create_image(0,0,anchor=NW, image=o)
pi = PhotoImage(file="sbk.png")
ig = c.create_image(750,500,anchor=NW,image=pi)
k = c.coords(j) #координаты карты
y = k[0] # длина расстояние правого угла карты до правого угла точки
x = k[1] # высота расстоняние ширина
p = c.coords(ig) #cписок координат игрока
y2 = p[0]  # длина
x2 = p [1] # ширина высота
def movs(event):
    k = c.coords(j)
    p = c.coords(ig) #cписок координат игрока
    y2 = p[0]  # длина
    x2 = p [1] # ширина высота
    #движение камеры
    if event.keysym == "Up" and k[1] != 0 and x2 == 500:
        c.move(j, 0, 10)
    elif event.keysym == "Down" and k[1] != -2000 and x2 == 500:
        c.move(j, 0, -10)
    elif event.keysym == "Right" and k[0] != -1500 and y2 >= 750:
        c.move(j, -10, 0)
    elif event.keysym == "Left" and k[0] != 0 and y2 <= 750:
        c.move(j, 10, 0)
    #движение игрока
    elif event.keysym == "Up" :
        c.move(ig, 0, -10)
    elif event.keysym == "Down":
        c.move(ig, 0, 10)
    elif event.keysym == "Left":
        c.move(ig, -10, 0)
    elif event.keysym == "Right":
        c.move(ig, 10, 0)
c.bind_all('<Key>', movs)
 
