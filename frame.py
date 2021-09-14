# Эта программа создаёт надписи в двух разных рамках.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создаём две рамки: верхней и нижней части.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создаём три эдемента интерфейса Label.
        self.label1 = tkinter.Label(self.top_frame, text='Мигнуть')
        self.label2 = tkinter.Label(self.top_frame, text='Моргнуть')
        self.label3 = tkinter.Label(self.top_frame, text='Кивнуть')

        # Упакуем надписи, расположенные в верхней рамке,
        # применив аргумент side='top',
        # чтобы расположить их рдну под другой.

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Создаём три элемента интерфейса
        # Label для нижней рамки.

        self.label4 = tkinter.Label(self.bottom_frame, text='Мигнуть')
        self.label5 = tkinter.Label(self.bottom_frame, text='Моргнуть')
        self.label6 = tkinter.Label(self.bottom_frame, text='Кивнуть')

        # Упакуем надписи, расположенные в нижней рамке,
        # применив аргумент side='left',
        # чтобы расположить их горизонтально слева рамки.

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Упаковываем рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл.
        tkinter.mainloop()


my_gui = MyGUI()
