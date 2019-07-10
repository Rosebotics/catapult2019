import pygame
import sys


def get_row_col(mouse_x, mouse_y):
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


class Game:
    def __init__(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.turn_counter = 0
        self.game_is_over = False

    def take_turn(self):
        """Handle the current turn of the player and update board array"""
        if self.game_is_over:
            return
        click_x, click_y = pygame.mouse.get_pos()
        row, col = get_row_col(click_x, click_y)
        if row < 0 or row > 3 or col < 0 or col > 3:
            return
        if self.board[row][col] == '.':
            if self.turn_counter % 2 == 0:
                self.board[row][col] = 'X'
                pygame.display.set_caption("O's Turn")
            else:
                self.board[row][col] = 'O'
                pygame.display.set_caption("X's Turn")
            self.turn_counter = self.turn_counter + 1
            if self.turn_counter >= 9:
                self.game_is_over = True
                pygame.display.set_caption("Tie Game")
        self.check_for_game_over()

    def check_for_game_over(self):
        pygame.mixer.music.load("win.mp3")
        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        for line in lines:
            if line == "XXX":
                self.game_is_over = True
                pygame.display.set_caption("X is winner!")
                pygame.mixer.music.play()
            if line == "OOO":
                self.game_is_over = True
                pygame.display.set_caption("O is winner")
                pygame.mixer.music.play()
        # TODO: Use the lines list to determine if there is a winner.
        # TODO: If there is a winner, update the title text, play a sound, and set game_is_over to True.


def draw_board(screen, game):
    for row in range(3):
        for col in range(3):
            current_mark = game.board[row][col]
            if current_mark == "X":
                xImage = pygame.image.load("x_mark.png")
                screen.blit(xImage, get_xy_position(row, col))
            if current_mark == "O":
                oImage = pygame.image.load("o_mark.png")
                screen.blit(oImage, get_xy_position(row, col))




def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    pygame.display.set_caption("X's Turn")

    board_surface = pygame.image.load("board.png")
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            key = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP:
                game.take_turn()
            if key[pygame.K_SPACE]:
                game = Game()
                pygame.display.set_caption("X's Turn")
        screen.fill(pygame.Color("white"))
        screen.blit(board_surface, get_xy_position(0, 0))

        draw_board(screen, game)

        pygame.display.update()


main()
