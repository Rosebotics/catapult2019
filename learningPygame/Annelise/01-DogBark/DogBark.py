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

    # Load the music and the image
    # Done 1: Create an image with the 2dogs.JPG image

    dog_image = pygame.image.load("2dogs.JPG")

    # Done 4: Create a font object with a size 28 font.
    caption_font = pygame.font.Font(None, 28)
    # TODO 7: Load the sound "bark.mp3" into the pygame music mixer.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 8: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # Done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))
        # Done 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0,0))
        # Draw the text onto the screen
        # Done 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        caption = caption_font.render("Two Dogs.", True, BLACK)
        # Done 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption, ((IMAGE_SIZE - caption.get_width()) // 2, IMAGE_SIZE + 5))

        meme_font = pygame.font.Font(None, 35)
        meme_text = meme_font.render("I'm 2 minutes older, I go first.", True, WHITE)
        screen.blit(meme_text, ((IMAGE_SIZE - caption.get_width()) // 4, IMAGE_SIZE - 450))

        # Update the screen
        pygame.display.update()


main()
