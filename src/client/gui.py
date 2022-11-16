import tkinter as tk

from client.login import LoginWindow
from client.resolvers import check_login


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn = tk.Button(self, text='Войти', command=self.login)
        btn.grid(row=0, column=0)


    def login(self):
        login_window = LoginWindow(self)
        login, password = login_window.open()
        if check_login(login, password):
            print('User ok')


if __name__ == '__main__':
    app = App()
    app.mainloop()

