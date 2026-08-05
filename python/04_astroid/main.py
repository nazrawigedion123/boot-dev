

from typing import overload

import pygame
from constants.screendimensions import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from models.asteroid import Asteroid
from models.asteroidfield import AsteroidField
from models.player import Player
def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0.0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    player= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    


    asteroids=pygame.sprite.Group()

    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)

    asteroidfield=AsteroidField() 
    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        dt=clock.tick(60)/1000.0
            
        updatable.update(dt)
            
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
