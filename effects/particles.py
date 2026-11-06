
import cv2
import random
import math


class Particle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-3, 1)

        self.life = random.randint(20, 40)
        self.radius = random.randint(2, 5)


class ParticleEffect:

    def __init__(self):
        self.particles = []

    def emit(self, point, count=3):

        for _ in range(count):
            self.particles.append(
                Particle(point[0], point[1])
            )

    def update(self, frame):

        for particle in self.particles[:]:

            particle.x += particle.vx
            particle.y += particle.vy

            particle.life -= 1

            if particle.life <= 0:
                self.particles.remove(particle)
                continue

            cv2.circle(
                frame,
                (int(particle.x), int(particle.y)),
                particle.radius,
                (255, 0, 180),
                -1,
                cv2.LINE_AA
            )

        return frame
