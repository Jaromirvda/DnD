import pygame
import sys
import random
from karakters_info import *
from screens import *
from battle import *
pygame.init()



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



def select_start_position(screen, font, coords):
    world_map = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/map2.png')

    running = True
    while running:
        screen.fill(white)
        screen.blit(world_map, (0, 0))

        for coord in coords:
            color = coord["color"] if "color" in coord else green
            pygame.draw.circle(screen, color, coord["position"], 10)

        show_text(screen, "Choose your starting position", (20, 20), font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for coord in coords:
                    circle_rect = pygame.Rect(coord["position"][0] - 10, coord["position"][1] - 10, 20, 20)
                    if circle_rect.collidepoint(mouse_pos):
                        return coord["action"]

        pygame.display.update()



def show_victory_message(screen, font):
    victory_text = "Victory! Returning to map..."
    show_text(screen, victory_text, (width // 2, height // 2), font, white)
    pygame.display.update()
    pygame.time.wait(3000)








def new_character_selection(screen, font):
    # Afbeeldingen voor de klassen
    wizard_image = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/mage.png')
    rogue_image = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/assassin.png')
    paladin_image = pygame.image.load('C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/paladin.png')

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
                    # Controleer voor 'Start New Game'
                    if width // 2 - 100 <= mouse_pos[0] <= width // 2 + 100 and height // 2 - 50 <= mouse_pos[1] <= height // 2 - 10:
                        current_coords = [{"position": (627, 344), "action": "goblin_battle"}]
                        next_coords = [
                            {"position": (500, 300), "action": "rat_battle", "color": red},
                            {"position": (550, 250), "action": "troll_battle", "color": blue}]
                        game_state = "character_selection"
                    # Controleer voor 'Exit Game'
                    elif width // 2 - 100 <= mouse_pos[0] <= width // 2 + 100 and height // 2 + 50 <= mouse_pos[1] <= height // 2 + 90:
                        pygame.quit()
                        sys.exit()


        elif game_state == "character_selection":
            selected_class, character_name = new_character_selection(screen, font)
            if selected_class and character_name:
                game_state = "intro"

        elif game_state == "intro":
            show_intro(screen, font, character_name)
            game_state = "select_start_position"

        elif game_state == "select_start_position":
            result = select_start_position(screen, font, current_coords)
            if result == "goblin_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health
                elif selected_class == 'Paladin':
                    player_health = paladin.health
                elif selected_class == 'Rogue':
                    player_health = assisin.health
                monster_health = 15
                battle_result = show_battle_screen(screen, font, player_health, monster_health, 'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/goblin.png')
                if battle_result == "select_start_position":
                    current_coords = next_coords
                    next_coords = [
                        {"position": (300, 350), "action": "giant_battle", "color": yellow},
                        {"position": (450, 300), "action": "hellhound_battle", "color": purple}]

            elif result == "rat_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health
                elif selected_class == 'Paladin':
                    player_health = paladin.health
                elif selected_class == 'Rogue':
                    player_health == assisin.health
                rat_health = 15
                battle_result = show_battle_screen(screen, font, player_health, rat_health, 'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/GIANT_RAT.png')
                if battle_result == "select_start_position":
                    current_coords = next_coords

            elif result == "troll_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health
                elif selected_class == 'Paladin':
                    player_health = paladin.health
                elif selected_class == 'Rogue':
                    player_health == assisin.health
                troll_health = 15
                battle_result = show_battle_screen(screen, font, player_health, troll_health, 'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/troll.png')
                if battle_result == "select_start_position":
                    current_coords = next_coords

            elif result == "giant_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health
                elif selected_class == 'Paladin':
                    player_health = paladin.health
                elif selected_class == 'Rogue':
                    player_health == assisin.health+3
                giant_health = 20
                battle_result = show_battle_screen(screen, font, player_health, giant_health,
                                                   'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/giant.png')
                if battle_result == "select_start_position":
                    # Update naar coördinaten van de draak en beholder
                    current_coords = [
                        {"position": (100, 300), "action": "dragon_battle", "color": green},
                        {"position": (200, 450), "action": "beholder_battle", "color": orange}
                    ]

            elif result == "hellhound_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health 
                elif selected_class == 'Paladin':
                    player_health = paladin.health
                elif selected_class == 'Rogue':
                    player_health == assisin.health+3
                hellhound_health = 20
                battle_result = show_battle_screen(screen, font, player_health, hellhound_health,
                                                   'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/hellhound.png')
                if battle_result == "select_start_position":
                    # Update naar coördinaten van de draak en beholder
                    current_coords = [
                        {"position": (700, 400), "action": "dragon_battle", "color": green},
                        {"position": (200, 450), "action": "beholder_battle", "color": orange}
                    ]

            elif result == "dragon_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health+10
                elif selected_class == 'Paladin':
                    player_health = paladin.health+5
                elif selected_class == 'Rogue':
                    player_health == assisin.health+13
                dragon_health = 30
                battle_result = show_battle_screen(screen, font, player_health, dragon_health, 'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/dragon.png')
                if battle_result == "select_start_position":
                    show_end_screen(screen, font, "You Saved the World!")
                    game_state = "main_menu"

            elif result == "beholder_battle":
                if selected_class == 'Wizard':
                    player_health = mage.health +10
                elif selected_class == 'Paladin':
                    player_health = paladin.health +5
                elif selected_class == 'Rogue':
                    player_health == assisin.health +13
                beholder_health = 30
                battle_result = show_battle_screen(screen, font, player_health, beholder_health, 'C:/Users/vdaja/OneDrive/Documenten/School/python/DnD/Assets/beholder.png')
                if battle_result == "select_start_position":
                    show_end_screen(screen, font, "You Saved the World!")
                    game_state = "main_menu"

        pygame.display.update()

game_state = "main_menu"

if __name__ == '__main__':
    main_menu()





