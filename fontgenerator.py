import pygame
import os
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()


pygame.init()
pygame.mixer.init()

fixedword = ""
fixedword2 = ""
sentence = ""
sentence2 = ""
sentence3 = ""
sentence4 = ""
sentence5 = ""
cooldown = False
x = 0

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hmmmm")

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
LIME = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
SILVER = 192, 192, 192
GREY = 128, 128, 128
DARKGREY = 64, 64, 64
MAROON = 128, 0, 0
OLIVE = 128, 128, 0
GREEN = 0, 128, 0
PURPLE = 128, 0, 128
TEAL = 0, 128, 128
NAVY = 0, 0, 128





FONT = pygame.font.SysFont("russoone", 40)
BIGFONT = pygame.font.SysFont("russoone", 70)


FPS = 60


if __name__ == "__main__":

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN and cooldown == False:
            mx, my = pygame.mouse.get_pos()
            if mx >= 10 and mx <= 310 and my >= 10 and my <= 110:
                sentence = (random.choice(WORDS).decode('utf-8') + " " + random.choice(WORDS).decode('utf-8'))
                sentence2 = (random.choice(WORDS).decode('utf-8') + " " + random.choice(WORDS).decode('utf-8'))
                sentence3 = (random.choice(WORDS).decode('utf-8') + " " + random.choice(WORDS).decode('utf-8'))
                sentence4 = (random.choice(WORDS).decode('utf-8') + " " + random.choice(WORDS).decode('utf-8'))
                sentence5 = (random.choice(WORDS).decode('utf-8') + " " + random.choice(WORDS).decode('utf-8'))
                cooldown = True
        if cooldown == True:
            x += 1
            if x == 10:
                x = 0
                cooldown = False
        keys_pressed = pygame.key.get_pressed()




        WIN.fill(WHITE)
        button = pygame.Rect(10, 10, 300, 100)
        pygame.draw.rect(WIN, NAVY, button)
        text = BIGFONT.render("Generate", 1, WHITE)
        WIN.blit(text, (30, 40))
        fonttext = FONT.render(sentence, 1, BLACK)
        fonttext2 = FONT.render(sentence2, 1, BLACK)
        fonttext3 = FONT.render(sentence3, 1, BLACK)
        fonttext4 = FONT.render(sentence4, 1, BLACK)
        fonttext5 = FONT.render(sentence5, 1, BLACK)

        WIN.blit(fonttext, (30, 160))
        WIN.blit(fonttext2, (30, 200))
        WIN.blit(fonttext3, (30, 240))
        WIN.blit(fonttext4, (30, 280))
        WIN.blit(fonttext5, (30, 320))
        pygame.display.update()



