import tkinter as tk
from tkinter import messagebox
import pymysql as pm

class Register(tk.Frame):  
    def __init__(self, master):  
        super().__init__(master) 
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # First Name
        self.first_name_var = tk.StringVar()
        self.first_name_inp_label = tk.Label(self, text="Please enter your first name:")
        self.first_name_inp_label.grid(row = 0, column = 0, padx=10, pady=10)
        self.first_name_inp_entry = tk.Entry(self, textvariable=self.first_name_var)
        self.first_name_inp_entry.grid(row=0, column=1, padx=10, pady=10)

        # Last Name
        self.last_name_var = tk.StringVar()
        self.last_name_inp_label = tk.Label(self, text="Please enter your last name:")
        self.last_name_inp_label.grid(row = 1, column = 0, padx=10, pady=10)
        self.last_name_inp_entry = tk.Entry(self, textvariable=self.last_name_var)
        self.last_name_inp_entry.grid(row=1, column=1, padx=10, pady=10)

        # Date of Birth
        self.dob_var = tk.StringVar()
        self.dob_inp_label = tk.Label(self, text="Please enter your Date of Birth:")
        self.dob_inp_label.grid(row = 2, column = 0, padx=10, pady=10)
        self.dob_inp_entry = tk.Entry(self, textvariable=self.dob_var)
        self.dob_inp_entry.grid(row=2, column=1, padx=10, pady=10)

        # Email
        self.email_var = tk.StringVar()
        self.email_inp_label = tk.Label(self, text="Please enter your email:")
        self.email_inp_label.grid(row = 3, column = 0, padx=10, pady=10)
        self.email_inp_entry = tk.Entry(self, textvariable=self.email_var)
        self.email_inp_entry.grid(row=3, column=1, padx=10, pady=10)

        # Contact Number
        self.contact_number_var = tk.StringVar()
        self.contact_number_inp_label = tk.Label(self, text="Please enter your contact number:")
        self.contact_number_inp_label.grid(row = 4, column = 0, padx=10, pady=10)
        self.contact_number_inp_entry = tk.Entry(self, textvariable=self.contact_number_var)
        self.contact_number_inp_entry.grid(row=4, column=1, padx=10, pady=10)

        # Username
        self.username_var = tk.StringVar()
        self.username_inp_label = tk.Label(self, text="Please enter your desired username:")
        self.username_inp_label.grid(row = 5, column = 0, padx=10, pady=10)
        self.username_inp_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_inp_entry.grid(row=5, column=1, padx=10, pady=10)

        # Password
        self.password_var = tk.StringVar()
        self.password_inp_label = tk.Label(self, text="Please enter your desired password:")
        self.password_inp_label.grid(row = 6, column = 0, padx=10, pady=10)
        self.password_inp_entry = tk.Entry(self, textvariable=self.password_var, show="*")
        self.password_inp_entry.grid(row=6, column=1, padx=10, pady=10)

        # Enter Button
        self.enter_button = tk.Button(self, text="ENTER", command= self.data_to_sql)
        self.enter_button.grid(row = 7, columnspan=2, padx=10, pady=10)

        # Exit Button
        self.exit_button = tk.Button(self, text="EXIT", command= self.exit)
        self.exit_button.grid(row = 8, columnspan=2, padx=10, pady=10)

    def exit(self):
        """
        Method to handle exit upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.hide_register()
        self.master.show_login()

    def show_register(self):
        """
        Method to show the register in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_register(self):
        """
        Method to hide the register frame.
        """
        self.place_forget()

    def data_to_sql(self):
        first_name_value = self.first_name_var.get()
        last_name_value = self.last_name_var.get()
        dob_value = self.dob_var.get()
        email_value = self.email_var.get()
        contact_number_value = self.contact_number_var.get()
        username_value = self.username_var.get()
        password_value = self.password_var.get()

        conn= pm.connect(host='localhost', user='root', password='FIT1056') 
        cr=conn.cursor() 
        cr.execute("create database if not exists Users") 
        cr.execute("use Users") 
        cr.execute("create table if not exists students (first_name varchar(20), last_name varchar(20), DOB date, email varchar(20), contact_number int, username varchar(20), password varchar(20))") 
        dob_formatted = f"{dob_value[6:]}-{dob_value[3:5]}-{dob_value[:2]}"  # Converts to 'YYYY-MM-DD'
        values_tuple = (first_name_value, last_name_value, dob_formatted, email_value, int(contact_number_value), username_value, password_value)
        cr.execute("INSERT INTO students (first_name, last_name, DOB, email, contact_number, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", values_tuple)

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data has been stored successfully!")
