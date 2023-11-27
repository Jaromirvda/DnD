from os import error
from dobbelstenen import rollen
import classes

def character_selection():
    ans = input('Would you like to make a new character?\n')
    if ans == 'y' or 'yes':
        _class = input('*****************************\nWhat class would you like to play?\nWizard\nRogue\nPaladin\n')
        # Hier word de class aangemaakt en alle gegevens toegewezen.
        if _class.lower() == 'wizard':
            race = input(f'\n*****************************\nWhat race of {_class} would you like to be: ')
            name = input(f'\n*****************************\nTell me your brave {race} {_class}: ')
            age = int(input('\n*****************************\nHow old are you: '))
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            alignment = input('\n*****************************\nWhat are your believes: ')
            language = input("\n*****************************\nWhat language do you speak: ")
            damage= 4 #is op 5
            armor = 2 #is op 5
            speed = 3 #is op 5
            defence = 3 #is op 5

            p1 = classes.Charachter(race, name, age, size, alignment, language)
            # We verdelen de gegevens over de 2 eigenschappen omdat zo de data gemakkelijker kan worden aangepast/opgevraagd. Hierdoor blijft alles ordelijk.
            p1stats = classes. Wizard(armor ,speed, damage, defence)
            print(p1.__dict__, p1stats.__dict__)

        if _class.lower() == 'rogue':
            race = input(f'\n*****************************\nWhat race of {_class} would you like to be: ')
            name = input(f'\n*****************************\nTell me your brave {race} {_class}: ')
            age = int(input('\n*****************************\nHow old are you: '))
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            alignment = input('\n*****************************\nWhat are your believes: ')
            language = input("\n*****************************\nWhat language do you speak: ")
            damage= 3 #is op 5
            armor = 2 #is op 5
            speed = 5 #is op 5
            defence = 2 #is op 5
            stealth = 4 #is op 5
            p1 = classes.Charachter(race,name,age,size,alignment,language)
            p1stats = classes.Rogue(damage,armor,speed,defence,stealth)
            print(p1.__dict__, p1stats.__dict__)
            
        if _class.lower() == 'paladin':
            race = input('\n*****************************\nWhat race of Paladin would you like to be: ')
            name = input(f'\n*****************************\nTell me your brave {race} Paladin: ')
            age = int(input('\n*****************************\nHow old are you: '))
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            alignment = input('\n*****************************\nWhat are your believes: ')
            language = input("\n*****************************\nWhat language do you speak: ")
            damage= 2 #is op 5
            armor = 5 #is op 5
            speed = 2 #is op 5
            defence = 4 #is op 5
            
            p1 = classes.Charachter(race,name,age,size,alignment,language)
            p1stats = classes.Paladin(damage,armor,speed,defence)
            print(p1.__dict__, p1stats.__dict__)
        
        if _class.lower() != 'wizard' or _class.lower() != 'rogue' or _class.lower() != 'paladin':
            raise error(f'{_class} not found please enter a correct class')
            character_selection()




def Dobbelen():
    # Hier rollen we de dobbelsteen aan de hand van de keuze van de gebruiker. Hij kan een dobbelsteen kiezen en hoeveel keer dat hij deze wil rollen.
    x = input('Welke dobbelsteen wilt u rollen? D6, D4, D8, D10\n')
    y = int(input('Hoeveel keer wilt u uw dobbelsteen rollen?\n'))
    z = input('Gaat u damage doen of ontvangen?\n')
    # Aan het einde van de rolbeurten worden de gegevens opgetelt voor het totaal aantal damage dat hij/zij heeft ontvangen.
    w = sum(rollen(x,y,z))
    print(f'u heeft {w} gerolled.')


if __name__ == '__main__':
    character_selection()