import random
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

alphabet = []
for x in range(10):
    alphabet.append(LetterButton(chr(x + 65), 125 + (x * 50), 550))
for y in range(10, 19):
    alphabet.append(LetterButton(chr(y + 65), 150 + ((y - 10) * 50), 600))
for z in range(19, 26):
    alphabet.append(LetterButton(chr(z + 65), 200 + ((z - 19) * 50), 650))

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
            index_last_blank = 0

            while user_types:

                if user_input[len(user_input) - 1] == '':
                    index_last_blank = user_input.index('')
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

                        elif event.key == pygame.K_BACKSPACE:
                            if not flag:
                                user_input[index_last_blank - 1] = ''
                            else:
                                user_input[4] = ''
                                flag = False
                        elif not flag and event.unicode.isalpha():
                            user_input[index_last_blank] = event.unicode.upper()
                            print(user_input)

                for square in grid.get_current_row():
                    square.insert_letter(user_input[square.get_col()])

                if not user_types:

                    user_input = ['', '', '', '', '']

                    if grid.check_row(alphabet):
                        end[0] = True
                        end[1] = 'win'

                    if grid.change_row():
                        end[0] = True
                        end[1] = 'lose'

                if pygame.mouse.get_pressed()[0]:
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]

                else:
                    x_pos = None
                    y_pos = None

                if x_pos and y_pos:
                    for button in button_list:
                        if button.get_hitbox().collidepoint(x_pos, y_pos) and button.get_scene() == scene:
                            scene = button.set_clicked_true()

                    for letter in alphabet:

                        if letter.is_clicked():
                            if not letter.get_hitbox().collidepoint(x_pos, y_pos):
                                letter.set_clicked_false()

                        if letter.get_hitbox().collidepoint(x_pos, y_pos):
                            if not flag and not letter.is_clicked():
                                user_input[index_last_blank] = letter.get_letter()
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

        if not start:

            scene = 1

        elif start and not end[0]:

            scene = 2

        elif end[0] and end[1] == 'win':

            scene = 3

        elif end[0] and end[1] == 'lose':

            scene = 4

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
