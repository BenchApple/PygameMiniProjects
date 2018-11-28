import sys, os, pygame
from pygame.locals import *
from random import randint

pygame.init()
size = width, height = 1920, 1080

def main():

    screen = pygame.display.set_mode(size)

    text = "OK now THIS is epic!"
    color = (0, 0, 0)
    default = pygame.font.get_default_font()
    fontSize = 35
    ga = pygame.font.Font(default, fontSize)
    pygame.mouse.set_visible(0)

    benshapiro = pygame.image.load('benshapiro.jpg').convert()

    pygame.display.set_caption(text)

    screen.fill((250, 250, 250))

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                return
        
        screen.blit(benshapiro, (800, 500), benshapiro.get_rect())
        showText(screen, ga, text, (randint(0 - fontSize, width), randint(0, height)), (randint(0, 255), randint(0, 255), randint(0, 255)))
        pygame.time.wait(25)       

def showText(screen, font, text, position, color, background = None): #position must be a tuple or else this doesn't work
    if isinstance(position, tuple):
        textRen = font.render(text, True, color, background)
        textRect = textRen.get_rect()
        screen.blit(textRen, position, textRect)
        pygame.display.update()

if __name__ == "__main__":
    main()