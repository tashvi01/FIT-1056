import tkinter as tk
from GUI.Login_UI import LoginScreen

class EmpowerU(tk.Tk):
    def __init__(self, title, width, height, bg):
        """
        Constructor for the EmpowerU class.

        Parameter(s):
        - title: str
        """
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")
        super().configure(bg=bg)

        self.login = LoginScreen(master=self)
        self.show_login()

    def show_login(self):
        """
        Displays the login page to make it visible in the main window.
        """
        self.login.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_login(self):
        """
        Hides the login page to make it invisible in the main window.
        """
        self.login.place_forget()

if __name__ == "__main__":
    # DO NOT MODIFY
    pass
