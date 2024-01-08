from database_info import *

class karakter_mage: 
    def __init__(self,name,health,damage,armer,speed,magic_damage):
        self.name= name
        self.health= health
        self.damage= damage
        self.armer=armer
        self.speed=speed
        self.magic_damage=magic_damage

class karakter_assisin:
    def __init__(self,name,health,damage,armer,speed,stealth_damage):
        self.name= name
        self.health= health
        self.damage= damage
        self.armer=armer
        self.speed=speed
        self.stealth_damge=stealth_damage

class karakter_palladin:
    def __init__(self,name,health,damage,armer,speed,true_damage):
        self.name= name
        self.health= health
        self.damage= damage
        self.armer=armer
        self.speed=speed
        self.true_damge=true_damage

mage = karakter_mage(mage_karakter_name,mage_karakter_hp,mage_karakter_damage,mage_karakter_armer,mage_karakter_speed,mage_karakter_magic_damage)
assisin = karakter_assisin(assisin_karakter_name,assisin_karakter_hp,assisin_karakter_damage,assisin_karakter_armer,assisin_karakter_speed,assisin_karakter_stealth_damage)
paladin= karakter_palladin(paladin_karakter_name,paladin_karakter_hp,paladin_karakter_damage,paladin_karakter_armer,paladin_karakter_speed,paladin_karakter_true_damage)