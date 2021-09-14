# Эта программа показывает пустое окно.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Label,
        # элементы распологаются друг под другом.
        self.label1 = tkinter.Label(self.main_window, text='Первое окно')
        self.label2 = tkinter.Label(self.main_window, text='Второе окно')

        # Создаём элемент интерфейса Label с аргументом side='left',
        # элементы распологаются друг возле друга в родительском элементе
        # интерфейса максимально слева. Ещё есть 'right', 'top' и 'bottom'.        self.label3 = tkinter.Label(self.main_window, text='Третье окно')
        self.label3 = tkinter.Label(self.main_window, text='Третье окно')
        self.label4 = tkinter.Label(self.main_window, text='Четвёртое окно')

        # Вызываем метод pack элемента label.
        self.label1.pack()
        self.label2.pack()
        self.label3.pack(side='left')
        self.label4.pack(side='left')

        # Входим в главный цикл tkinter.
        tkinter.mainloop()


# Создаём экземпляр класса.
my_gui = MyGUI()
