import tkinter as tk
from Register import Register

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.mainframe = tk.Frame(master, padx=3, pady=12)
        self.mainframe.grid(column=0, row=0, sticky="nsew")

        # Load logo image
        self.logo = tk.PhotoImage(file="logo.png")  
        self.label = tk.Label(self.mainframe, image=self.logo, width=750, height=300)  
        self.label.image = self.logo 
        self.label.grid(row=0, column=0, sticky=tk.S, padx=10, pady=10) 

        # Welcome heading
        self.welcome_label = tk.Label(self.mainframe, text="Welcome to EmpowerU", font=("Arial Bold", 20))
        self.welcome_label.grid(row=1, column=0, pady=10)

        # Create buttons below the welcome label
        self.register_button = tk.Button(self.mainframe, text="Register", command= self.open_register)
        self.register_button.grid(row=2, column=0, padx=10, pady=5)

        self.signin_button = tk.Button(self.mainframe, text="Sign In")
        self.signin_button.grid(row=3, column=0, padx=10, pady=5)

        self.signout_button = tk.Button(self.mainframe, text="Sign Out")
        self.signout_button.grid(row=4, column=0, padx=10, pady=5)

        # Button to shut down
        self.shutdown_button = tk.Button(self.mainframe, text="Shut down", command=root.destroy)
        self.shutdown_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def open_register(self):
        # Clear the mainframe
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        # Initialize and display the Register class
        register_frame = Register(self.master)
        register_frame.grid(sticky="nsew")

root = tk.Tk()
root.title("Music School Management System")
login = LoginScreen(root)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
login.grid(sticky="nsew")
root.mainloop()