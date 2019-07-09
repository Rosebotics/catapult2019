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
    pygame.display.set_caption("Text, Sound, and an Image")
    image = pygame.image.load("2dogs.JPG")
    font = pygame.font.Font(None, 90)
    pygame.mixer.music.load("bark.mp3")

    # Load the music and the image
    # TODO 4: Create a font object with a size 28 font.
    # TODO 7: Load the sound "bark.mp3" into the pygame music mixer.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 8: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)
        image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))
        top = font.render("when u", True, (255, 255, 255))
        bottom = font.render("bottom text", True, (255, 255, 255))
        screen.blit(image, (0, 0))
        screen.blit(top, ((IMAGE_SIZE - top.get_width())//2, 20))
        screen.blit(bottom, ((IMAGE_SIZE - bottom.get_width()) // 2, 400))



        # Draw the image onto the screen
        # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)

        # Draw the text onto the screen
        # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.

        # Update the screen
        pygame.display.update()


main()
