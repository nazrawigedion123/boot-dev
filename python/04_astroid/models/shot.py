#models/shot
from models.circleshape import CircleShape
from constants.shot import SHOT_RADIOUS
import pygame
from constants.screendimensions import SCREEN_WIDTH
class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIOUS)


    def draw(self, screen:pygame.Surface)->None:
        pygame.draw.circle(screen,"white",self.position,self.radius,SCREEN_WIDTH)
    def update(self, dt: float) -> None:

        self.position +=  self.velocity * dt
        

