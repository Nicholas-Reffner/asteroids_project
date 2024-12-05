import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *




def main():

    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

   
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for thing in updatable:
            thing.update(dt)

        for object in asteroids:
           if object.collisions(player):
               print("Game Over!")
               event.type == pygame.QUIT
               return

        screen.fill('black')
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


        
if __name__ == "__main__":
    main()
