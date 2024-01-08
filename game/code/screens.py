import pygame
import sys

# In deze file vind u alle soorten schermen die ontwikkeld werden voor de game. alle benodigdheden etc. zijn erbij inbegrepen.
pygame.init()

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


# Lettertype
font = pygame.font.Font(None, 36)



def show_end_screen(screen, font, message):
    screen.fill(black)
    end_text = font.render(message, True, white)
    text_rect = end_text.get_rect(center=(width // 2, height // 2))
    screen.blit(end_text, text_rect)
    pygame.display.update()
    pygame.time.wait(5000)



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
