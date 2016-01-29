#Tej Patel
#2:30-4:25 Thursday

from Tkinter import *

#sunglass program
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    #main screen visible for user
    def create_widgets(self):
        #gives the top caption for user to see what this is about
        self.label = Label(self, text="Choose sunglasses, then click 'Add Order' to save to file.")
        self.label.grid(row=1, column=0, columnspan=4, sticky=N)
        self.lblBrand = Label(self, text="Brand name:")
        self.lblBrand.grid(row=2, column=0, columnspan=1, sticky=E)
        #space to enter brand name
        self.txtBrand = Entry(self, width=40)
        self.txtBrand.grid(row=2, column=1, columnspan=1, sticky=W)
        #set up the radio and check buttons
        self.like_color = StringVar()
        self.like_color.set(None)
        self.like_anti = BooleanVar()
        #various buttons for the user to select
        self.coat1 = Checkbutton(self, text="Anti-reflective Coating", variable=self.like_anti).grid(row=3, column=1, columnspan=1, sticky=W)
        self.tint1 = Radiobutton(self, text="Dark Gray", variable=self.like_color, value="dark gray").grid(row=3, column=2, columnspan=1, sticky=W)
        self.like_polar = BooleanVar()
        self.coat2 = Checkbutton(self, text="Polarized Filter", variable=self.like_polar).grid(row=4, column=1, columnspan=1, sticky=W)
        self.tint2 = Radiobutton(self, text="Teal", variable=self.like_color, value="teal").grid(row=4, column=2, columnspan=1, sticky=W)
        self.lblCoat = Label(self, text="Coating(s):")
        self.lblCoat.grid(row=5, column=0, columnspan=1, sticky=E)
        self.like_resis = BooleanVar()
        self.coat3 = Checkbutton(self, text="Scratch Resistant", variable=self.like_resis).grid(row=5, column=1, columnspan=1, sticky=W)
        self.tint3 = Radiobutton(self, text="Amber", variable=self.like_color, value="amber").grid(row=5, column=2, columnspan=1, sticky=W)
        #indicates the tint color options 
        self.lblTint = Label(self, text="Tint Color:")
        self.lblTint.grid(row=5, column=1, columnspan=1, sticky=E)
        self.like_mirror = BooleanVar()
        self.coat4 = Checkbutton(self, text="Mirror Coating", variable=self.like_mirror).grid(row=6, column=1, columnspan=1, sticky=W)
        self.tint4 = Radiobutton(self, text="Green", variable=self.like_color, value="green").grid(row=6, column=2, columnspan=1, sticky=W)
        #the textbox which will print out the features of the sunglass(s)
        self.txtprint = Text(self, width=46, height=10, wrap=WORD)
        self.txtprint.grid(row=7, column=0, columnspan=4, sticky=N)
        #adds the specified glass
        self.bttn1 = Button(self, text="Add Order")
        self.bttn1.grid(row=8, column=1, columnspan=1, sticky=W)
        self.bttn1["command"] = self.add_order
        #deletes all the content within the textbox
        self.bttn2 = Button(self, text="Clear Inputs")
        self.bttn2.grid(row=8, column=2, columnspan=2, sticky=N)
        self.bttn2["command"] = self.clear_info
    #deletes the contents within textbox and resets all the previously chosen buttons/names
    def clear_info(self):
        self.txtBrand.delete(0, END)
        self.txtprint.delete(0.0, END)
        self.like_color.set(None)
        self.like_anti.set(None)
        self.like_polar.set(None)
        self.like_resis.set(None)
        self.like_mirror.set(None)
    #adds the properties of the chosen sunglass    
    def add_order(self):
        #checks to see if user entered a brand name
        if str(self.txtBrand.get()) == "":
            info = "Brand name: Unspecified\n"
        else:
            info = "Brand name: " + str(self.txtBrand.get()) + "\n"
        likes = ""
        #checks to see which coatings the user wants
        if self.like_anti.get():
            likes += "add anti-reflective coating, "
        if self.like_polar.get():
            likes += "add polarized filter, "
        if self.like_resis.get():
            likes += "add scratch resistant, "
        if self.like_mirror.get():
            likes += "add mirror coating, "
        info += "Coatings: " + likes + "\n"
        #indicates the color the user wants
        info += "Tint color: " + str(self.like_color.get()) + "\n"
        info += "-" * 25 + "\n"
        info += "has been saved to file.\n"
        #enters all the information into the textbox
        self.txtprint.insert(0.0, info)
        #opens a file and attempts to write to it
        text_file = open("sunglasses.txt", "w")
        #initiates the file and enters all the content from the textbox into the file
        text_file.writelines(self.txtprint.get(0.0, END))
        
    



#main
root = Tk()
root.title("Sunglasses Order")
root.geometry("430x470")
app = Application(root)
root.mainloop()
