# Эта программа применяет GUI для получения
# трёх оценок и вывода среднего балла.

import tkinter


class TestAvg:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создаём пять рамок.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Создаём и упаковываем элементы интерфейса для оценки 1.
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Введите оценку 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Создаём и упаковываем элементы интерфейса для оценки 2.
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Введите оценку 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Создаём и упаковываем элементы интерфейса для оценки 3.
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Введите оценку 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Создаём и упаковываем элементы интерфейса для среднего балла.
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Средний балл:')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Создаём и упаковываем элементы интерфейса Button.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Усреднить',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковываем рамки.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()

    # Метод calc_avg является функцией обратного
    # вызова для элемента интерфейса calc_button.

    def calc_avg(self):
        # Получить три оценки и сохранить в переменные.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Вычисляем средний балл.
        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        # Обновляем элемент интерфейса avg_label,
        # сохранив значение self.average в объекте
        # StrinVar, на который ссылается avg.
        self.avg.set(self.average)


# Создаём экземпляр класса TestAvg.
test_avg = TestAvg()
