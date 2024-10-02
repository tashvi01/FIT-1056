"""
The homepage of EmpowerU 

"""

import tkinter as tk

class Homepage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.fullscreen(master)
        
        self.mainframe = tk.Frame(self.master,bg="lightblue")
        self.mainframe.grid(row=0,column=0,sticky="nsew")
        
        #background colour learnt from https://www.geeksforgeeks.org/tkinter-colors/
        self.config(bg="lightblue")
        
        #BOTTOM HALF OF SCREEN
        # self.bot_screen = tk.Frame(self.master, bg = "lightblue")
        # self.bot_screen.grid(row=0,column=0,sticky="sew")

        # # Configure rows and columns for even distribution
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(1, weight=1)  
        self.mainframe.grid_rowconfigure(2, weight=1)

        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=1)  
        self.mainframe.grid_columnconfigure(2, weight=1)
            

        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.mainframe,image=self.logo)
        self.logo_label.grid(row = 1, column=2,sticky="e")
        

        self.top_bar = tk.Frame(self.master, bg="steelblue")  # Specify the background color and height
        self.top_bar.grid(row=0, column=0, sticky="new")  # Place it in the first row and expand it east-west

        
        #TOP BAR
        #Home label
        # fotnsize https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
        self.home_label = tk.Label(self.top_bar, text="HOME", bg="steelblue",font = "Impact 20")
        self.home_label.grid(row=0,column=0,padx=20,pady=20)

        #Progress bar
        #TODO: progress bar
        self.progressbar_filler = tk.Label(self.top_bar,text = "PROGRESS BAR PLACEHOLDER",font = "Impact 20", bg="steelblue")
        self.progressbar_filler.grid(row=0,column=1,padx=20,pady=20)

        self.profile_button = tk.Button(self.top_bar,text="PROFILE",font = "Impact 20", bg="mediumspringgreen")
        self.profile_button.grid(row=0,column=2,padx=20,pady=20)

        #configures the columns for the top bar
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)


        


    
        



    

    






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
