# Эта программа конвертируе километры в мили,
# результат выводится в информационном диалоговои окне и
# в элемент Label в главном окне.


import tkinter
from tkinter import messagebox


class KMConverter:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создаём рамки для группировки элементов интерфейса.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Создаём элементы интерфейса для верхней рамки.
        self.promt_label = tkinter.Label(self.top_frame,
                                         text='Введите расстояние в километрах: ')
        self.conv_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковываем элементы верхней рамки.
        self.promt_label.pack(side='left')
        self.conv_entry.pack(side='left')

        # Создаём элементы интерфейса для средней рамки.
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Преобразовано в мили: ')

        # Объект StringVar связывает с выходной надписью,
        # для сохранения последовательности
        # пробелов используется метод set данного объекта.
        self.value = tkinter.StringVar()

        # Создаём надпись Label и связываем её с объектом StringVar,
        # любые значения, хранящиеся
        # в объекте StringVar, будут автоматически
        # выводиться в надписи label.
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        # Создаём элементы интерфейса средней рамки.
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Создаём элементы интерфейса Button для нижней рамки.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Конвертировать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        # Упаковываем кнопки.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Главный цикл.
        tkinter.mainloop()

        # Метод convert преобразует полученные в conv_entry
        # от пользователя километры в мили.

    def convert(self):
        km = float(self.conv_entry.get())

        # Конвертирование километров в мили.
        miles = km * 0.6214

        # Конвертируем мили в строковое значение и сохраняем в объекте StringVar.
        # В результате элемент miles_label будет автоматически обновлён.
        self.value.set(miles)

        # Показать результаты в информационном диалоговом окне.
        messagebox.showinfo('Результаты', str(km) +
                            'километров эквивалентно' +
                            str(miles) + ' милям.')


my_gui = KMConverter()
