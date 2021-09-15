# Эта программа демонстрирует элемент интерфейса Button
# (когда пользователь нажимает кнопку Button,
# на экран выводится информационное диалоговое окно)

import tkinter
import tkinter.messagebox
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Button widget.
        # На кнопке появится текс "Нажми меня!".
        # При  нажатии кнопки исполняется метод do_something.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                        command=self.do_something)

        # Создаём кнопку "Выйти"
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        # Упаковать элемент интерфейса Button и Quit.
        self.my_button.pack()
        self.quit_button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод do_something является функцией обратного вызова
    # для элемента интерфейса Button.
    def do_something(self):
        # Показать информационное диалоговое окно.
        messagebox.showinfo('Реакция',
                                    'Благодарю, что нажали кнопку')


# Создаём экземпляр класса MyGUI.
my_gui = MyGUI()
