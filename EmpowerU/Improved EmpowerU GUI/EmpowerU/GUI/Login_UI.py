import tkinter as tk
import pymysql as pm

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
        super().__init__(master=master)
        super().configure(bg="navy")
        self.master = master

        # Load logo image
        self.logo = tk.PhotoImage(file="./GUI/logo.png")  
        self.label = tk.Label(master=self, image=self.logo, width=750, height=300, bg="navy")  
        self.label.grid(row=0, column=0, columnspan=2, sticky=tk.S, padx=10, pady=10) 

        # Welcome heading
        self.welcome_label = tk.Label(master=self, text="Welcome to EmpowerU", font=("Arial Bold", 20), bg="navy", fg="white")
        self.welcome_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Create username label and entry
        self.username_label = tk.Label(master=self, text="Username:", bg="navy", fg="white")
        self.username_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)  # Align label to the right
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        # Create password label and entry
        self.password_label = tk.Label(master=self, text="Password:", bg="navy", fg="white")
        self.password_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)  # Align label to the right
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        # Alert message label
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var, bg="navy", fg="red")
        self.alert_label.grid(row=4, column=0, columnspan=2, pady=10)  # Center alert message

        # Create sign-in button
        self.signin_button = tk.Button(master=self, text="Sign In", command= self.sign_in)
        self.signin_button.grid(row=6, column=0, columnspan=2, sticky="n", padx=10, pady=10)

        # Create sign-out button
        self.signout_button = tk.Button(master=self, text="Sign Out", command=self.sign_out)
        self.signout_button.grid(row=7, column=0, columnspan=2, sticky="n", padx=10, pady=10)

    def authenticate(self, username_input, password_input):
        """
        Checks whether the username and password entered are correct 

        Parameters:
        self
        username_input (str): the username the user enters
        password_input (str): the password the user enters

        Returns:
        None      
        """
        self.username_input = username_input
        self.password_input = password_input
        conn= pm.connect(host='localhost', user='root', password='FIT1056') 
        cr=conn.cursor() 
        cr.execute("USE Users")
        cr.execute("SELECT * from STUDENTS where username=%s and password=%s",(self.username_input, self.password_input))
        result = cr.fetchone()
        self.alert_var.set("")
        if result is None:
            self.alert_var.set("Invalid username or password. Please try again.")
        else:
            #show hompeage
            pass

        self.username_var.set("")
        self.password_var.set("")

        conn.commit()
        conn.close()

    def sign_in(self):
        """
        Stores the User's username and password and calls the authenticate function

        Parameters:
        self
     
        Outputs: 
        None
        """
        self.username = self.username_var.get()
        self.password = self.password_var.get()
        print(self.username)
        print(self.password)
        self.authenticate(self.username, self.password)
        
    def hide_signin_page(self):
        self.master.hide_signin()
        
    def sign_out(self):
        # Logic for sign out can be implemented here
        pass
