import pygame, sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()
    pygame.font.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption('DOGGOS')

    # Load the music and the image
    # DONE 1: Create an image with the 2dogs.JPG image
    puppers = pygame.image.load('2dogs.JPG')
    # DONE 4: Create a font object with a size 28 font.
    captionfont = pygame.font.Font(None, 28)
    captionfont2 = pygame.font.Font(None, 28)
    # DONE 7: Load the sound "bark.mp3" into the pygame music mixer.
    pygame.mixer.music.load('puppy.wav')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # DONE 8: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # DONE 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        puppers = pygame.transform.scale(puppers, (IMAGE_SIZE, IMAGE_SIZE))
        # DONE 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(puppers, (0, 0))
        # Draw the text onto the screen
        # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        caption = captionfont.render('Runtime error', True, BLACK)
        caption2 = captionfont2.render('Me', True, BLACK)
        # DONE 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption, (280, 100))
        screen.blit(caption2, (100, 45))
        # Update the screen
        pygame.display.update()


main()
