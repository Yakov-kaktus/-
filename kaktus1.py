from tkinter import * #импортируем ткинтер
t = Tk() #задаём его отрисовку переменной
c = Canvas(t, width=1000, height=500) #создаём холст
t.title("go!") # делаем заголовок вкладки
c.pack() #упаковываем холст

pi = PhotoImage(file="sbk.png") #загружаем нашу собаку
ig = c.create_image(500,250,anchor=NW,image=pi) #делаем её объектом на экране


def movs(event): # задаём переменную и даём ей параметр событий( в конце мы укажем что это события с клавиатуры)
    if event.keysym == "Up": # при нажатии клавиши вверх
        c.move(ig, 0, -10)#двигаем вверх
    elif event.keysym == "Down":#при нажатии клавиши вниз
        c.move(ig, 0, 10) #двигаем вниз
    elif event.keysym == "Right": #
        c.move(ig, 10, 0)         #
    elif event.keysym == "Left":  #
        c.move(ig, -10, 0)        # и т д
c.bind_all('<Key>', movs)# при нажатии на клавишу любую срабатывает функция
