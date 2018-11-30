import pygame, os, sys
from pygame.locals import *

def main():
    screen = pygame.display.set_mode((1000, 1000))
    #screen.toggle_fullscreen()
    player = pygame.image.load('characters/cat.png').convert()

    screen.fill((255, 255, 255))

    pControl = GameObject(player, 70, 1, "idle", 200, 200)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (K_w, K_UP):
                    pControl.setState("n")
                elif event.key in (K_d, K_RIGHT):
                    pControl.setState("e")
                elif event.key in (K_s, K_DOWN):
                    pControl.setState("s")
                elif event.key in (K_a, K_LEFT):
                    pControl.setState("w")
                
                elif event.key == K_ESCAPE:
                    sys.exit()

            elif event.type == KEYUP:
                if event.key in (K_w, K_d, K_s, K_a, K_UP, K_RIGHT, K_DOWN, K_LEFT):
                    pControl.state = "idle"

        screen.fill((255, 255, 255))

        pControl.setMovement()
        screen.blit(pControl.image, pControl.pos)

        pygame.display.update()
        #pygame.time.delay(1)

class GameObject():

    states = ["idle", "n", "s", "w", "e"]

    def __init__(self, image, height, speed, state, x, y):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(x, y)
        self.state = state
        self.x = x
        self.y = y

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setImage(self, image):
        self.image = image
        self.rect = image.get_rect().move(x, y)

    def getImage(self):
        return self.image

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def setState(self, state):
        if state in self.states:
            self.state = state

    def getState(self):
        return self.state

    def getStates():
        return states

    def setMovement(self):
        if self.state == "n": #North
            if self.y - self.speed > 0:
                self.y -= self.speed
                self.pos = self.pos.move(0, -self.speed)
            else:
                self.y = 0
                self.pos = self.pos.move(0, -self.y)
        elif self.state == "s": #South
            if self.y + self.speed < 1000:
                self.y += self.speed
                self.pos = self.pos.move(0, self.speed)
            else:
                self.y = 1000
                self.pos = self.pos.move(0, self.y)
        elif self.state == "w": #West
            if self.x - self.speed > 0:
                self.x -= self.speed
                self.pos = self.pos.move(-self.speed, 0)
            else:
                self.x = 0
                self.pos = self.pos.move(-self.x, 0)
        elif self.state == "e": #East
            if self.x + self.speed < 1000:
                self.pos = self.pos.move(self.speed, 0)
                self.x += self.speed
            else:
                self.x = 1000
                self.pos = self.pos.move(self.x, 0)


if __name__ == "__main__":
    main()