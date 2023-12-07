import pygame.font


class Text:

    SCREEN_HEIGHT, SCREEN_WIDTH = (750, 750)

    def __init__(self, string,  font_size, text_color, scene, x_pos=None, y_pos=None):

        self.string = string
        self.scene = scene

        self.font = pygame.font.SysFont('cambria', font_size)
        self.text = self.font.render(self.string, True, text_color)

        if not x_pos:
            self.x = (self.SCREEN_WIDTH / 2.0) - (self.text.get_width() / 2.0)
        else:
            self.x = x_pos

        if not y_pos:
            self.y = (self.SCREEN_HEIGHT / 2.0) - (self.text.get_height() / 2.0)
        else:
            self.y = y_pos

    def render(self, screen):
        screen.blit(self.text, (self.x, self.y))

    def get_text_string(self):
        return self.string

    def get_scene(self):
        return self.scene

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
