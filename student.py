from Tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.lbl = Label(self, text="Enter student homework information.")
        self.lbl.grid(row=0, column=0,columnspan=4, sticky= N)
        self.lblname = Label(self, text="Student Name:")
        self.lblname.grid(row=1, column=0,columnspan=1, sticky= W)
        self.txt_ent = Entry(self, width = 40)
        self.txt_ent.grid(row=1, column=1, columnspan=3, stick=W)
        self.lblassignment = Label(self, text="Assignment:")
        self.lblassignment.grid(row=2, column=0,columnspan=1, sticky= W)
        self.txtas_ent = Entry(self, width = 40)
        self.txtas_ent.grid(row=2, column=1, columnspan=3, stick=W)
        self.lblgrade = Label(self, text="Grade:")
        self.lblgrade.grid(row=3, column=0,columnspan=1, sticky= W)
        self.favorite = StringVar()
        self.favorite.set(None)
        self.rdo1 = Radiobutton(self, text="A", variable=self.favorite, value="A").grid(row=3, column=1,columnspan=1, sticky= W)
        self.rdo2 = Radiobutton(self, text="B", variable=self.favorite, value="B").grid(row=3, column=2,columnspan=1, sticky= W)
        self.rdo3 = Radiobutton(self, text="F", variable=self.favorite, value="F").grid(row=3, column=3,columnspan=1, sticky= W)
        self.lblwork = Label(self, text="Work:")
        self.lblwork.grid(row=4, column=0, columnspan=1, sticky=W)
        self.txtwork = Text(self, width=50, height = 10, wrap=WORD)
        self.txtwork.grid(row=5, column=0, columnspan=4, sticky=W)
        self.txtprint = Text(self, width=50, height = 10, wrap=WORD)
        self.txtprint.grid(row=6, column=0, columnspan=4, sticky=W)
        self.bttn1 = Button(self, text="Save")
        self.bttn1.grid(row=7, column=0, columnspan=1, sticky=E)
        self.bttn1["command"] = self.update_info
        self.bttn2 = Button(self, text="Clear")
        self.bttn2.grid(row=7, column=2, columnspan=1, sticky=W)
        self.bttn2["command"] = self.clear_info
    def clear_info(self):
        self.txtwork.delete(0.0, END)
        self.txtprint.delete(0.0, END)
        self.txtas_ent.delete(0, END)
        self.txt_ent.delete(0, END)
        self.favorite.set(None)
    def update_info(self):
        info = "Name: " + str(self.txt_ent.get())+ "\n"
        info += "Assignment: "+ str(self.txtas_ent.get())+ "\n"
        info += "Grade: "+ str(self.favorite.get())+ "\n"
        info += "Work: " + str(self.txtwork.get(0.0, END))
        self.txtprint.insert(INSERT, info)
    
        

root =Tk()
root.title("Student Homework")
root.geometry("430x470")
app = Application(root)
root.mainloop()
