import pygame
import sys
from dobbelstenen import *
from DungeonsandDragons import show_text, show_victory_message






width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('D&D Game')

# Achtergrondafbeelding van het hoofdscherm
background = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/bb.jpg')


# Kleuren en lettertype
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
font = pygame.font.Font(None, 36)

# Lettertype
font = pygame.font.Font(None, 36)


# Het scherm dat word weergeven voor als je de battle bent verloren.
def show_you_died_screen(screen, font):
    global game_state  # Voeg deze regel toe

    died_background = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/you_died.png')
    died_background = pygame.transform.scale(died_background, (800, 500))
    screen.blit(died_background, (0, 0))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                waiting = False
                game_state = "main_menu"  # Reset de game state
                return


def battle(screen, font, player_health, monster_health, player_action):
    if player_action == "attack":
        # Speler valt aan
        monster_damage = sum(rollen('d4', 1))
        monster_health -= monster_damage
        print(f"Speler doet {monster_damage} schade aan het monster.")
    elif player_action == "heal":
        # Speler geneest
        if player_health in range(1,15):
            player_health+=3
            print(f"Speler geneest, huidige gezondheid: {player_health}.")
        else:
            player_health = player_health
        
    # Monster aanvalsbeurt
    if monster_health > 0:
        player_damage = sum(rollen('d4', 1))
        player_health -= player_damage
        print(f"Monster doet {player_damage} schade aan de speler.")

    return player_health, monster_health



# De funtie voor het weergeve van het gevechtscherm met alle bijhorende assets.
def show_battle_screen(screen, font, player_health, monster_health, background_image):
    # Functie voor het tonen van het gevechtsscherm met achtergrond dat kan veranderen
    battle_background = pygame.image.load(background_image)
    battle_background = pygame.transform.scale(battle_background, (800, 500))

    attack_button = pygame.Rect(50, 400, 100, 50)
    heal_button = pygame.Rect(200, 400, 100, 50)

    screen.blit(battle_background, (0, 0))
    pygame.display.update()

    running = True
    while running and player_health > 0 and monster_health > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if attack_button.collidepoint(event.pos):
                    player_health, monster_health = battle(screen, font, player_health, monster_health, "attack")
                elif heal_button.collidepoint(event.pos):
                    player_health, monster_health = battle(screen, font, player_health, monster_health, "heal")

        screen.blit(battle_background, (0, 0))
        show_text(screen, f"Player HP: {player_health}", (50, 450), font, green)
        show_text(screen, f"Monster HP: {monster_health}", (600, 50), font, red)
        pygame.draw.rect(screen, white, attack_button)
        pygame.draw.rect(screen, white, heal_button)
        show_text(screen, "Attack", (60, 410), font, black)
        show_text(screen, "Heal", (210, 410), font, black)

        pygame.display.update()

        if player_health <= 0:
            return show_you_died_screen(screen, font)
        elif monster_health <= 0:
            show_victory_message(screen, font)
            return "select_start_position"

    return "main_menu"
