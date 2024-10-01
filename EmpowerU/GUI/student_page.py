import tkinter as tk
class StudentPage(tk.Frame):
    def __init__(self, master,student_user):
        """
        Constructor for StudentPage class. Initializes the frame and adds widgets to it.
        
        Parameters:
        master (tk.Tk): The root window of the application.
        student_user (Student): The user associated with the application.
        
        Returns:
        None
        """
        
        super().__init__(master)
        self.student_user = student_user
        self.mainframe = tk.Frame(master, padx=3, pady=12)
        self.mainframe.grid(column=0, row=0, sticky="nsew")


        # Load logo image
        photo_path = "./interfaces/logo.png"
        self.logo = tk.PhotoImage(file=photo_path)
        self.label = tk.Label(self.mainframe, image=self.logo, width=750, height=300)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, sticky=tk.S, pady=10)

        # Welcome heading
        self.welcome_label = tk.Label(self.mainframe, text="Welcome to EmpowerU", font=("Arial Bold", 20))
        self.welcome_label.grid(row=1, column=0, pady=10)

        # Create buttons below the welcome label
        self.lessons = tk.Button(self.mainframe, text="Lessons")
        self.lessons.grid(row=2, column=0, padx=10, pady=5)

        self.quiz = tk.Button(self.mainframe, text="Quiz")
        self.quiz.grid(row=3, column=0, padx=10, pady=5)

        self.logout = tk.Button(self.mainframe, text="Logout")
        self.logout.grid(row=4, column=0, padx=10, pady=5)

        # Button to shut down
        self.shutdown_button = tk.Button(self.mainframe, text="Shut down", command=self.master.destroy)
        self.shutdown_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        self.place(relx=.5, rely=.5, anchor=tk.CENTER)
    
    def show_student_page(self):
        """
        Shows the student page
        
        This method will show the student page on the application's
        main window. This page contains buttons to access the student's
        lessons, take a quiz, and logout.
        """
        # Place the main frame in the root window, and configure it to expand in both directions
        self.mainframe.grid(column=0, row=0, sticky="nsew")
