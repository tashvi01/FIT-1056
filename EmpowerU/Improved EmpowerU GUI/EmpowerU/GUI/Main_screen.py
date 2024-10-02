import tkinter as tk
from GUI.Login_UI import SignIn

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

        self.signin = SignIn(master=self)
        self.show_signin()

    def show_signin(self):
        """
        Displays the signin page to make it visible in the main window.
        """
        self.signin.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_signin(self):
        """
        Hides the signin page to make it invisible in the main window.
        """
        self.signin.place_forget()

if __name__ == "__main__":
    # DO NOT MODIFY
    pass
