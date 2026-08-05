from models.circleshape import CircleShape
from constants.screendimensions import SCREEN_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)



    def draw(self, screen:pygame.Surface)->None:
        pygame.draw.circle(screen,"white",self.position,self.radius,SCREEN_WIDTH)
    def update(self, dt: float) -> None:
        self.move(dt)

    def move(self,dt : float)->None:
        
        self.position +=  self.velocity * dt

