import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png") # Load the mole image
        screen = pygame.display.set_mode((640, 512)) # Defines size of window
        clock = pygame.time.Clock() # clock object that controls frame rate

        square = 32
        width = 20
        height = 16
        mole_x = 0
        mole_y = 0

        running = True
        while running:
            for event in pygame.event.get(): # a for loop that will get all the events happening to your window
                if event.type == pygame.QUIT: # when corner X gets clicked, game closes
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos # variable which holds (x,y) position of the click
                # checks position of mole, and if the click is within the range of the mole
                if mole_x * square <= mouse_x < (mole_x + 1) * square and mole_y * square <= mouse_y < (mole_y + 1) * square:
                    # randomizes position of the mole if true
                    mole_x = random.randrange(0, width)
                    mole_y = random.randrange(0, height)

            screen.fill("light pink") # fills the screen with a color

            for x in range(0, 640, square):
                pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 512))
            for y in range(0, 512, square):
                pygame.draw.line(screen, (255, 255, 255), (0,y), (640, y))

            screen.blit(mole_image, (mole_x * square, mole_y * square))

            pygame.display.flip() # updates the screen
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
