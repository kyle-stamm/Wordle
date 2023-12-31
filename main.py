import random
import time
import pygame

from text import *
from buttons import *
from grid import *
pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = (750, 750)
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Wordle")

running = True
start = False
end = [False, None]

text_list = [Text('Welcome to Wordle!', 48, (0, 0, 0), 1, y_pos=200),
             Text('WORDLE', 36, (240, 240, 240), 2, y_pos=20),
             Text('You Won!', 60, (0, 0, 0), 3, y_pos=300),
             Text('You Lost!', 60, (0, 0, 0), 4, y_pos=300)]
button_list = [Button('Start', 100, 200, (150, 50, 0), 1, y_pos=400),
               Button('Exit', 50, 50, (150, 50, 0), 2, x_pos=690, y_pos=10),
               Button('Exit', 100, 150, (12, 176, 194), 3, x_pos=400, y_pos=475),
               Button('Play Again', 100, 150, (12, 176, 194), 3, x_pos=200, y_pos=475),
               Button('Exit', 100, 150, (12, 176, 194), 4, x_pos=400, y_pos=475),
               Button('Play Again', 100, 150, (12, 176, 194), 4, x_pos=200, y_pos=475)]
alphabet = [LetterButton('Q', 125, 550),
            LetterButton('W', 175, 550),
            LetterButton('E', 225, 550),
            LetterButton('R', 275, 550),
            LetterButton('T', 325, 550),
            LetterButton('Y', 375, 550),
            LetterButton('U', 425, 550),
            LetterButton('I', 475, 550),
            LetterButton('O', 525, 550),
            LetterButton('P', 575, 550),
            LetterButton('A', 150, 600),
            LetterButton('S', 200, 600),
            LetterButton('D', 250, 600),
            LetterButton('F', 300, 600),
            LetterButton('G', 350, 600),
            LetterButton('H', 400, 600),
            LetterButton('J', 450, 600),
            LetterButton('K', 500, 600),
            LetterButton('L', 550, 600),
            LetterButton('Z', 200, 650),
            LetterButton('X', 250, 650),
            LetterButton('C', 300, 650),
            LetterButton('V', 350, 650),
            LetterButton('B', 400, 650),
            LetterButton('N', 450, 650),
            LetterButton('M', 500, 650)]

word_bank = []
file = open('5 letter words.txt')
for line in file:
    word_bank.append(line.strip())
file.close()

wordle_bank = []
file = open('wordle bank.txt')
for line in file:
    wordle_bank.append(line.strip())
file.close()

ERROR_FONT = pygame.font.SysFont('cambria', 48)


def update(x_pos, y_pos):

    global scene, start, grid, end

    if x_pos and y_pos:
        if scene == -1:
            quit()
        elif scene == 1:

            for button in button_list:
                if button.get_hitbox().collidepoint(x_pos, y_pos) and button.get_scene() == scene:
                    scene = button.set_clicked_true()
                    start = True
                    grid = Grid(6, 5, wordle_bank[random.randint(0, len(wordle_bank) - 1)], word_bank)
                    # grid = Grid(6, 5, word_bank[0], word_bank)

        elif scene == 2:

            user_types = True
            user_input = ['', '', '', '', '']
            flag = False
            index_first_blank = 0

            while user_types:

                if user_input[len(user_input) - 1] == '':
                    index_first_blank = user_input.index('')
                else:
                    flag = True

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        quit()
                    elif event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN and user_input[4] != '':
                            word_str = ''
                            for letter in user_input:
                                word_str += letter

                            if word_str.lower() in word_bank:
                                user_types = False
                            else:
                                invalid_word_text = ERROR_FONT.render("Not In Word List", True, (0, 0, 0))
                                pygame.draw.rect(screen, (150, 0, 0), (175, 275, 400, 200))
                                screen.blit(invalid_word_text, (175 + 200 - (invalid_word_text.get_width() / 2.0), 275 + 100 - (invalid_word_text.get_height() / 2.0)))
                                pygame.display.flip()
                                time.sleep(1)

                        elif event.key == pygame.K_BACKSPACE:
                            if not flag:
                                user_input[index_first_blank - 1] = ''
                            else:
                                user_input[4] = ''
                                flag = False
                            print(user_input)
                        elif not flag and event.unicode.isalpha():
                            user_input[index_first_blank] = event.unicode.upper()
                            print(user_input)

                for square in grid.get_current_row():
                    square.insert_letter(user_input[square.get_col()])

                if not user_types:

                    user_input = ['', '', '', '', '']

                    if grid.check_row(alphabet):
                        scene = 3
                        end[0] = True
                        end[1] = 'win'
                        start = False

                    elif grid.change_row():
                        scene = 4
                        end[0] = True
                        end[1] = 'lose'
                        start = False

                if pygame.mouse.get_pressed()[0]:
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]

                else:
                    x_pos = None
                    y_pos = None

                if x_pos and y_pos and not end[0]:
                    for button in button_list:
                        if button.get_hitbox().collidepoint(x_pos, y_pos) and button.get_scene() == scene:
                            scene = button.set_clicked_true()

                    for letter in alphabet:

                        if letter.is_clicked():
                            if not letter.get_hitbox().collidepoint(x_pos, y_pos):
                                letter.set_clicked_false()

                        if letter.get_hitbox().collidepoint(x_pos, y_pos):
                            if not flag and not letter.is_clicked():
                                user_input[index_first_blank] = letter.get_letter()
                                print(user_input)
                                letter.set_clicked_true()

                render()
                pygame.display.flip()

        elif scene == 3:

            if x_pos and y_pos:
                for button in button_list:
                    if button.get_hitbox().collidepoint(x_pos, y_pos) and button.get_scene() == scene:
                        scene = button.set_clicked_true()
                        start = False
                        end[0] = False
                        end[1] = None

                        for letter in alphabet:
                            letter.set_status(-1)

                        for button in button_list:
                            button.set_clicked_false()

        elif scene == 4:

                if x_pos and y_pos:
                    for button in button_list:
                        if button.get_hitbox().collidepoint(x_pos, y_pos) and button.get_scene() == scene:
                            scene = button.set_clicked_true()
                            start = False
                            end[0] = False
                            end[1] = None

                            for letter in alphabet:
                                letter.set_status(-1)

                            for button in button_list:
                                button.set_clicked_false()


def render():

    global grid

    if scene == -1:
        quit()
    elif scene == 1:

        screen.fill((66, 135, 245))

        for text in text_list:
            if text.get_scene() == scene:
                text.render(screen)

        for button in button_list:
            if button.get_scene() == scene:
                button.render(screen)

    elif scene == 2:

        screen.fill((0, 0, 0))

        for text in text_list:
            if text.get_scene() == scene:
                text.render(screen)

        for button in button_list:
            if button.get_scene() == scene:
                button.render(screen)

        for letter in alphabet:
            letter.render(screen)

        grid.render(screen)

    elif scene == 3:

        screen.fill((21, 173, 54))

        for text in text_list:
            if text.get_scene() == scene:
                text.render(screen)

        for button in button_list:
            if button.get_scene() == scene:
                button.render(screen)

        grid.render_win(screen)

    elif scene == 4:

        screen.fill((105, 7, 12))

        for text in text_list:
            if text.get_scene() == scene:
                text.render(screen)

        for button in button_list:
            if button.get_scene() == scene:
                button.render(screen)

        grid.render_win(screen)


def main():

    global scene, start

    x_pos, y_pos = None, None

    while running:

        if not start and not end[0]:

            scene = 1

        elif start and not end[0]:

            scene = 2

        elif end[0] and end[1] == 'win':

            scene = 3
            x_pos = None
            y_pos = None

        elif end[0] and end[1] == 'lose':

            scene = 4
            x_pos = None
            y_pos = None

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if pygame.mouse.get_pressed()[0]:
                x_pos = pygame.mouse.get_pos()[0]
                y_pos = pygame.mouse.get_pos()[1]

            else:
                x_pos = None
                y_pos = None

        update(x_pos, y_pos)
        render()

        pygame.display.flip()


if __name__ == '__main__':
    main()
