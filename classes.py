class Charachter:
    def __init__(self, race, _class, age, alignment, size, language, level=0):
        self.race = race
        self._class = _class
        self.age = age 
        self.alignment = alignment
        self.size = size
        self.language = language
        self.__level = level
        


class Wizard(Charachter):
    def __init__(self, armor, speed, defence, damage):
        self.__speed = speed
        self.__armor = armor
        self.__damage = damage
        self.__defence = defence

        @property
        def pspeed(self):
            return self.__speed

        @pspeed.setter
        def pspeed(self):
            if self.__level +1:
                self.__speed +=1
                return self.__speed

        @property
        def parmor(self):
            return self.__armor
        
        @parmor.setter
        def parmor(self):
            if self.__level +1:
                self.__speed +=1
                return self.__speed
        
        @property
        def pdamage(self):
            return self.__damage
        
        
        @pdamage.setter
        def pdamage(self):
            if self.__level +1:
                self.__armor +=1
                return self.__armor

        
        @property
        def pdefence(self):
            return self.__defence
        
        @pdefence.setter
        def pdefence(self):
            if self.__level +1:
                self.__defence +=1
                return self.__defence

        
class Rogue(Charachter):
    def __init__(self, armor, speed, stealth, damage, defence):
        self.__armor = armor 
        self.__speed = speed 
        self.__stealth = stealth
        self.__damage = damage
        self.__defence = defence

    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self):
        if self.__level +1:
            self.__armor +=1
            return self.__armor
    
    @property
    def defence(self):
        return self.__defence
    
    @defence.setter
    def defence(self):
        if self.__level +1:
            self.__defence +=1
            return  self.__defence
    
    @property
    def speed(self):
        return self.__speed

    @property
    def stealth(self):
        return self.__stealth
    
    @property
    def damage(self):
        return self.__damage
    
class Paladin(Charachter):
    def __init__(self, true_damage, armor, speed, defence):
        self.__true_damage = true_damage
        self.__armor = armor
        self.__speed = speed
        self.__defence = defence

    @property
    def true_damage(self):
        return self.__true_damage
    
    @property
    def armor(self):
        return self.__armor
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def defence(self):
        return self.__defence