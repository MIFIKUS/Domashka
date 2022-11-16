import tkinter as tk

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.login = tk.StringVar()
        self.password = tk.StringVar()

        label = tk.Label(self, text='Введите данные для аутентификации')
        entry_login = tk.Entry(self, textvariable=self.login)
        entry_pass = tk.Entry(self, textvariable=self.password)
        btn_ok = tk.Button(self, text="Ok", command=self.destroy)

        label.grid(row=0, columnspan=2)
        tk.Label(self, text='Логин:').grid(row=1, column=0)
        tk.Label(self, text='Пароль:').grid(row=2, column=0)
        entry_login.grid(row=1, column=1)
        entry_pass.grid(row=2, column=1)
        btn_ok.grid(row=3, columnspan=2)


    def open(self):
        self.grab_set()
        self.wait_window()
        user_login = self.login.get()
        user_pass = self.password.get()
        return user_login, user_pass
