# Эта программа показывает пустое окно.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Label.
        self.label = tkinter.Label(self.main_window, text='Новое окно')

        # Вызываем метод pack элемента label.
        self.label.pack()

        # Входим в главный цикл tkinter.
        tkinter.mainloop()


# Создаём экземпляр класса.
my_gui = MyGUI()
