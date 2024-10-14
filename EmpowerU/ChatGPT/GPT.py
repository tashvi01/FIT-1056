import tkinter as tk
from tkinter import messagebox

# Global user object to store the logged-in user
logged_in_user = None


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.progress = 0

    def update_progress(self, points):
        self.progress += points


# Tkinter App class
class EmpowerUApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EmpowerU Learning Platform")
        self.geometry("600x400")
        self.resizable(False, False)

        # Create a menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.user_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="User", menu=self.user_menu)
        self.user_menu.add_command(label="Register/Login", command=self.show_login_window)
        self.user_menu.add_command(label="Logout", command=self.logout)

        self.course_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Courses", menu=self.course_menu)
        self.course_menu.add_command(label="Enroll in Course", command=self.show_course_window)
        self.course_menu.add_command(label="View Progress", command=self.show_progress)

        self.forum_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Forum", menu=self.forum_menu)
        self.forum_menu.add_command(label="Ask Question", command=self.show_forum_window)

        self.show_login_window()

    # Function to display the login/registration window
    def show_login_window(self):
        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        tk.Label(frame, text="Email:").grid(row=0, column=0, padx=10, pady=10)
        email_entry = tk.Entry(frame)
        email_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        def login():
            global logged_in_user
            email = email_entry.get()
            password = password_entry.get()
            if email and password:
                logged_in_user = User(email, password)  # Simplified user creation for demo
                messagebox.showinfo("Login Success", f"Welcome {email}")
                self.show_course_window()
            else:
                messagebox.showwarning("Input Error", "Please enter email and password.")

        tk.Button(frame, text="Login/Register", command=login).grid(row=2, column=1, pady=20)

    # Function to show course enrollment window
    def show_course_window(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to enroll in courses.")
            return

        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        tk.Label(frame, text="Available Courses", font=('Arial', 14)).pack()

        courses = ["Python Programming", "Information Security", "Artificial Intelligence"]
        selected_course = tk.StringVar()

        for course in courses:
            tk.Radiobutton(frame, text=course, variable=selected_course, value=course).pack(anchor=tk.W)

        def enroll_in_course():
            course = selected_course.get()
            if course:
                messagebox.showinfo("Enrolled", f"You have successfully enrolled in {course}!")
            else:
                messagebox.showwarning("No Selection", "Please select a course to enroll.")

        tk.Button(frame, text="Enroll", command=enroll_in_course).pack(pady=10)

    # Function to show user progress
    def show_progress(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to view progress.")
            return

        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        progress_text = f"Your current progress: {logged_in_user.progress} points."
        tk.Label(frame, text=progress_text, font=('Arial', 14)).pack()

        def add_points():
            logged_in_user.update_progress(10)
            messagebox.showinfo("Progress Updated", "10 points added to your progress!")
            self.show_progress()

        tk.Button(frame, text="Complete Quiz (Add 10 points)", command=add_points).pack(pady=10)

    # Function to show forum window
    def show_forum_window(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to ask questions.")
            return

        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        tk.Label(frame, text="Forum - Ask a Question", font=('Arial', 14)).pack()

        question_entry = tk.Entry(frame, width=50)
        question_entry.pack(pady=10)

        def post_question():
            question = question_entry.get()
            if question:
                messagebox.showinfo("Posted", f"Your question: '{question}' has been posted!")
            else:
                messagebox.showwarning("Input Error", "Please enter a question.")

        tk.Button(frame, text="Post Question", command=post_question).pack(pady=10)

    # Function to clear current frame contents
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Function to log out
    def logout(self):
        global logged_in_user
        logged_in_user = None
        messagebox.showinfo("Logout", "You have been logged out.")
        self.show_login_window()


# Running the Tkinter application
if __name__ == "__main__":
    app = EmpowerUApp()
    app.mainloop()
