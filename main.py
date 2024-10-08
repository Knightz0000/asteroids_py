import pygame
import random
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for values in updatable:
            values.update(dt)
        screen.fill("black")
        for values in drawable:
            values.draw(screen)
        for asteroid in asteroids:
            if asteroid.colision(player):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.colision(shot):
                    shot.kill()
                    asteroid.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
