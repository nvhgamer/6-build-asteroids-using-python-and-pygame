# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            # Check for QUIT event to exit the game
            if event.type == pygame.QUIT:
                return

        # screen.fill((0, 0, 0))  # Fill the screen with black
        screen.fill("black")  # Fill the screen with black

        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()
