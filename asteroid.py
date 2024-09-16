from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 
    
    def update(self, dt):
        self.position += self.velocity * dt

    #Assumptions
    #  an astroid has been hit by a shot
    #Expected behaviour
    #  if astroid is too small it is removed else
    #  2 smaller astroids are formed with a random 
    #  angle of 20 to 50 as their new heading.
    #Encapsulation changes
    #  either a small astroid is removed from game or 
    #  2 new astroids are created that are one size smaller
    #  its predecessor.
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20.0, 50.0)
            left_vect = self.velocity.rotate(-1 * new_angle)
            right_vect = self.velocity.rotate(new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS 
            asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid1.velocity = left_vect * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid2.velocity = right_vect * 1.2

            