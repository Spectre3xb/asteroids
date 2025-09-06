import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)

        alpha = self.velocity.rotate(split_angle)
        beta = self.velocity.rotate(-split_angle)

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid.velocity = alpha *1.2
        asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid.velocity = beta * 1.2

