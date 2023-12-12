from xml.sax.handler import property_encoding


class Charachter:
    def __init__(self, race, _class, age, alignment, size, language):
        self.race = race
        self._class = _class
        self.age = age 
        self.alignment = alignment
        self.size = size
        self.language = language


class Wizard(Charachter):
    def __init__(self, armor, speed, damage, magic_damage):
        self.__speed = speed
        self.__armor = armor
        self.__damage = damage
        self.__magic_damage = magic_damage

    @property
    def speed(self):
        return self.__speed
    
    @property
    def armor(self):
        return self.__armor
    
    @property 
    def damage(self):
        return self.__damage
class Rogue(Charachter):
    def __init__(self, armor, speed, damage, stealth):
        self.__armor = armor 
        self.__speed = speed 
        self.__damage = damage
        self.__stealth = stealth

    @property
    def armor(self):
        return self.__armor
    
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
    def __init__(self, armor, speed, damage, true_damage):
        self.__armor = armor
        self.__speed = speed
        self.__damage = damage
        self.__true_damage = true_damage

    
    @property
    def armor(self):
        return self.__armor
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def damage(self):
        return self.__damage
    
    @property
    def true_damage(self):
        return self.__true_damage

        

    
    