from squares import *

class Grid:

    def __init__(self, rows, cols, word):

        self.rows = rows
        self.cols = cols
        self.word = word.upper()
        self.word_list = []
        for letter in self.word:
            self.word_list.append(letter)

        self.squares = []
        for row in range(rows):
            self.squares.append([])
            for square in range(cols):
                self.squares[row].append(Square(row, square))

        self.current_row = self.squares[0]
        self.current_row_index = 0

        self.word_square_render = []
        for x in range(cols):
            self.word_square_render.append(Square(5, x, 3))
            self.word_square_render[x].insert_letter(self.word[x])

    def render(self, screen):
        for row in self.squares:
            for square in row:
                square.render(screen)

    def render_win(self, screen):
        for square in self.word_square_render:
            square.render(screen)

    def get_current_row(self):
        return self.current_row

    def check_win(self):

        for square in self.current_row:
            if not (square.get_status() == 3):
                return False
        else:
            return True

    def check_row(self):

        for x in range(len(self.current_row)):
            if self.current_row[x].get_letter() not in self.word_list:
                self.current_row[x].set_status(1)

            elif self.current_row[x].get_letter() == self.word_list[x]:
                self.current_row[x].set_status(3)

            elif self.current_row[x].get_letter() in self.word_list and not (self.word_list.index(self.current_row[x].get_letter()) == self.current_row[x].get_col()):
                self.current_row[x].set_status(2)

        if self.check_win():
            return True
        else:
            return False

    def change_row(self):
        self.current_row_index += 1
        if self.current_row_index == 6:
            return True
        else:
            self.current_row = self.squares[self.current_row_index]
            return False
