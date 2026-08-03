

import pygame
from pygame import display
from constants.screen_dimensions import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill("black")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            pass
        display.flip()
if __name__ == "__main__":
    main()
