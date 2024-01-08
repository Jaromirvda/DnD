
from database_info import *

class monster_tier1:
    def __init__(self,name,health,damage,armer,speed):
        self.name=name
        self.health=health
        self.damage=damage
        self.armer=armer
        self.speed=speed


class monster_tier2:
    def __init__(self,name,health,damage,armer,speed):
        self.name=name
        self.health=health
        self.damage=damage
        self.armer=armer
        self.speed=speed

class boss:
    def __init__(self,name,health,damage,armer,speed):
        self.name=name
        self.health=health
        self.damage=damage
        self.armer=armer
        self.speed=speed


monster1 = monster_tier1(tier1_monster1_name,tier1_monster1_hp,tier1_monster1_damage,tier1_monster1_armer,tier1_monster1_speed)
monster2 = monster_tier1(tier1_monster2_name,tier1_monster2_hp,tier1_monster2_damage,tier1_monster2_armer,tier1_monster2_speed)
monster3 = monster_tier1(tier1_monster3_name,tier1_monster3_hp,tier1_monster3_damage,tier1_monster3_armer,tier1_monster3_speed)

monster4 = monster_tier2(tier2_monster1_name,tier2_monster1_hp,tier2_monster1_damage,tier2_monster1_armer,tier2_monster1_speed)
monster5 = monster_tier2(tier2_monster2_name,tier2_monster2_hp,tier2_monster2_damage,tier2_monster2_armer,tier2_monster2_speed)
monster6 = monster_tier2(tier2_monster3_name,tier2_monster3_hp,tier2_monster3_damage,tier2_monster3_armer,tier2_monster3_speed)

boss1 = boss(boss1_name,boss1_hp,boss1_damage,boss1_armer,boss1_speed)
boss2 = boss(boss2_name,boss2_hp,boss2_damage,boss2_armer,boss2_speed)
boss3 = boss(boss3_name,boss3_hp,boss3_damage,boss3_armer,boss3_speed)

