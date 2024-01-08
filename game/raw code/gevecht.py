from dobbelstenen import *
import time
def DobbelenSpeler():
            ans = input('Would you like to attack or to heal?')
            if ans.lower() == 'attack':    
                # Hier rollen we de dobbelsteen aan de hand van de keuze van de gebruiker. Hij kan een dobbelsteen kiezen en hoeveel keer dat hij deze wil rollen.
                x = 'd4'
                y = 1
                # Aan het einde van de rolbeurten worden de gegevens opgetelt voor het totaal aantal damage dat hij/zij heeft gegeven/ontvangen.
                w = sum(rollen(x,y))
                print(f'u heeft {w} gerolled.')
                return w
            else:
                 return +3
            
def DobbelenMonster():
                x = 'd4'
                y = 1
                # Aan het einde van de rolbeurten worden de gegevens opgetelt voor het totaal aantal damage dat hij/zij heeft gegeven/ontvangen.
                w = sum(rollen(x,y))
                print(f'u heeft {w} gerolled.')
                return w
# Functie voor gevechtsscène tussen speler en monster
def battle(player_hp, monster_hp):
    while player_hp > 0 and monster_hp > 0:

        print(f"********** HEROES TURN ***********")
        player_damage = DobbelenSpeler()
        if player_damage == +3:
             player_hp +=3
             print(f'your current hp is {player_hp}')
             time.sleep(2)
        else:
            monster_hp -= player_damage
            print(f'the current hp of the enemy is {monster_hp}')
            time.sleep(2)

        
        if monster_hp <= 0:
                    print("Monster verslagen!")
                    break


        print(f"********** MONSTERS TURN ***********")        
        monster_damage = DobbelenMonster()        
        player_hp -= monster_damage
        print(f'the current hp of the enemy is {player_hp}')
        time.sleep(2)
        

        if player_hp <= 0:
            print("Je hebt het gevecht verloren.")
            break



player_health = 10 
monster_health = 15

battle(player_health, monster_health)