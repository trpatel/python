class Fish(object):
    school = []
    def __init__(self, name, length, caught=False):
        self.name = name
        self.length = length
        self.caught = caught
        Fish.school.append(self)
    def __str__(self):
        reply = "Fish object\n"
        reply += "Fish put in pond: " + self.name
        return reply
    def remaining():
        number = Fish.school
        print "Number of fish in the pond: ", number
        for item in Fish.school:
            print item
    remaining = staticmethod(remaining)

    def largest():
        largest = 0
        name = "non-name"
        for fish in Fish.school:
            if fish.length > largest:
                largest = fish.length
                name = fish.name
            print "The largest fish is: ", name
    largest = staticmethod(largest)
        
       
            
    
    def __cmp__(self, other):
        if self.length > other.length:
            return 1
        elif self.length == other.length:
            return 0
        else:
            return -1
    def catch(self):
        if self.caught:
            fishing = "You attempt to catch " + self.name + ". " + self.name + " was already caught!"
        else:
            fishing = "You attempt to catch " + self.name + ". SUCCESS!\n"
            fishing += "Name: " + self.name + "\n"
            fishing += "Length: " + str(self.length) + '"\n'
            fishing += "Status: CAUGHT\n"
            self.caught = True
        print fishing
class StealthFish(Fish):
    def catch(self):
        fishing = "You attempt to catch " + self.name + ". But it can't be done!"
        print fishing
class FancyFish(Fish):
    def __init__(self, title, name):
        super(FancyFish, self).__init__(name)
        self.title = title
    def catch(self):
        print "What a rude thing to do to ", self.title, self.name, "!\n"
class NiceFish(Fish):
    def release(self):
        if not self.caught:
            fishing =  "You attempt to release", self.name, ". ", self.name, "was already free!"
        else:
            fishing = "You attempt to release " + self.name + ". SUCCESS!\n"
            fishing += "Name: " + self.name + "\n"
            fishing += "Length: " + str(self.length) + '"\n'
            fishing += "Status: FREE\n"
            self.caught = False
        return fishing

    
fish1 = StealthFish("007", 11)
fish2 = FancyFish("Lord", "Grantham", 10)
fish3 = NiceFish("Nemo", 3)
fish1.catch()
fish2.catch()
fish3.catch()
fish3.release()
fish3.release()
Fish.remaining()

