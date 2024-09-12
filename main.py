import pygame
import sys
import time
from constants import *
from player import *
from asteroid import *
from asteroidField import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    group_updateable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()

    # look at parent of parent of Player, Asteroid, or 
    # AsteroidField to see how container works.
    Player.containers = (group_updateable, group_drawable)
    Asteroid.containers = (group_asteroids, group_updateable, group_drawable)
    AsteroidField.containers = (group_updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    asteroidField = AsteroidField()

    go = True
    while(go):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in group_drawable:
            thing.draw(screen)

        pygame.display.flip() #refreshes the screen
        dt = clock.tick(60) / 1000 # converted to seconds        
        
        for thing in group_updateable:
            thing.update(dt)

        for thing in group_asteroids:
            if player.collisions(thing):
                font = pygame.font.Font(pygame.font.get_default_font(), 36)
                text_surface = font.render('Game over!', True, (50, 150, 50))
                go = False
                screen.blit(text_surface, dest=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                pygame.display.flip() #refreshes the screen
                time.sleep(5)
                #sys.exit()

if __name__ == "__main__":
    main()