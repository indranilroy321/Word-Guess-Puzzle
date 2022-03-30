import pygame           
import pyautogui        
import string           
import random           
from pygame import mixer    
import math                 


class Keys:                                                                     
    def __init__(self, scr, draw_start_pos_x, draw_start_pos_y, letter, source, color):        
        self.color = color                                                
        self.screen = scr                                                       
        self.draw_start_pos_X = draw_start_pos_x                                
        self.draw_start_pos_Y = draw_start_pos_y                                
        self.letter = letter                                                    
        self.width = tile_width                                                 
        self.height = tile_height                                               
        self.source = source                                                    
        self.selected = False                                                   

    def draw_key(self):                                                                                         
        char_color = (255, 69, 0)     # Orange Red                                                              
        char_adj_x, char_adj_y = 10, 10                                                                         
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.draw_start_pos_X, self.draw_start_pos_Y, self.width,
                                                              self.height))                                     
        if self.source == "keys":                                                                               
            letter = key_font.render(str(self.letter), True, char_color)                                            
            screen.blit(letter, (self.draw_start_pos_X + char_adj_x, self.draw_start_pos_Y + char_adj_y))           


    def mouse_hover(self, x_m_motion, y_m_motion):
        if game_over == False:
            if x_m_motion > self.draw_start_pos_X and x_m_motion < self.draw_start_pos_X + self.width and y_m_motion > \
                    self.draw_start_pos_Y and y_m_motion < self.draw_start_pos_Y + self.height:                     
                self.color = (255, 255, 255)                                                                        
            else:                                                                                                                                                                                      
                self.color = (0, 255, 0)


    def change_key_color(self):                                                     
        self.color = (255, 255, 255)                                                


    def key_press(self, x_m_click_rel, y_m_click_rel):                                                          
        global successful_guess_count, actual_attempt                                            
        if self.selected == False:                                              
            if x_m_click_rel > self.draw_start_pos_X and x_m_click_rel < self.draw_start_pos_X + self.width and y_m_click_rel > \
                    self.draw_start_pos_Y and y_m_click_rel < self.draw_start_pos_Y + self.height:                     
                self.selected = True                                                                        
                actual_attempt += 1
                                                     
                for j in range(len(match_board)):                                   
                    if self.letter == match_board[j].letter:                        
                        match_board[j].source = "keys"                              
                        match_board[j].draw_key()                                   
                        appearing_sound.play()                                      
                        successful_guess_count += 1                                 



def create_target_word(target_word):                                                       
    
    delim_width = 2                                                             
    cell_start_x = 50                                                           
                       
    cell_start_y = 50                                                           
    for letter in target_word:                                                  
        k = Keys(screen, cell_start_x, cell_start_y, letter.upper(), "word", (238, 166, 245))            
        match_board.append(k)                                                   
        cell_start_x = cell_start_x + tile_width + delim_width                  


def create_keys():                                                          
    cell_start_x = 20                                                      
    cell_start_y = 400                                                      
    delim_width = 2                                                         
    letter_count = 1                                                        

    for letter in string.ascii_uppercase:                                   
        k = Keys(screen, cell_start_x, cell_start_y, letter, "keys", (0, 255, 0))               
        print(letter, end=" ")                                              
        keyboard.append(k)                                                  
        cell_start_x = cell_start_x + tile_width + delim_width              
        if letter_count == 13:                                              
            cell_start_y = cell_start_y + tile_height + delim_width         
            cell_start_x = 20                                               
        letter_count += 1                                                   

                                                   
def replay_mouse_hover(x_m_motion, y_m_motion):             
    global cursor_on_replay                                 
    if x_m_motion > replay_button_outer_x and x_m_motion < replay_button_outer_x + replay_button_length and y_m_motion > \
            replay_button_outer_y and y_m_motion < replay_button_outer_y + replay_button_width:  
        cursor_on_replay = True                             
    else:                                                   
        cursor_on_replay = False                            


def display_meaning():                                              
    char_color = 255, 255, 0                                        
    start_pos_x = 50                                                
    start_pos_y = 200                                               
    rest = meaning_font.render(rest_words, True, char_color)          
    screen.blit(rest, (start_pos_x, start_pos_y))                 


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
    
    WORD_SIZE_RANGE = [4, 8]
    WORD_MEANING_RANGE = [40, 80]
                                            
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))  
                                          
    file_name = "Dictionary in csv/" + randomUpperLetter + "." + "csv"  

    f = open(file_name, "r")  
    max_line_no = 1  
    for x in f:  
        max_line_no += 1  
    f.close()  

    word_line = get_line_from_file(max_line_no, file_name)  

    print("inside get_word: ", word_line)  
    words = word_line.split()  
    target_word = words[0].replace('"', "")  
    word_size = len(target_word)  

    print("outside loop", target_word, word_size, WORD_SIZE_RANGE[0], WORD_SIZE_RANGE[1])
    if word_size < WORD_SIZE_RANGE[0] or word_size > WORD_SIZE_RANGE[1] or (target_word.find('-') != -1):
        print("execute loop")
      
        word_mean = get_word()
    else:

        rest_words = word_line.replace(target_word, '').replace('"', '')  
        rest_words = rest_words[0:len(rest_words) - 1]  
        if len(rest_words) < WORD_MEANING_RANGE[0] or len(rest_words) > WORD_MEANING_RANGE[1]:
            word_mean = get_word()
        else:
            target_distinct = get_distinct_chars(target_word)               
            print("target_distinct: ", target_distinct)
            word_mean = [target_word, rest_words, target_distinct]          
        

    print("word mean get_word: ", word_mean)
    return word_mean


def get_line_from_file(max_line_no, file_name):                                                   
    
    random_no = random.randint(1, max_line_no)                              
    f = open(file_name, "r")                                                
    line_no = 1                                                             
    word_line = ""                                                          

    for x in f:                                                             
        if random_no == line_no:                                            
            if x.strip() == '':                                             
                
                word_line = get_line_from_file(max_line_no, file_name)                            
            else:                                                           
                word_line = x                                               
                break                                                       
        line_no += 1                                                        
    f.close()                                                               
    print("get_line_from_file: ", len(word_line), word_line)                                        
    
    return word_line

def replay(x_m_motion, y_m_motion, match_board):                                   
    global rest_words, successful_guess_count, word_size, replay_ind, game_over, game_level, level_counter, \
        level_attempt, actual_attempt

    if x_m_motion > replay_button_outer_x and x_m_motion < replay_button_outer_x + replay_button_length and y_m_motion > \
            replay_button_outer_y and y_m_motion < replay_button_outer_y + replay_button_width:  
        
        level_change_sound.play()
        replay_ind = True

        
        for j in range(len(match_board) - 1, -1, -1):
            
            del match_board[j]

        word_mean = get_word()
        target_word = word_mean[0]
        rest_words = word_mean[1]
        target_distinct = word_mean[2]

        word_size = len(target_word)  
        print("replay code: ", word_size, target_word)
        successful_guess_count = 0  

        create_target_word(target_word)  
        display_meaning()  
        game_over = False

        for i in range(len(keyboard)):  
            keyboard[i].selected = False  

        game_level = 'EASY'  
        level_counter = 0  
        level_attempt = len(target_distinct) * 2  
        actual_attempt = 0  

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
    


def show_game_level(screen):
    global game_level, level_counter
    pygame.draw.circle(screen, (255, 255, 255), level_easy_center, level_circle_radius, 0)     # outer
    pygame.draw.circle(screen, (255, 255, 255), level_medium_center, level_circle_radius, 0)    # outer
    pygame.draw.circle(screen, (255, 255, 255), level_hard_center, level_circle_radius, 0)     # outer

    if game_level == "EASY":
        pygame.draw.circle(screen, (0, 128, 0), level_easy_center, level_circle_radius - 5, 0)    # easy
        pygame.draw.circle(screen, (255, 165, 0), level_medium_center, level_circle_radius - 5, 0)       # medium
        pygame.draw.circle(screen, (250, 128, 114), level_hard_center, level_circle_radius - 5, 0)     # hard
        if level_counter % 3 == 0:
            screen.blit(level_easy, (965, 90))  
        screen.blit(level_medium, (1070, 90))  
        screen.blit(level_hard, (1200, 90))  
    elif game_level == "MEDIUM":
        pygame.draw.circle(screen, (124, 252, 0), level_easy_center, level_circle_radius - 5, 0)     # easy
        pygame.draw.circle(screen, (255, 140, 0), level_medium_center, level_circle_radius - 5, 0)       # medium
        pygame.draw.circle(screen, (250, 128, 114), level_hard_center, level_circle_radius - 5, 0)     # hard

        screen.blit(level_easy, (965, 90))  
        if level_counter % 3 == 0:
            screen.blit(level_medium, (1070, 90))  
        screen.blit(level_hard, (1200, 90))  
    elif game_level == "HARD":
        pygame.draw.circle(screen, (124, 252, 0), level_easy_center, level_circle_radius - 5, 0)     # easy
        pygame.draw.circle(screen, (255, 165, 0), level_medium_center, level_circle_radius - 5, 0)       # medium
        pygame.draw.circle(screen, (255, 0, 0), level_hard_center, level_circle_radius - 5, 0)     # hard

        screen.blit(level_easy, (965, 90))  
        screen.blit(level_medium, (1070, 90))  
        if level_counter % 3 == 0:
            screen.blit(level_hard, (1200, 90))  

    level_counter += 1



def show_score(screen):
    screen.blit(score_board, (980, 180))  
    actual_score_render = score_font.render(str(actual_attempt), True, (255, 0, 0))
    screen.blit(actual_score_render, (1085, 270))
    level_score_render = score_font.render(str(level_attempt), True, (255, 0, 0))
    screen.blit(level_score_render, (1110, 330))

# driver code

# page_width, page_depth = 800, 600                                
page_width, page_depth = pyautogui.size()                         
page_depth = int(page_depth * .95)                                 
tile_width, tile_height = 100, 100                                 
keyboard = []                                                      

pygame.init()          
screen = pygame.display.set_mode((page_width, page_depth))         
pygame.display.set_caption("Word Guess Puzzle")                    
key_font = pygame.font.Font('freesansbold.ttf', 100)              
meaning_font = pygame.font.Font('freesansbold.ttf', 35)           

create_keys()                                                     


word_mean = get_word()
target_word = word_mean[0]
rest_words = word_mean[1]
target_distinct = word_mean[2]              

word_size = len(target_word)                                        
print("driver code: ", word_size, target_word)                                      
successful_guess_count = 0                                          
image_scale_x, image_scale_y = 100, 100                                 
image_scale_max_x, image_scale_max_y = 650, 650                     

match_board = []                                                
create_target_word(target_word)                                            
display_meaning()                                               

replay_button_outer_x = 600                            
replay_button_outer_y = 625                            
replay_button_length = 150                             
replay_button_width = 50                              
replay_font = pygame.font.Font('freesansbold.ttf', 35)              
replay_print = replay_font.render("Replay", True, (215, 0, 64))    
cursor_on_replay = False                                         
game_over = False                                              
player_status = "PLAYING"                                      
trophy = pygame.image.load("trophy.png")                       
trophy = pygame.transform.scale(trophy, (700, 700))
loser = pygame.image.load("loser.png")
loser = pygame.transform.scale(loser, (700, 650))
run_counter, run_counter_min, run_counter_max = 0, 10, 40         
speed = 50                                                    
clapping_sound = mixer.Sound('Clapping.mp3')                   
appearing_sound = mixer.Sound('Appearing.mp3')                  
level_change_sound = mixer.Sound('Dragging.mp3')
crowd_boo = mixer.Sound('long-boo.wav')

replay_ind = False
level_font = pygame.font.Font('freesansbold.ttf', 25)            
level_easy = level_font.render("EASY", True, (255, 255, 255))     
level_medium = level_font.render("MEDIUM", True, (255, 255, 255))    
level_hard = level_font.render("HARD", True, (255, 255, 255))      
level_easy_center, level_medium_center, level_hard_center = [1000, 100], [1120, 100], [1240, 100]      
level_circle_radius = 60                                                                               
game_level = 'EASY'                                                                                    
level_counter = 0                                                                                      
level_attempt = len(target_distinct) * 2                                                                
actual_attempt = 0                                                                                     
score_board = pygame.image.load("score.png")                                                           
score_font = pygame.font.Font('freesansbold.ttf', 60)                                                   


running = True 

while running:  
    screen.fill((0, 0, 0))  

    pygame.draw.rect(screen, (0, 128, 128), pygame.Rect(replay_button_outer_x, replay_button_outer_y,
                                                        replay_button_length, replay_button_width)) # Teal 
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(603, 628, 144, 44))  # Cyan 
    if cursor_on_replay:  
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(603, 628, 144, 44))  # Cyan 
    screen.blit(replay_print, (615, 635))                               

    show_game_level(screen)
    show_score(screen)                          

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False 

        if event.type == pygame.MOUSEMOTION:                            
            x_m_motion, y_m_motion = pygame.mouse.get_pos()             
                            
            for i in range(len(keyboard)):                              
                keyboard[i].mouse_hover(x_m_motion, y_m_motion)        
            replay_mouse_hover(x_m_motion, y_m_motion)

        if event.type == pygame.MOUSEBUTTONUP:                          
            x_m_click_rel, y_m_click_rel = pygame.mouse.get_pos()       
            if game_over == False:
                for i in range(len(keyboard)):                              
                    keyboard[i].key_press(x_m_click_rel, y_m_click_rel)     
                print("successful_guess_count:", successful_guess_count, "actual_attempt:", actual_attempt)

                if actual_attempt <= level_attempt and word_size == successful_guess_count:
                    game_over = True 
                    player_status = "WINNER"
                    clapping_sound.play()  
                    print("game over", player_status)
                elif actual_attempt >= level_attempt and word_size != successful_guess_count:
                    game_over = True
                    player_status = "LOSER"
                    crowd_boo.play()
                    print("game over", player_status)                                     

                check_game_level(x_m_motion, y_m_motion)

            replay(x_m_motion, y_m_motion, match_board)                              

    for i in range(len(keyboard)):              
        keyboard[i].draw_key()                  

    for j in range(len(match_board)):           
        match_board[j].draw_key()              

    for k in range(len(keyboard)):                              
        if keyboard[k].selected:                                
            keyboard[k].change_key_color()                      

    display_meaning()                           

    if game_over:
        run_counter += 1
        if run_counter > run_counter_min and run_counter < run_counter_max:
            if player_status == "WINNER":
                screen.blit(trophy, (320, 15))
            else:
                screen.blit(loser, (320, 15))

        if run_counter > speed:
            run_counter = 1

    pygame.display.flip()   
pygame.display.update()  




