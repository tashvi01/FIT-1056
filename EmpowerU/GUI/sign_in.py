import tkinter as tk
class SignIn(tk.Frame):
    def __init__(self, master):
        """
        Constructor for SignIn class. Initializes the frame and adds widgets to it.
        
        Parameters:
        master (tk.Tk): The root window of the application.
        
        Returns:
        None
        """
        super().__init__(master)
        self.mainframe = tk.Frame(master, padx=10, pady=10)  # Increased padding for mainframe
        self.mainframe.grid(column=0, row=0, sticky="nsew")

        # Load logo image
        self.logo = tk.PhotoImage(file="logo.png")
        self.label = tk.Label(self.mainframe, image=self.logo, width=750, height=300)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, columnspan=2, sticky=tk.S, pady=10)

        # Welcome heading
        self.welcome_label = tk.Label(self.mainframe, text="Welcome to EmpowerU", font=("Arial Bold", 20))
        self.welcome_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Create username label and entry
        self.username_label = tk.Label(self.mainframe, text="Username:")
        self.username_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)  # Align label to the right
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self.mainframe, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create password label and entry
        self.password_label = tk.Label(self.mainframe, text="Password:")
        self.password_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)  # Align label to the right
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.mainframe, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        # Alert message label
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self.mainframe, textvariable=self.alert_var, fg="red")
        self.alert_label.grid(row=4, column=0, columnspan=2, pady=5)  # Center alert message

        # Create sign-in button
        self.signin_button = tk.Button(self.mainframe, text="Sign In")
        self.signin_button.grid(row=5, column=1, padx=10, pady=5)

        # Create sign-out button
        self.signout_button = tk.Button(self.mainframe, text="Sign Out", command=self.sign_out)
        self.signout_button.grid(row=5, column=0, padx=10, pady=5)
    def sign_in(self):

        username = self.username_var.get()
        password = self.password_var.get()
        "This was code when I used my own authenticate method, get rid of when you implement your own"
        # student_user = Student.authenticate(username, password)
        # if isinstance(student_user, Student):
        #     student_page = StudentPage(self.master, student_user)
        #     self.hide_signin_page()
        #     student_page.show_student_page()
        # else:
        #     self.alert_var.set("Invalid username or password. Please try again.")
        self.username_var.set("")
        self.password_var.set("")
    def hide_signin_page(self):
        self.mainframe.grid_forget()
    def sign_out(self):
        # Logic for sign out can be implemented here
        pass
