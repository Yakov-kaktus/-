from tkinter import *
t = Tk()
c = Canvas(t, width=1000, height=500)
t.title("go!")
c.pack()

pi = PhotoImage(file="sbk.png")
ig = c.create_image(500,250,anchor=NW,image=pi)


def movs(event):
    if event.keysym == "Up":
        c.move(ig, 0, -10)
    elif event.keysym == "Down":
        c.move(ig, 0, 10)
    elif event.keysym == "Right":
        c.move(ig, 10, 0)
    elif event.keysym == "Left":
        c.move(ig, -10, 0)
c.bind_all('<Key>', movs)
