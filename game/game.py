
from signal import raise_signal
import pygame
from errors import NoAgeError, NoClassError, NoLanguageError, NoNameError, NoRaceError
from dobbelstenen import rollen
import classes


# width, height = 1920, 1080
# WIN = pygame.display.set_mode((width,height)) 
# map = pygame.image.load('map.jpg')
# pygame.display.set_caption('Dungeon & Dragons')
# pygame.init()

# FPS = 60

# def draw_display():
#     pygame.image.load('map.jpg')
#     pygame.display.update()

# def main():
#     clock = pygame.time.Clock()
#     new_icon = pygame.image.load('DnD.png')
#     pygame.display.set_icon(new_icon)
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         draw_display()   
        
    
#     pygame.quit()
#     exit()



def character_selection():
    ans = input('Would you like to make a new character?\n')
    if ans == 'y' or 'yes':
        _class = input('*****************************\nWhat class would you like to play?\nWizard\nRogue\nPaladin\n')
        # Hier word de class aangemaakt en alle gegevens toegewezen.
        if _class.lower() == 'wizard':

            # Hier worden er gegevens toegewezen om je character wat vorm te geven.
            race = input(f'\n*****************************\nWhat race of {_class} would you like to be: ')
            name = input(f'\n*****************************\nTell me your name brave {race} {_class}: ')
            if name == ' ' or '':
                raise NoNameError()
            age = int(input('\n*****************************\nHow old are you: '))
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            alignment = input('\n*****************************\nWhat are your believes: ')
            language = input("\n*****************************\nWhat language do you speak: ")

            # Hier worder er default stats toegewezen.
            damage= 4 #is op 5
            armor = 2 #is op 5
            speed = 3 #is op 5
            magic_damage = 3
            lvl = 0
            exp = 0

            p1 = classes.Charachter(race, name, age, size, alignment, language, lvl, exp)

            # We verdelen de gegevens over de 2 eigenschappen omdat zo de data gemakkelijker kan worden aangepast/opgevraagd. Hierdoor blijft alles ordelijk.
            p1stats = classes. Wizard(armor ,speed, damage, magic_damage)

            print(p1.__dict__, p1stats.__dict__)

        if _class.lower() == 'rogue':
            race = input(f'\n*****************************\nWhat race of {_class} would you like to be: ')
            if race == ' ' or '':
                raise NoRaceError()
            name = input(f'\n*****************************\nTell me your name brave {race} {_class}: ')
            if name == '' or ' ':
                raise NoNameError()
            age = int(input('\n*****************************\nHow old are you: '))
            if name == '' or ' ':
                raise NoAgeError()
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            if size == '' or ' ':
                size = 'Midget'
            alignment = input('\n*****************************\nWhat are your believes: ')
            language = input("\n*****************************\nWhat language do you speak: ")
            if name == '' or ' ':
                raise NoLanguageError()

            damage= 3 #is op 5
            armor = 2 #is op 5
            speed = 5 #is op 5
            stealth = 4 #is op 5

            level = 0
            exp = 0
            p1 = classes.Charachter(race,name,age,size,alignment,language, level, exp)
            p1stats = classes.Rogue(damage,armor,speed,stealth)
            print(p1.__dict__, p1stats.__dict__)
            
        if _class.lower() == 'paladin':

            race = input('\n*****************************\nWhat race of Paladin would you like to be: ')
            if race == '' or ' ':
                raise NoRaceError() 
            
            name = input(f'\n*****************************\nTell me your name brave {race} Paladin: ')
            if name == '' or ' ':
                raise NoNameError()
            
            age = int(input('\n*****************************\nHow old are you: '))
            if age == '' or ' ':
                raise NoAgeError()
            
            size = input('\n*****************************\nWhat is you size: \nsmall\naverage\ntall\n')
            if size == ' ' or '':
                size = 'Midget'
            alignment = input('\n*****************************\nWhat are your believes: ')

            language = input("\n*****************************\nWhat language do you speak: ")
            if language == '' or ' ':
                raise NoLanguageError()
            
            damage= 2 #is op 5
            armor = 5 #is op 5
            speed = 2 #is op 5
            true_damage = 3 #is op 5

            level = 0
            exp = 0
            
            p1 = classes.Charachter(race,name,age,size,alignment,language, level, exp)
            p1stats = classes.Paladin(damage,armor,speed,true_damage)
            print(p1.__dict__, p1stats.__dict__)
        
        if _class.lower() != 'wizard' or _class.lower() != 'rogue' or _class.lower() != 'paladin':
            character_selection()
            raise NoClassError()
        
        if _class.lower() == 'no':
            print('Goodbye Hero! Until next time.')




def Dobbelen():
    # Hier rollen we de dobbelsteen aan de hand van de keuze van de gebruiker. Hij kan een dobbelsteen kiezen en hoeveel keer dat hij deze wil rollen.
    x = input('Welke dobbelsteen wilt u rollen? D6, D4, D8, D10\n')
    y = int(input('Hoeveel keer wilt u uw dobbelsteen rollen?\n'))
    # Aan het einde van de rolbeurten worden de gegevens opgetelt voor het totaal aantal damage dat hij/zij heeft ontvangen.
    w = sum(rollen(x,y))
    print(f'u heeft {w} gerolled.')


if __name__ == '__main__':
    character_selection()



