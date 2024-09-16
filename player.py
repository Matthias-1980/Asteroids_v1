from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    #Assumptions
    #  one of the following keys is being pressed to rotate the ship: a, d.
    #Expected behaviour
    #  alters the player ship's rotation
    #Encapsulation change
    #  player ship's rotate variable 
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    #Assumptions
    #  the update phase in main.py is being iterated over every one frame per second.
    #Expected behaviour
    #  depending on various keys the ship is either moved, rotated, or it shoots.
    #Encapsulation change
    #  timer is decremented
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)

    #Assumptions
    #  one of the following keys is being pressed to move the ship: s, w.
    #Expected behaviour
    #  moves the player ship forwards or backwards.
    #Encapsulation change
    #  player's position is altered.
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #Assumptions 
    #  space bar has been pressed and the timer is at 0 or below.
    #Expected behaviour 
    #  a new bullet is created, and it is given a direction and velocity.
    #Encapsulation change 
    #  timer is reset.
    def shoot(self, dt):
        self.timer = PLAYER_SHOT_COOLDOWN
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)    
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity = forward * PLAYER_SHOT_SPEED
    