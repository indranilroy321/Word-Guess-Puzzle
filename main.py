import pygame           # 1.
import pyautogui        # 2.
import string           # 3.3
import random           # 5
from pygame import mixer    # 15
import math                 # 17


class Keys:                                                                     # 3.1
    def __init__(self, scr, draw_start_pos_x, draw_start_pos_y, letter, source, color):        # 3.1
        self.color = color                                                # 3.1
        self.screen = scr                                                       # 3.1
        self.draw_start_pos_X = draw_start_pos_x                                # 3.1
        self.draw_start_pos_Y = draw_start_pos_y                                # 3.1
        self.letter = letter                                                    # 3.1
        self.width = tile_width                                                 # 3.1
        self.height = tile_height                                               # 3.1
        self.source = source                                                    # 12
        self.selected = False                                                   # 13

    def draw_key(self):                                                                                         # 3.2
        char_color = (255, 69, 0)     # Orange Red                                                              # 3.2
        char_adj_x, char_adj_y = 10, 10                                                                         # 3.2
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.draw_start_pos_X, self.draw_start_pos_Y, self.width,
                                                              self.height))                                     # 3.2
        if self.source == "keys":                                                                               # 12
            letter = key_font.render(str(self.letter), True, char_color)                                            # 3.2
            screen.blit(letter, (self.draw_start_pos_X + char_adj_x, self.draw_start_pos_Y + char_adj_y))           # 3.2


    def mouse_hover(self, x_m_motion, y_m_motion):
        if game_over == False:
            if x_m_motion > self.draw_start_pos_X and x_m_motion < self.draw_start_pos_X + self.width and y_m_motion > \
                    self.draw_start_pos_Y and y_m_motion < self.draw_start_pos_Y + self.height:                     # 11
                self.color = (255, 255, 255)                                                                        # 11
            else:                                                                                                   # 11
                # self.color = (255, 165, 0)                                                                          # 11
                self.color = (0, 255, 0)


    def change_key_color(self):                                                     # 13
        self.color = (255, 255, 255)                                                # 13


    def key_press(self, x_m_click_rel, y_m_click_rel):                                                          # 13
        global successful_guess_count, actual_attempt                                            # 15
        if self.selected == False:                                              # 15
            if x_m_click_rel > self.draw_start_pos_X and x_m_click_rel < self.draw_start_pos_X + self.width and y_m_click_rel > \
                    self.draw_start_pos_Y and y_m_click_rel < self.draw_start_pos_Y + self.height:                     # 13
                self.selected = True                                                                        # 13
                actual_attempt += 1
                # key_board_sound.play()
                # print(self.letter)                                                  # 14
                for j in range(len(match_board)):                                   # 14
                    if self.letter == match_board[j].letter:                        # 14
                        match_board[j].source = "keys"                              # 14
                        match_board[j].draw_key()                                   # 14
                        appearing_sound.play()                                      # 14
                        successful_guess_count += 1                                 # 15



def create_target_word(target_word):                                                       # 9
    # print("target_word: ", target_word)
    delim_width = 2                                                             # 9
    cell_start_x = 50                                                           # 9
    # cell_start_x = (tile_width + delim_width) * word_size                     # 9
    cell_start_y = 50                                                           # 9
    for letter in target_word:                                                  # 9
        k = Keys(screen, cell_start_x, cell_start_y, letter.upper(), "word", (238, 166, 245))            # 9     # 12
        match_board.append(k)                                                   # 9
        cell_start_x = cell_start_x + tile_width + delim_width                  # 9


def create_keys():                                                          # 3.3
    cell_start_x = 20                                                      # 3.3
    cell_start_y = 400                                                      # 3.3
    delim_width = 2                                                         # 3.3
    letter_count = 1                                                        # 3.3

    for letter in string.ascii_uppercase:                                   # 3.3
        k = Keys(screen, cell_start_x, cell_start_y, letter, "keys", (0, 255, 0))                # 3.3   # 12
        print(letter, end=" ")                                              # 3.3
        keyboard.append(k)                                                  # 3.3
        cell_start_x = cell_start_x + tile_width + delim_width              # 3.3
        if letter_count == 13:                                              # 3.3
            cell_start_y = cell_start_y + tile_height + delim_width         # 3.3
            cell_start_x = 20                                               # 3.3
        letter_count += 1                                                   # 3.3

                                                   # 7


def replay_mouse_hover(x_m_motion, y_m_motion):             # 16
    global cursor_on_replay                                 # 16
    if x_m_motion > replay_button_outer_x and x_m_motion < replay_button_outer_x + replay_button_length and y_m_motion > \
            replay_button_outer_y and y_m_motion < replay_button_outer_y + replay_button_width:  # 16
        cursor_on_replay = True                             # 16
    else:                                                   # 16
        cursor_on_replay = False                            # 16


def display_meaning():                                              # 10
    char_color = 255, 255, 0                                        # 10
    start_pos_x = 50                                                # 10
    start_pos_y = 200                                               # 10
    rest = meaning_font.render(rest_words, True, char_color)          # 10
    screen.blit(rest, (start_pos_x, start_pos_y))                 # 10


def get_distinct_chars(target_word):
    target_distinct = ""
    for i in range(0, len(target_word)):
        char_to_find = target_word[i]
        found = False
        for j in range(0, len(target_distinct)):
            if char_to_find.upper() == target_distinct[j].upper():
                found = True
                break
        if found == False:
            target_distinct = target_distinct + char_to_find
    print("get_distinct_chars: ", target_distinct)
    return target_distinct

def get_word():
    # global word_mean
    WORD_SIZE_RANGE = [4, 8]
    WORD_MEANING_RANGE = [40, 80]
    # target_distinct = ""                                            # 17
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))  # 5
    # print(randomUpperLetter)                                            # 5

    file_name = "Dictionary in csv/" + randomUpperLetter + "." + "csv"  # 6

    f = open(file_name, "r")  # 6
    max_line_no = 1  # 6
    for x in f:  # 6
        max_line_no += 1  # 6
    f.close()  # 6

    word_line = get_line_from_file(max_line_no, file_name)  # 7

    print("inside get_word: ", word_line)  # 7
    words = word_line.split()  # 8
    target_word = words[0].replace('"', "")  # 8
    word_size = len(target_word)  # 9

    print("outside loop", target_word, word_size, WORD_SIZE_RANGE[0], WORD_SIZE_RANGE[1])
    if word_size < WORD_SIZE_RANGE[0] or word_size > WORD_SIZE_RANGE[1] or (target_word.find('-') != -1):
        print("execute loop")
        # target_word = ""
        word_mean = get_word()
    else:
        # rest_words = word_line[len(target_word) + 1: ]
        #
        rest_words = word_line.replace(target_word, '').replace('"', '')  # 8
        rest_words = rest_words[0:len(rest_words) - 1]  # 8
        if len(rest_words) < WORD_MEANING_RANGE[0] or len(rest_words) > WORD_MEANING_RANGE[1]:
            word_mean = get_word()
        else:
            target_distinct = get_distinct_chars(target_word)               # 17
            print("target_distinct: ", target_distinct)
            word_mean = [target_word, rest_words, target_distinct]          # target_distinct is pushed later   # 18
        # return word_line                # 8

    print("word mean get_word: ", word_mean)
    return word_mean


def get_line_from_file(max_line_no, file_name):                                                   # 7
    # WORD_SIZE_RANGE = [4, 8]
    random_no = random.randint(1, max_line_no)                              # 7
    f = open(file_name, "r")                                                # 7
    line_no = 1                                                             # 7
    word_line = ""                                                          # 7

    for x in f:                                                             # 7
        if random_no == line_no:                                            # 7
            if x.strip() == '':                                             # 7
                # f.close()
                word_line = get_line_from_file(max_line_no, file_name)                            # 7
            else:                                                           # 7
                word_line = x                                               # 7
                break                                                       # 7
        line_no += 1                                                        # 7
    f.close()                                                               # 7
    print("get_line_from_file: ", len(word_line), word_line)                                        # 7
    # print("word_mean inside get_line_from_file: ", word_mean)
    return word_line

def replay(x_m_motion, y_m_motion, match_board):                                   # 16
    global rest_words, successful_guess_count, word_size, replay_ind, game_over, game_level, level_counter, \
        level_attempt, actual_attempt

    if x_m_motion > replay_button_outer_x and x_m_motion < replay_button_outer_x + replay_button_length and y_m_motion > \
            replay_button_outer_y and y_m_motion < replay_button_outer_y + replay_button_width:  # 16
        # print("replay_click")
        level_change_sound.play()
        replay_ind = True

        # print("match_board:", len(match_board))
        for j in range(len(match_board) - 1, -1, -1):
            # print(match_board[j].letter)
            del match_board[j]
        # match_board.clear()
        # print("after delete within replay")
        # for k in range(len(match_board)):
            # print(match_board[k].letter)
        word_mean = get_word()
        target_word = word_mean[0]
        rest_words = word_mean[1]
        target_distinct = word_mean[2]

        word_size = len(target_word)  # 9
        print("replay code: ", word_size, target_word)
        successful_guess_count = 0  # 15

        create_target_word(target_word)  # 16
        display_meaning()  # 16
        game_over = False

        for i in range(len(keyboard)):  # 3.4
            keyboard[i].selected = False  # 3.4

        game_level = 'EASY'  #
        level_counter = 0  #
        level_attempt = len(target_distinct) * 2  #
        actual_attempt = 0  #

        crowd_boo.stop()
        clapping_sound.stop()


def check_game_level(x_m_motion, y_m_motion):
    global level_easy_center, level_medium_center, level_hard_center, game_level, level_attempt, target_distinct
    level_det = ""
    d_easy = int(math.sqrt(pow((x_m_motion - level_easy_center[0]), 2) + pow((y_m_motion - level_easy_center[1]), 2)))
    d_medium = int(math.sqrt(pow((x_m_motion - level_medium_center[0]), 2) + pow((y_m_motion - level_medium_center[1]), 2)))
    d_hard = int(math.sqrt(pow((x_m_motion - level_hard_center[0]), 2) + pow((y_m_motion - level_hard_center[1]), 2)))
    min_dis = min([d_easy, d_medium, d_hard])
    if min_dis == d_easy and min_dis < level_circle_radius:
        level_det = "EASY"
        game_level = "EASY"
        level_attempt = len(target_distinct) * 2
        level_change_sound.play()
    elif min_dis == d_medium and min_dis < level_circle_radius:
        level_det = "MEDIUM"
        game_level = "MEDIUM"
        level_attempt = int(len(target_distinct) * 1.5)
        level_change_sound.play()
    elif min_dis == d_hard and min_dis < level_circle_radius:
        level_det = "HARD"
        game_level = "HARD"
        level_attempt = len(target_distinct)
        level_change_sound.play()

    print("distance: ", d_easy, d_medium, d_hard, "min_dis: ", min_dis, level_det, "level_attempt:", level_attempt)
    # return level_det


def show_game_level(screen):
    global game_level, level_counter
    pygame.draw.circle(screen, (255, 255, 255), level_easy_center, level_circle_radius, 0)  # 17   # outer
    pygame.draw.circle(screen, (255, 255, 255), level_medium_center, level_circle_radius, 0)  # 17   # outer
    pygame.draw.circle(screen, (255, 255, 255), level_hard_center, level_circle_radius, 0)  # 17   # outer

    if game_level == "EASY":
        pygame.draw.circle(screen, (0, 128, 0), level_easy_center, level_circle_radius - 5, 0)  # 17   # easy
        pygame.draw.circle(screen, (255, 165, 0), level_medium_center, level_circle_radius - 5, 0)  # 17     # medium
        pygame.draw.circle(screen, (250, 128, 114), level_hard_center, level_circle_radius - 5, 0)  # 17   # hard
        if level_counter % 3 == 0:
            screen.blit(level_easy, (965, 90))  # 17
        screen.blit(level_medium, (1070, 90))  # 17
        screen.blit(level_hard, (1200, 90))  # 17
    elif game_level == "MEDIUM":
        pygame.draw.circle(screen, (124, 252, 0), level_easy_center, level_circle_radius - 5, 0)  # 17   # easy
        pygame.draw.circle(screen, (255, 140, 0), level_medium_center, level_circle_radius - 5, 0)  # 17     # medium
        pygame.draw.circle(screen, (250, 128, 114), level_hard_center, level_circle_radius - 5, 0)  # 17   # hard

        screen.blit(level_easy, (965, 90))  # 17
        if level_counter % 3 == 0:
            screen.blit(level_medium, (1070, 90))  # 17
        screen.blit(level_hard, (1200, 90))  # 17
    elif game_level == "HARD":
        pygame.draw.circle(screen, (124, 252, 0), level_easy_center, level_circle_radius - 5, 0)  # 17   # easy
        pygame.draw.circle(screen, (255, 165, 0), level_medium_center, level_circle_radius - 5, 0)  # 17     # medium
        pygame.draw.circle(screen, (255, 0, 0), level_hard_center, level_circle_radius - 5, 0)  # 17   # hard

        screen.blit(level_easy, (965, 90))  # 17
        screen.blit(level_medium, (1070, 90))  # 17
        if level_counter % 3 == 0:
            screen.blit(level_hard, (1200, 90))  # 17

    level_counter += 1



def show_score(screen):
    screen.blit(score_board, (980, 180))  # 19
    actual_score_render = score_font.render(str(actual_attempt), True, (255, 0, 0))
    screen.blit(actual_score_render, (1085, 270))
    level_score_render = score_font.render(str(level_attempt), True, (255, 0, 0))
    screen.blit(level_score_render, (1110, 330))

# driver code

# page_width, page_depth = 800, 600                                 # 1.  # 2.
page_width, page_depth = pyautogui.size()                           # 2.
page_depth = int(page_depth * .95)                                  # 2.
tile_width, tile_height = 100, 100                                    # 3.1
keyboard = []                                                       # 3.3

pygame.init()           # 1.
screen = pygame.display.set_mode((page_width, page_depth))          # 1.
pygame.display.set_caption("Word Guess Puzzle")                     # 1.
key_font = pygame.font.Font('freesansbold.ttf', 100)               # 3.2
meaning_font = pygame.font.Font('freesansbold.ttf', 35)             # 10

create_keys()                                                       # 3.3

'''
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))         # 5
# print(randomUpperLetter)                                            # 5

file_name = "Dictionary in csv/" + randomUpperLetter + "." + "csv"      # 6

f = open(file_name, "r")                                            # 6
max_line_no = 1                                                     # 6
for x in f:                                                         # 6
    max_line_no += 1                                                # 6
f.close()                                                           # 6

word_line = get_line_from_file()                                    # 7
print(word_line)                                                    # 7
words = word_line.split()                                           # 8
'''
word_mean = get_word()
target_word = word_mean[0]
rest_words = word_mean[1]
target_distinct = word_mean[2]              # 18
# word_line = get_word()                  # 8
# words = word_line.split()               # 8
# target_word = words[0].replace('"', "")                             # 8
# rest_words = word_line[len(target_word) + 1: ]
# rest_words = word_line.replace(target_word, '')                      # 8
# rest_words = rest_words[0:len(rest_words) - 1]                      # 8
word_size = len(target_word)                                        # 9
print("driver code: ", word_size, target_word)                                       # 9
successful_guess_count = 0                                          # 15
image_scale_x, image_scale_y = 100, 100                                 # 15
image_scale_max_x, image_scale_max_y = 650, 650                     # 15
# for i in target_word:
    # print(i.upper())

# print(rest_words)
match_board = []                                                # 9
create_target_word(target_word)                                            # 9
display_meaning()                                               # 10

replay_button_outer_x = 600                             # 16
replay_button_outer_y = 625                             # 16
replay_button_length = 150                              # 16
replay_button_width = 50                                # 16
replay_font = pygame.font.Font('freesansbold.ttf', 35)              # 16
replay_print = replay_font.render("Replay", True, (215, 0, 64))     # 16
cursor_on_replay = False                                          # 16
game_over = False                                               # 15
player_status = "PLAYING"                                       # 18
trophy = pygame.image.load("trophy.png")                        # 15
trophy = pygame.transform.scale(trophy, (700, 700))
loser = pygame.image.load("loser.png")
loser = pygame.transform.scale(loser, (700, 650))
run_counter, run_counter_min, run_counter_max = 0, 10, 40          # 15
speed = 50                                                      # 15
clapping_sound = mixer.Sound('Clapping.mp3')                    # 15
appearing_sound = mixer.Sound('Appearing.mp3')                    # 14
level_change_sound = mixer.Sound('Dragging.mp3')
crowd_boo = mixer.Sound('long-boo.wav')
# key_board_sound = mixer.Sound('walther-p38-firing-sound-effect-11651.mp3')
replay_ind = False
level_font = pygame.font.Font('freesansbold.ttf', 25)              # 17
level_easy = level_font.render("EASY", True, (255, 255, 255))      # 17
level_medium = level_font.render("MEDIUM", True, (255, 255, 255))      # 17
level_hard = level_font.render("HARD", True, (255, 255, 255))      # 17
level_easy_center, level_medium_center, level_hard_center = [1000, 100], [1120, 100], [1240, 100]       # 17
level_circle_radius = 60                                                                                # 17
game_level = 'EASY'                                                                                     # 17
level_counter = 0                                                                                       # 17
level_attempt = len(target_distinct) * 2                                                                # 18
actual_attempt = 0                                                                                      # 18
score_board = pygame.image.load("score.png")                                                            # 19
score_font = pygame.font.Font('freesansbold.ttf', 60)                                                   # 19


running = True  # 1.

while running:  # 1.
    screen.fill((0, 0, 0))  # 1.

    pygame.draw.rect(screen, (0, 128, 128), pygame.Rect(replay_button_outer_x, replay_button_outer_y,
                                                        replay_button_length, replay_button_width)) # Teal # 16
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(603, 628, 144, 44))  # Cyan # 16
    if cursor_on_replay:  # 16
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(603, 628, 144, 44))  # Cyan # 16
    screen.blit(replay_print, (615, 635))                               # 16

    show_game_level(screen)
    show_score(screen)                          # 19

    for event in pygame.event.get():  # 1
        if event.type == pygame.QUIT:  # 1
            running = False  # 1

        if event.type == pygame.MOUSEMOTION:                            # 11
            x_m_motion, y_m_motion = pygame.mouse.get_pos()             # 11
            # print("mouse", X_m_motion, Y_m_motion)                    # 11
            for i in range(len(keyboard)):                              # 11
                keyboard[i].mouse_hover(x_m_motion, y_m_motion)         # 11
            replay_mouse_hover(x_m_motion, y_m_motion)

        if event.type == pygame.MOUSEBUTTONUP:                          # 13
            x_m_click_rel, y_m_click_rel = pygame.mouse.get_pos()       # 13
            if game_over == False:
                for i in range(len(keyboard)):                              # 13
                    keyboard[i].key_press(x_m_click_rel, y_m_click_rel)     # 13
                print("successful_guess_count:", successful_guess_count, "actual_attempt:", actual_attempt)
                # if word_size == successful_guess_count and game_over == False:  # 15   # 18 change of game over condition
                # if game_over == False:
                if actual_attempt <= level_attempt and word_size == successful_guess_count:
                    game_over = True  # 15
                    player_status = "WINNER"
                    clapping_sound.play()  # 14
                    print("game over", player_status)
                elif actual_attempt >= level_attempt and word_size != successful_guess_count:
                    game_over = True
                    player_status = "LOSER"
                    crowd_boo.play()
                    print("game over", player_status)                                      # 15

                check_game_level(x_m_motion, y_m_motion)

            replay(x_m_motion, y_m_motion, match_board)                              # 16


    for i in range(len(keyboard)):              # 3.4
        keyboard[i].draw_key()                  # 3.4

    for j in range(len(match_board)):           # 9
        match_board[j].draw_key()               # 9
        # if replay_ind:
            # print(match_board[j].letter)

    for k in range(len(keyboard)):                              # 13
        if keyboard[k].selected:                                # 13
            keyboard[k].change_key_color()                      # 13

    display_meaning()                           # 10
    '''
    if game_over and player_status == "WINNER":                               # 15
        run_counter += 1  # 15
        if run_counter > run_counter_min and run_counter < run_counter_max:   # 15
            screen.blit(trophy, (320, 15))  # 15

        if run_counter > speed:             # 15
            run_counter = 1                 # 15
    '''
    if game_over:
        run_counter += 1
        if run_counter > run_counter_min and run_counter < run_counter_max:
            if player_status == "WINNER":
                screen.blit(trophy, (320, 15))
            else:
                screen.blit(loser, (320, 15))

        if run_counter > speed:
            run_counter = 1

    pygame.display.flip()   # 3
pygame.display.update()  # 1




# 1. Create Game Window
# 2. Make Game Window Full Screen
# 3. Create Key Board
#   3.1 Create Key Class
#   3.2 Method for drawing key
#   3.3 Function for creating key objects
#   3.4 drawing keys on game window
# 4. get dictionary files in project
# 5. generate a random letter
# 6. Get line count in the file
# 7. get a random word from file
# 8. extract word and meaning
# 9. show target word
# 10. show word meaning
# 11. mouse hover
# 12. do not show word.
# 13. select key in keyboard
# 14. find letter in matchboard
# 15. game over
# 16. Replay
# 17. game level
# 18. winner/loser
# 19. score board


# issue
# 1. if word if found within meaning, then meaning is trancated
# 2. get a new word if meaning contains a numeric