import pygame, sys


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.segment_width = 15
        self.segment_height = 15
        self.segment_margin = 3
    
        # Set initial speed
        self.x_change = self.segment_width + self.segment_margin
        self.y_change = 0

        # Create an initial snake
        self.snake_segments = []
        for i in range(15):
            x = 250 - (self.segment_width + self.segment_margin) * i
            y = 30
            segment = Segment(self.screen, x, y, self.segment_width, self.segment_height)
            self.snake_segments.append(segment)

    def change_direction(self, letter):
        if letter == 'L':
            self.x_change = (self.segment_width + self.segment_margin) * -1
            self.y_change = 0
        if letter == 'R':
            self.x_change = (self.segment_width + self.segment_margin)
            self.y_change = 0
        if letter == 'U':
            self.x_change = 0
            self.y_change = (self.segment_height + self.segment_margin) * -1
        if letter == 'D':
            self.x_change = 0
            self.y_change = (self.segment_height + self.segment_margin)
            
    def move(self):
        # Get rid of last segment of the snake .pop() command removes last item in list
        self.snake_segments.pop()

        # Figure out where new segment will be
        x = self.snake_segments[0].x + self.x_change
        y = self.snake_segments[0].y + self.y_change

        # Insert new segment into the list
        segment = Segment(self.screen, x, y, self.segment_width, self.segment_height)
        self.snake_segments.insert(0, segment)

    def draw(self):
        for segment in self.snake_segments:
            segment.draw()


class Segment():
    """ Class to represent one segment of the snake. """

    def __init__(self, screen, x, y, segment_width, segment_height):
        self.screen = screen
        self.x = x
        self.y = y
        self.segment_width = segment_width
        self.segment_height = segment_height

    def draw(self):
        # pygame.draw.rect(screen, color, (x, y, width, height), thickness)
        pygame.draw.rect(self.screen, pygame.Color("Green"),
                         (self.x, self.y, self.segment_width, self.segment_height))


def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Snake Example')

    clock = pygame.time.Clock()
    snake = Snake(screen)

    while True:
        clock.tick(15)  # Sets the game speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction('L')
                if event.key == pygame.K_RIGHT:
                    snake.change_direction('R')
                if event.key == pygame.K_UP:
                    snake.change_direction('U')
                if event.key == pygame.K_DOWN:
                    snake.change_direction('D')

        screen.fill(pygame.Color("Black"))

        snake.move()
        snake.draw()

        pygame.display.update()


main()
