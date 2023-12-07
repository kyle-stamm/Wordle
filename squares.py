import pygame
import math
pygame.init()


class Square:

    SQUARE_DIMENSION = 75
    INITIAL_X_OFFSET = (750 - (SQUARE_DIMENSION * 5)) / 2.0
    INITIAL_Y_OFFSET = 75
    INNER_COLOR_GREY = (150, 150, 150)
    INNER_COLOR_DARK_GREY = (125, 125, 125)
    INNER_COLOR_YELLOW = (195, 217, 26)
    INNER_COLOR_GREEN = (22, 107, 22)
    EDGE_COLOR = (100, 100, 100)
    FONT = pygame.font.SysFont('cambria', int(math.floor((SQUARE_DIMENSION ** 2) / 140.625)))
    FONT_COLOR = (240, 240, 240)

    def __init__(self, row, col, initial_status=-1):

        self.row = row
        self.col = col
        self.letter = ''

        self.x = self.INITIAL_X_OFFSET + (self.col * self.SQUARE_DIMENSION)
        self.y = self.INITIAL_Y_OFFSET + (self.row * self.SQUARE_DIMENSION)
        self.hitbox = pygame.Rect(self.x, self.y, self.SQUARE_DIMENSION, self.SQUARE_DIMENSION)

        self.status = initial_status

    def render(self, screen):

        if self.status == -1:
            pygame.draw.rect(screen, self.INNER_COLOR_GREY, self.hitbox)

        elif self.status == 1:
            pygame.draw.rect(screen, self.INNER_COLOR_DARK_GREY, self.hitbox)

        elif self.status == 2:
            pygame.draw.rect(screen, self.INNER_COLOR_YELLOW, self.hitbox)

        elif self.status == 3:
            pygame.draw.rect(screen, self.INNER_COLOR_GREEN, self.hitbox)

        text = self.FONT.render(self.letter, True, self.FONT_COLOR)
        screen.blit(text, (self.x + (self.SQUARE_DIMENSION / 2.0) - (text.get_width() / 2.0),
                           self.y + (self.SQUARE_DIMENSION / 2.0) - (text.get_height() / 2.0)))

        pygame.draw.rect(screen, self.EDGE_COLOR, self.hitbox, 5)

    def insert_letter(self, letter):
        self.letter = letter

    def set_status(self, status):
        self.status = status

    def get_col(self):
        return self.col

    def get_letter(self):
        return self.letter

    def get_status(self):
        return self.status
