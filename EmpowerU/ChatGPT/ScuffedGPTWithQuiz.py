import tkinter as tk
from tkinter import messagebox

# Global user object to store the logged-in user
logged_in_user = None


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.progress = 0
        self.completed_questions = 0
        self.enrollments = []  # Track enrolled courses

    def update_progress(self, points, questions=1):
        self.progress += points
        self.completed_questions += questions

    def enroll_in_course(self, course):
        if course not in self.enrollments:
            self.enrollments.append(course)


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
        self.user_menu.add_command(label="Profile", command=self.show_profile)
        self.user_menu.add_command(label="Logout", command=self.logout)

        self.course_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Courses", menu=self.course_menu)
        self.course_menu.add_command(label="Enroll in Course", command=self.show_course_window)
        self.course_menu.add_command(label="Take Quiz", command=self.show_quiz_window)
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
                logged_in_user.enroll_in_course(course)  # Add the course to user's enrollments
                if course == "Python Programming":
                    messagebox.showinfo("Enrolled", f"You have successfully enrolled in {course}!")
                    self.show_quiz_window()  # Automatically show quiz window after enrolling in Python
                else:
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
        questions_text = f"Completed {logged_in_user.completed_questions} quiz questions."
        tk.Label(frame, text=progress_text, font=('Arial', 14)).pack()
        tk.Label(frame, text=questions_text, font=('Arial', 14)).pack()

    # Function to show quiz window
    def show_quiz_window(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to take a quiz.")
            return

        self.clear_frame()

        # Quiz Data (for demonstration)
        basic_python_questions = [
            {
                "question": "What data type is used to represent text in Python?",
                "options": ["int", "str", "list", "float"],
                "correct": "str"
            },
            {
                "question": "Which of the following is an immutable data type?",
                "options": ["list", "tuple", "set", "dict"],
                "correct": "tuple"
            },
            {
                "question": "What is the result of 2 + 2 in Python?",
                "options": ["3", "22", "4", "None"],
                "correct": "4"
            }
        ]

        advanced_python_questions = [
            {
                "question": "Which of the following is a mutable data type in Python?",
                "options": ["tuple", "list", "str", "int"],
                "correct": "list"
            },
            {
                "question": "What is the purpose of 'def' in Python?",
                "options": ["To define a variable", "To define a function", "To define a class", "To define a module"],
                "correct": "To define a function"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["class", "def", "new", "object"],
                "correct": "class"
            }
        ]

        # Choose quiz based on progress
        quiz_data = basic_python_questions if not hasattr(logged_in_user, 'completed_basic_quiz') else advanced_python_questions
        quiz_title = "Basic Python Quiz" if not hasattr(logged_in_user, 'completed_basic_quiz') else "Advanced Python Quiz"

        current_question = 0
        score = 0

        def show_question():
            nonlocal current_question
            if current_question >= len(quiz_data):
                messagebox.showinfo("Quiz Completed", f"You completed the {quiz_title}! Your score: {score}/{len(quiz_data)}")
                logged_in_user.update_progress(points=score, questions=len(quiz_data))
                if quiz_title == "Basic Python Quiz":
                    logged_in_user.completed_basic_quiz = True  # Mark the first quiz as completed
                self.show_next_step()  # Redirect to choose next step after quiz
                return

            # Clear frame for new question
            self.clear_frame()

            question_frame = tk.Frame(self)
            question_frame.pack(pady=20)

            question_data = quiz_data[current_question]
            tk.Label(question_frame, text=question_data['question'], font=('Arial', 14)).pack()

            selected_answer = tk.StringVar()

            for option in question_data['options']:
                tk.Radiobutton(question_frame, text=option, variable=selected_answer, value=option).pack(anchor=tk.W)

            def check_answer():
                nonlocal score, current_question
                if selected_answer.get() == question_data['correct']:
                    score += 1
                    messagebox.showinfo("Correct", "That's the correct answer!")
                else:
                    messagebox.showwarning("Wrong", "That's not the correct answer.")

                current_question += 1
                show_question()

            tk.Button(question_frame, text="Submit", command=check_answer).pack(pady=10)

        show_question()

    # Function to decide the next step after completing the quiz
    def show_next_step(self):
        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        if hasattr(logged_in_user, 'completed_basic_quiz'):
            tk.Label(frame, text="You can now take the Advanced Python Quiz!", font=('Arial', 14)).pack(pady=10)
        else:
            tk.Label(frame, text="Basic Python Quiz completed!", font=('Arial', 14)).pack(pady=10)

        def take_advanced_quiz():
            self.show_quiz_window()

        tk.Button(frame, text="Take Next Quiz", command=take_advanced_quiz).pack(pady=10)
        tk.Button(frame, text="View Profile", command=self.show_profile).pack(pady=10)

    # Function to show forum window
    def show_forum_window(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to post a question.")
            return

        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        tk.Label(frame, text="Ask a Question", font=('Arial', 14)).pack()

        question_entry = tk.Entry(frame, width=50)
        question_entry.pack(pady=10)

        def post_question():
            question = question_entry.get()
            if question:
                messagebox.showinfo("Posted", f"Your question: '{question}' has been posted!")
            else:
                messagebox.showwarning("Input Error", "Please enter a question.")

        tk.Button(frame, text="Post Question", command=post_question).pack(pady=10)

    # Function to show user profile
    def show_profile(self):
        if not logged_in_user:
            messagebox.showwarning("Not Logged In", "Please login to view your profile.")
            return

        self.clear_frame()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        progress_text = f"Current progress: {logged_in_user.progress} points."
        completed_text = f"Completed {logged_in_user.completed_questions} quiz questions."
        enrollments_text = f"Enrolled in: {', '.join(logged_in_user.enrollments)}"
        quiz_status = "Basic Python Quiz Completed" if hasattr(logged_in_user, 'completed_basic_quiz') else "No Quizzes Completed"

        tk.Label(frame, text="Profile", font=('Arial', 18)).pack(pady=10)
        tk.Label(frame, text=progress_text, font=('Arial', 14)).pack()
        tk.Label(frame, text=completed_text, font=('Arial', 14)).pack()
        tk.Label(frame, text=enrollments_text, font=('Arial', 14)).pack()
        tk.Label(frame, text=f"Quiz Status: {quiz_status}", font=('Arial', 14)).pack()

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
