import pygame
pygame.init()


class Button:

    TEXT_COLOR = (0, 0, 0)
    SCREEN_HEIGHT, SCREEN_WIDTH = (750, 750)

    def __init__(self, string, height, width, color, scene, x_pos=None, y_pos=None):

        self.height, self.width = (height, width)
        if not x_pos:
            self.x = (self.SCREEN_WIDTH / 2.0) - (self.width / 2.0)
        else:
            self.x = x_pos

        if not y_pos:
            self.y = (self.SCREEN_HEIGHT / 2.0) - (self.height / 2.0)
        else:
            self.y = y_pos
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        self.string = string
        self.font = pygame.font.SysFont('cambria', 18)
        self.text = self.font.render(string, True, self.TEXT_COLOR)
        self.text_x = self.x + (self.width / 2.0) - (self.text.get_width() / 2.0)
        self.text_y = self.y + (self.height / 2.0) - (self.text.get_height() / 2.0)
        self.text_position = (self.text_x, self.text_y)

        self.color = color
        self.scene = scene
        if self.scene == 1:
            self.edge_color = (0, 0, 0)
        else:
            self.edge_color = (100, 100, 100)

        self.clicked = False

        self.action = None
        if self.string == 'Start':
            self.action = 2
        elif self.string == 'Play Again':
            self.action = 1
        elif self.string == 'Exit':
            self.action = -1

    def render(self, screen):

        pygame.draw.rect(screen, self.color, self.hitbox)
        pygame.draw.rect(screen, self.edge_color, self.hitbox, 5)
        screen.blit(self.text, self.text_position)

    def get_scene(self):
        return self.scene

    def get_hitbox(self):
        return self.hitbox

    def is_clicked(self):
        return self.clicked

    def set_clicked_true(self):
        self.clicked = True
        return self.action

    def set_clicked_false(self):
        self.clicked = False


class LetterButton(Button):

    LETTER_BOX_WIDTH = 50
    LETTER_BOX_HEIGHT = 50
    LETTER_BOX_COLOR = (215, 215, 215)

    def __init__(self, letter, x_pos, y_pos):

        super().__init__(letter, self.LETTER_BOX_HEIGHT, self.LETTER_BOX_WIDTH,
                         self.LETTER_BOX_COLOR, 2, x_pos=x_pos, y_pos=y_pos)

    def get_letter(self):
        return self.string
