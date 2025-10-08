# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidField = AsteroidField()

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            # Check for QUIT event to exit the game
            if event.type == pygame.QUIT:
                return

        # screen.fill((0, 0, 0))  # Fill the screen with black
        screen.fill("black")  # Fill the screen with black

        updatable.update(dt)   # Update all updateable sprites

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen)  # Draw the sprite

        pygame.display.flip()  # Update the full display Surface to the screen

        delta_time = clock.tick(60)  # Cap the frame rate at 60 FPS
        dt = delta_time / 1000  # Delta time in seconds

if __name__ == "__main__":
    main()
