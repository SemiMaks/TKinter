# Эта программа показывает пустое окно.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Входим в главный цикл tkinter.
        tkinter.mainloop()


# Создаём экземпляр класса.
my_gui = MyGUI()
