class Television(object):
    def __init__(self, __channel, volume, is_on):
        self.__channel = __channel
        self.volume = volume
        self.is_on = is_on
    def __str__(self):
        reply = "\tTelevision object\n"
        if self.is_on == "on":
            reply += "-" * 30 + "\n"
            reply += "|  The television is: " + self.is_on + "     |\n"
            reply += "|  The current channel is: " + str(self.__channel) + " |\n"
            reply += "|  The volume level is: " + str(self.volume) + "    |\n"
            reply += "-" * 30 + "\n"
        else:
            reply += "The television is: " + self.is_on + "\n"
        return reply
    def toggle_power(self):
        if self.is_on == "on":
            self.is_on = "off"
            print "The television is now", self.is_on
        else:
            self.is_on = "on"
            print "The television is now", self.is_on
    def get_channel(self):
        self.__channel = channel
        return channel
    def set_channel(self):
        if self.is_on == "on":
            new_channel = int(raw_input("What channel do you want to watch?: "))
            while new_channel < 0 or new_channel > 499:
                new_channel = int(raw_input("You don't have that channel, what channel do you want to watch?: "))
            self.__channel = new_channel
        else:
            print "The television is currently off."
    def raise_volume(self):
        if self.is_on == "on":
            if self.volume < 10:
                self.volume += 1
                print "The volume is now at", self.volume
            else:
                print "The volume is already at the maximum."
        else:
            print "The television is currently off."
    def lower_volume(self):
        if self.is_on == "on":
            if self.volume > 0:
                self.volume -= 1
                print "The volume is now at", self.volume
            else:
                print "The volume is already at the minimum."
        else:
            print "The television is currently off."
    @property
    def channel(self):
        return get_channel()

def main():
    tv1 = Television(4, 4, "on")
    choice = None
    while choice != "0":
        
        print tv1
        print \
        """
        Television

        0 - Exit
        1 - Toggle Power
        2 - Change Channel
        3 - Raise Volume
        4 - Lower Volume
        """
        choice = raw_input("Choice: ")
        print

        if choice == "0":
            print "The television is turned off."
        elif choice == "1":
            tv1.toggle_power()
        elif choice == "2":
            tv1.set_channel()
        elif choice == "3":
            tv1.raise_volume()
        elif choice == "4":
            tv1.lower_volume()
        else:
            print "\nSorry, but", choice, "isn't a valid choice."

main()
