from Tkinter import *

class Animal(object):
    animals = []
    closed = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.boredom = 0
        self.hunger = 0
        self.visible = True
        Animal.animals.append(self)

    def __str__(self):
        warning = 3
        bad = 5
        reply = self.species + " Name: " + self.name + "\n"
        
        status = ""
        if self.boredom >= bad:
            status += "BORED "
        elif self.boredom >= warning:
            status += "Somewhat Bored "
            
        if self.hunger >= bad:
            status += "HUNGRY "
        elif self.hunger >= warning:
            status += "Somewhat Hungry "

        if self.hunger < warning and self.boredom < warning:
            status += "Fine"

        return reply + "Status: " + status + "\n\n"
    
    def pace(self):
        for i in animals:
            if i.name != Application.interact_ent.get()
                if self.visible:
                    self.boredom += 1
                    self.hunger += 1

                    if self.boredom == 5 or self.hunger == 5:
                        Animal.closed += 1
                        self.visible = False
    


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.instructions = Label(self, text="Add animals on the left, or interact with them on the right")
        self.instructions.grid(row = 0, column = 0, columnspan = 5)
        
        Label(self, text="Name:").grid(row = 1, column = 0)
        self.name_ent = Entry(self, width=30)
        self.name_ent.grid(row = 1, column = 1)

        Label(self, text="Species:").grid(row = 2, column = 0)
        self.species_ent = Entry(self, width=30)
        self.species_ent.grid(row = 2, column = 1)
        
        self.make_bttn = Button(self, text = "Add Animal")
        self.make_bttn.grid(row = 3, column = 0, columnspan = 2)
        self.make_bttn.config(command = self.add_animal)

        self.closed_lbl = Label(self, text="Closed Exhibits: 0 / 2")
        self.closed_lbl.grid(row = 4, column = 0, columnspan = 5)

        self.display = Text(self, width = 50, height = 15, wrap = WORD)
        self.display.grid(row = 1, column = 2, rowspan = 3)

        Label(self, text="Name:").grid(row = 1, column = 3)
        self.interact_ent = Entry(self, width=30)
        self.interact_ent.grid(row = 1, column = 4)
        
        self.make_bttn = Button(self, text = "Feed Animal")
        self.make_bttn.grid(row = 2, column = 3, columnspan = 2)
        self.make_bttn.config(command = self.feed_animal)
        
        self.make_bttn = Button(self, text = "Entertain Animal")
        self.make_bttn.grid(row = 3, column = 3, columnspan = 2)
        self.make_bttn.config(command = self.ent_animal)

    def add_animal(self):
        species = self.species_ent.get()
        self.species_ent.delete(0,END)
        if species == "":
            species = "Unknown Species"
        self.species = species
        name = self.name_ent.get()
        self.name_ent.delete(0,END)
        if name == "":
            name = "Unnamed Animal"
        self.name = name
        self.boredom = 0
        self.hunger = 0
        self.visible = True
        self.display.insert(0.0, self)
        Animal.animals.append(self)

    def __str__(self):
        resp = self.species + " Name: " + self.name + "\n"
        if self.hunger == 3 or self.hunger == 4:
            hunger = "Somewhat Hungry"
        if self.hunger > 4:
            hunger = "HUNGRY"
        if self.boredom ==3 or self.boredom == 4:
            bored = "Somewhat Bored"
        if self.boredom > 4:
            bored = "BORED"
        if self.hunger < 3 and self.boredom < 3:
            resp += "Status: Fine" + "\n" + "\n"
            return resp
        resp += "Status: "+ hunger + " " + bored + "\n" + "\n"
        return resp

    def feed_animal(self):
        name = self.interact_ent.get()
        info = "You put food out for " + name + "\nAll of the other animals pace in their enclosure.\n"
        self.display.insert(0.0, info)
        Animal.pace

    def ent_animal(self):
        name = self.interact_ent.get()
        info = "You try to entertain " + name + "\nAll of the other animals pace in their enclosure.\n"
        self.display.insert(0.0, info)
        print "fun"

# main
root = Tk()
root.title("Animal Manager GUI")
root.geometry("1000x300")

app = Application(root)
root.mainloop()
