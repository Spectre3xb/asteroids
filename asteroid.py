import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.vertices = self._generate_vertices()

    def draw(self, screen):
        points = [(self.position.x + vertex.x, self.position.y + vertex.y)
                  for vertex in self.vertices]
        pygame.draw.polygon(screen, "white", points, 2)

    def _generate_vertices(self):
        num_vertices = random.randint(9, 15)  # Random number of points
        vertices = []

        for i in range(num_vertices):
            angle = (i / num_vertices) * 360
            distance = self.radius * random.uniform(0.7, 1.0)

            rad = pygame.math.Vector2(distance, 0).rotate(angle)
            vertices.append(rad)

        return vertices

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

