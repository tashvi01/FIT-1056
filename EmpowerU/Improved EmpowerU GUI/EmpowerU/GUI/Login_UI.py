import tkinter as tk
from GUI.Register import Register

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        super().configure(bg="navy")
        self.master = master

        # Load logo image
        self.logo = tk.PhotoImage(file="./GUI/logo.png")  
        self.label = tk.Label(master=self, image=self.logo, width=750, height=300, bg="navy")  
        self.label.grid(row=0, column=0, sticky=tk.S, padx=10, pady=10) 

        # Welcome heading
        self.welcome_label = tk.Label(master=self, text="Welcome to EmpowerU", font=("Arial Bold", 20), bg="navy", fg="white")
        self.welcome_label.grid(row=1, column=0, pady=10)

        # Create buttons below the welcome label
        self.register_button = tk.Button(master=self, text="Register", command = self.open_register, bg="deepskyblue", fg="black")
        self.register_button.grid(row=2, column=0, padx=10, pady=10)

        self.signin_button = tk.Button(master=self, text="Sign In", bg="deepskyblue", fg="black")
        self.signin_button.grid(row=3, column=0, padx=10, pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(master=self, text="Shut down", command=master.destroy, bg="deepskyblue", fg="black")
        self.shutdown_button.grid(row=5, column=0, padx=10, pady=10)

    def open_register(self):
        """
        Method to open the register upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.master.hide_login()

        # Initialize and display the Register class
        register_frame = Register(master=self.master)
        register_frame.show_register()

if __name__ == "__main__":
    pass
