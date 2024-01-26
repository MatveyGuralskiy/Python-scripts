        #Classes
    #Super Class(parent class)
class UNITS():
    """Class to create unit"""
    def __init__(self,name,race,level,magic,health):
        """Parameters for units"""
        self.name=name
        self.race=race
        self.level=1
        self.magic=100
        self.health=10
    
    
    def SHOW_UNITS(self):
        """How you actually gonna see the unit"""
        DISCRIPTION=("Unit: "+self.name+"\t race: "+self.race+"\t level: "+str(self.level)+"\t magic: "+str(self.magic)+"\t health: "+str(self.health)).title()
        print(DISCRIPTION)


    def LEVEL_UP(self):
        """Upgrade level of unit"""
        self.level+=1
        print("Congratilations!You're achieve new level: "+str(self.level))


    def MOVE(self):
        """Start moving unit"""
        print("Unit "+self.name+" moving now...")


    def HP_LOW(self):
        """Check your HP status"""
        if self.health <= 30:
            print("PLEASE CHECK YOUR HEALTH POINT: "+str(self.health))
            return 0
        else:
            print("You're HP status is normal")

    def HIT(self):
        """Hit your unit+status health point"""
        self.health -= 5
        print("You're got hit\nPlease check you're HP: "+str(self.health))


    def SET_HP(self,NEW_HEALTH):
        """Set how many HP you want"""
        self.health=NEW_HEALTH
        

    def DEAD(self):
        """Dead status"""
        if self.health <= 0:
            print("You're unit is dead")


    def MAKE_MAGIC(self):
        """Use magic"""
        self.magic-=10
        print("Checkout your magic points: "+str(self.magic))


        #Class child
class HERO(UNITS):
    """Class to create a hero"""
    def __init__(self,name,race,level,health,magic,magiclevel,color):
        """Initiate our hero"""
        super().__init__(name,race,level,health,magic)
        self.magiclevel=1
        self.color=color
    

    def SHOW_UNITS(self):
        """How you actually gonna see the unit"""
        DISCRIPTION=("Unit: "+self.name+"\t race: "+self.race+"\t level: "+str(self.level)+"\t magic: "+
                     str(self.magic)+"\t health: "+str(self.health)+"\t magic level: "+str(self.magiclevel)).title()
        print(DISCRIPTION)

