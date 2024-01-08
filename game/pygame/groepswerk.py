import pygame
import sys
import random
import time
# Initialisatie van Pygame
pygame.init()

# Scherm instellingen
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('D&D Game')

# Achtergrondafbeelding van het hoofdscherm
background = pygame.image.load('C:/Users/mounir/dend game/assets/bb.jpg')

# Kleuren
# Globale kleurdefinities
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Lettertype
font = pygame.font.Font(None, 36)



def show_you_died_screen(screen, font):
    global game_state  # Voeg deze regel toe

    died_background = pygame.image.load('C:/Users/mounir/dend game/assets/you_died.png')
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


def input_text(screen, font, prompt, position):
    user_input = ''
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        screen.fill((0, 0, 0))
        show_text(screen, prompt, (position[0], position[1] - 30), font)
        text_surface = font.render(user_input, True, white)
        screen.blit(text_surface, position)
        pygame.display.update()

    return user_input
def dobbelsteen_x(x):
    if x.lower() == 'd6':
        d6 = random.randint(1, 6)
        return d6
    elif x.lower() == 'd4':
        d4 = random.randint(1, 4)
        return d4
    elif x.lower() == 'd8':
        d8 = random.randint(1, 8)
        return d8
    elif x.lower() == 'd10':
        d10 = random.randint(1, 10)
        return d10
    elif x.lower() == 'd12':
        d12 = random.randint(1, 12)
        return d12
    elif x.lower() == 'd20':
        d20 = random.randint(1, 20)
        return d20
    elif x.lower() == 'd100':
        d100 = random.randint(1, 4)
        return d100


def rollen(x, y):
    o = []
    for i in range(y):
        w = dobbelsteen_x(x)
        o.append(w)
    return o


def show_text(screen, text, position, font, color=white):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Functie om de introductietekst te tonen
def show_intro(screen, font, character_name):
    intro_text = (
        f"Hello {character_name}, the hero we've been waiting for, "
        "destined to free the world from monsters.\n"
        "We wish you luck on your quest and hope you are "
        "the hero we've been waiting for all these years."
    )

    background_color = (173, 216, 230)  # Light blue
    screen.fill(background_color)

    intro_font = pygame.font.Font(None, 24)
    wrapped_text = intro_text.split('\n')

    y_pos = 150
    for line in wrapped_text:
        text_surface = intro_font.render(line, True, black)
        text_rect = text_surface.get_rect(center=(width // 2, y_pos))
        screen.blit(text_surface, text_rect)
        y_pos += intro_font.get_linesize()

    pygame.display.update()
    pygame.time.wait(7000)


current_coords = [{"position": (627, 344), "action": "battle"}]  # Begin met alleen het eerste punt
next_coords = [
    {"position": (500, 300), "action": "next_monster", "color": (255, 0, 0)},  # Rood voor nieuwe punten
    {"position": (700, 400), "action": "move_on", "color": (255, 0, 0)}
]

def select_start_position(screen, font, coords):
    world_map = pygame.image.load('C:/Users/mounir/dend game/assets/map2.png')

    running = True
    while running:
        screen.fill(white)
        screen.blit(world_map, (0, 0))

        for coord in coords:
            pygame.draw.circle(screen, green, coord["position"], 10)

        show_text(screen, "Choose your starting position", (20, 20), font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for coord in coords:
                    if pygame.Rect(coord["position"][0] - 10, coord["position"][1] - 10, 20, 20).collidepoint(mouse_pos):
                        return coord["action"]

        pygame.display.update()



def battle(screen, font, player_health, monster_health, player_action):
    tier_dict = {'t1':10; 't2':20; 't3':30}
    
    if player_action == "attack":
        # Speler valt aan
        monster_damage = sum(rollen('d4', 1))
        critfactor = sum(rollen('d10',1))
        if critfactor >=7:
            monster_health -= monster_damage * 1.2
            print(f"Speler doet {monster_damage} schade aan het monster.")
        else:
            monster_health -= monster_damage
            print(f"Speler doet {monster_damage} schade aan het monster.")
    elif player_action == "heal":
        # Speler geneest
        while player_health >=10:
            player_health += 3
            print(f"Speler geneest, huidige gezondheid: {player_health}.")
            time.sleep(2)

    # Monster aanvalsbeurt
    if monster_health > 0:
        player_damage = sum(rollen('d4', 1))
        critfactor = sum(rollen('d10',1))
        if critfactor >=7:
            player_health -= player_damage * 1.2
            print(f"Speler doet {player_damage} schade aan het monster.")
        else:
            player_health -= player_damage
            print(f"Speler doet {player_damage} schade aan het monster.")

    return player_health, monster_health

def show_victory_message(screen, font):
    victory_text = "Victory! Returning to map..."
    show_text(screen, victory_text, (width // 2, height // 2), font, white)
    pygame.display.update()
    pygame.time.wait(3000)


def show_battle_screen(screen, font, player_health, monster_health, background_image):
    # Functie voor het tonen van het gevechtsscherm met aanpasbare achtergrond
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





def new_character_selection(screen, font):
    # Afbeeldingen voor de klassen
    wizard_image = pygame.image.load('C:/Users/mounir/dend game/assets/mage.png')
    rogue_image = pygame.image.load('C:/Users/mounir/dend game/assets/assassin.png')
    paladin_image = pygame.image.load('C:/Users/mounir/dend game/assets/paladin.png')

    # Posities en afmetingen van de afbeeldingen
    wizard_rect = wizard_image.get_rect(topleft=(100, 100))
    rogue_rect = rogue_image.get_rect(topleft=(300, 100))
    paladin_rect = paladin_image.get_rect(topleft=(500, 100))

    # Kleurdefinities
    green = (0, 128, 0)

    running = True
    selected_class = None
    while running:
        screen.fill(green)  # Achtergrondkleur veranderen naar groen

        # Toon de titel
        show_text(screen, "Choose your Character", (20, 20), font)

        # Toon de afbeeldingen
        screen.blit(wizard_image, wizard_rect)
        screen.blit(rogue_image, rogue_rect)
        screen.blit(paladin_image, paladin_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if wizard_rect.collidepoint(mouse_pos):
                    selected_class = "Wizard"
                    running = False
                elif rogue_rect.collidepoint(mouse_pos):
                    selected_class = "Rogue"
                    running = False
                elif paladin_rect.collidepoint(mouse_pos):
                    selected_class = "Paladin"
                    running = False

        pygame.display.update()

    if selected_class:
        character_name = input_text(screen, font, "Enter your character's name:", (100, 100))
        return selected_class, character_name
    return None, None

game_state = "main_menu"
def main_menu():
    global game_state, current_coords, next_coords
    while True:
        if game_state == "main_menu":
            screen.blit(background, (0, 0))
            start_new_game = font.render('Start New Game', True, white)
            exit_game = font.render('Exit Game', True, white)
            load_saved_game = font.render('Load Saved Game', True, white)

            screen.blit(start_new_game, (width // 2 - 100, height // 2 - 50))
            screen.blit(exit_game, (width // 2 - 100, height // 2 + 50))
            screen.blit(load_saved_game, (width // 2 - 100, height // 2 + 150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if width // 2 - 100 <= mouse_pos[0] <= width // 2 + 100:
                        if height // 2 - 50 <= mouse_pos[1] <= height // 2 - 10:
                            # Reset coördinaten bij het starten van een nieuwe game
                            current_coords = [{"position": (627, 344), "action": "battle"}]
                            next_coords = [
                                {"position": (500, 300), "action": "next_monster", "color": (255, 0, 0)},
                                {"position": (700, 400), "action": "move_on", "color": (255, 0, 0)}
                            ]
                            game_state = "character_selection"

        elif game_state == "character_selection":
            selected_class, character_name = new_character_selection(screen, font)
            if selected_class and character_name:
                game_state = "intro"

        elif game_state == "intro":
            show_intro(screen, font, character_name)
            game_state = "select_start_position"

        elif game_state == "select_start_position":
            result = select_start_position(screen, font, current_coords)
            if result == "battle":
                player_health = 10
                monster_health = 15
                battle_result = show_battle_screen(screen, font, player_health, monster_health, 'C:/Users/mounir/dend game/assets/goblin.png')
                if battle_result == "select_start_position":
                    current_coords = next_coords
                    next_coords = []  # Bereid voor op toekomstige updates
            elif result == "next_monster":
                player_health = 10
                new_monster_health = 20
                battle_result = show_battle_screen(screen, font, player_health, new_monster_health, 'C:/Users/mounir/dend game/assets/GIANT_RAT.png')
                if battle_result == "select_start_position":
                    # Hier kun je logica toevoegen voor het geval de speler wint
                    pass
            elif result == "move_on":
                # Logica voor het geval de speler verder gaat zonder te vechten
                pass

        pygame.display.update()

game_state = "main_menu"

if __name__ == '__main__':
    main_menu()





