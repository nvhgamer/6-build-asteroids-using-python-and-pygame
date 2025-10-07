# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            # Check for QUIT event to exit the game
            if event.type == pygame.QUIT:
                return

        # screen.fill((0, 0, 0))  # Fill the screen with black
        screen.fill("black")  # Fill the screen with black

        player.draw(screen) # Draw the player

        pygame.display.flip()  # Update the full display Surface to the screen

        delta_time = clock.tick(60)  # Cap the frame rate at 60 FPS
        dt = delta_time / 1000  # Delta time in seconds

    pygame.quit()

if __name__ == "__main__":
    main()
