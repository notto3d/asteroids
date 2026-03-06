import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        radius = SHOT_RADIUS
    def draw(self, screen):
        width = LINE_WIDTH
        pygame.draw.circle(screen, "white", self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt