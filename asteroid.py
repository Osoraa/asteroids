from logger import log_event
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self) -> None:
        x = self.position[0]
        y = self.position[1]
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        asteroid_angle = random.uniform(20, 50)

        asteroid_a = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_b = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)

        asteroid_a.velocity = self.velocity.rotate(asteroid_angle) * 1.2
        asteroid_b.velocity = self.velocity.rotate(360 - asteroid_angle) * 1.2
