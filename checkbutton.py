# Эта программа демонстрирует группу элементов Checkbutton.
import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создаём две рамки, одну для элементов Checkbutton
        # и ещё одну для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создаём три объекта IntVar для использования
        # с элементами Checkbutton.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Назначаем объектам Intvar значение 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Создаём элементы Checkbutton в рамке top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 3',
                                       variable=self.cb_var3)

        # Упаковываем элементы Checkbutton.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Создаём кнопку 'ОК' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        # Упаковываем элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковываем рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()

    # Метод chow_choice является функцией обратного вызова
    # для кнопки 'OK'.

    def show_choice(self):
        # Создаем строковое значение с сообщением.
        self.message = 'Вы выбрали:\n'

        # Определяем, какие элементы Checkbuttons были выбраны,
        # и составляем соответствующее сообщение.
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        # Выводим сообщение в информационном диалоговом окне.
        tkinter.messagebox.showinfo('Выбор', self.message)


# Создаём экземпляр класса MyGUI.
my_gui = MyGUI()
