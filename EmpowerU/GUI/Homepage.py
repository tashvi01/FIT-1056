"""
The homepage of EmpowerU 

"""

import tkinter as tk

class Homepage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.fullscreen(master)
        
        
        
        #background colour learnt from https://www.geeksforgeeks.org/tkinter-colors/
        self.config(bg="lightblue")
        
        self.logo = tk.PhotoImage(file="logo.png")

        self.top_bar = tk.Frame(self.master, bg="steelblue")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        self.grid_rowconfigure(0, weight=0)  # Keep the top bar fixed height
        
        self.grid_columnconfigure(0, weight=1) #allows column 0 to exapnd horizontally

        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_label = tk.Label(self.top_bar, text="HOME", bg="steelblue",font = "Impact 20")
        self.home_label.grid(row=0,column=0,padx=20,pady=20)


        #TODO: progress bar
        self.progressbar_filler = tk.Label(self.top_bar,text = "PROGRESS BAR PLACEHOLDER",font = "Impact 20")
        self.progressbar_filler.grid(row=0,column=1,padx=20,pady=20)

        self.profile_button = tk.Button(self.top_bar,text="PROFILE",font = "Impact 20")
        self.profile_button.grid(row=0,column=2,padx=20,pady=20)

        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)

        self.bot_screen = tk.Frame(self.master, bg = "lightblue")
        self.bot_screen.grid(row=1,column=0,columnspan=3,sticky="nsew")

        for i in [0,1]:
            self.bot_screen.grid_rowconfigure(i, weight=1)

        for i in [0,1,2]:
            self.bot_screen.grid_columnconfigure(i, weight=1)
        


    
        



    

    






    def fullscreen(self,master):

        #fullscreen needs master parameter because of tk.Frame doesn't have geometry() method 
        # Fullscreen information learnt from geeksforgeeks.org 1/10/2024: https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/

        #obtaining width and height of screen
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        #makes window match screen geometry
        #geometry() method called with master (tk.Tk instance) instead of self which is the frame
        master.geometry(f"{width}x{height}")
        

if __name__ == "__main__":
    root = tk.Tk()  
    
    #create homepage
    homepage = Homepage(root)
    homepage.grid(row = 0, column = 0, sticky="nsew")

    #allows rows and columns to expand and contract when window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    homepage.mainloop()
