# File created by: Ivan Vikingstad

# GOALS FOR FINAL GAME PROJECT: Interactive visual RPS game; Goals, Rules, Feedback, Freedom 

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# setup asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)


cpu_choice = ""
# game settings
WIDTH = 600
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 255, 255)
BLUE = (255, 255, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")
clock = pg.time.Clock()

# sounds
scissors_sound = pg.mixer.Sound(os.path.join(game_folder, "scissors.wav"))

original_rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
original_paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
original_scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()

rock_image = pg.transform.smoothscale(original_rock_image, (200, 150))
paper_image = pg.transform.smoothscale(original_paper_image, (200, 150))
scissors_image = pg.transform.smoothscale(original_scissors_image, (200, 150))


# creates transparency 
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)

# gets the geometry of the image
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect.y = HEIGHT/2
scissors_rect.x = WIDTH/2

user_choice = ""
game_started = False

choices0 = ["rock","paper","scissors"]

def cpu_choice():
    return choices0[randint(0,2)]
    # return "The computer has chosen " + choices0[randint(0,2)]
# print(choices[randint(0,2)])


# user choices and options win/loose/tie
# setting variable of result
def compare(user_choice):
    cpu = cpu_choice()
    print("The computer chose", cpu)
    if user_choice == cpu:
        print("Tie!!")
        result = "Tie"
    elif user_choice == "rock":
        if cpu == "scissors":
            print("You win!")
            result = "The computer chose scissors, YOU WIN!!!"
        elif cpu == "paper":
            print("You lose!")
            result = "The computer chose paper, YOU LOSE!!!"
    elif user_choice == "paper":
        if cpu == "scissors":
            print("You lose!")
            result = "The computer chose scissors, YOU LOSE!!!"
        elif cpu == "rock":
            print("You win!")
            result = "The computer chose rock, YOU WIN!!!"
    elif user_choice == "scissors":
        if cpu == "rock":
            print("You lose!")
            result = "The computer chose rock, YOU LOSE!!!"
        elif cpu == "paper":
            print("You win!")
            result = "The computer chose paper, YOU WIN!!!"
    else:
        print("This is the last thing that will happen if nothing else is true.")

    # background = black
    screen.fill(BLACK)

    font = pg.font.SysFont('timesnewroman',  30)
    resulttext = font.render(result, True,  pg.Color(BLUE))
    resulttextRect = resulttext.get_rect()
    resulttextRect.center = (300, 200)

    screen.blit(resulttext, resulttextRect)

# defines where the user clicked and what outcome this will result in
def find_collision(mouse_coords):
    if rock_rect.collidepoint(mouse_coords):
        print("You clicked on rock")
        choice = "rock"
    elif paper_rect.collidepoint(mouse_coords):
        print("You clicked on paper")
        choice = "paper"
    elif scissors_rect.collidepoint(mouse_coords):
        print("You clicked on scissors")
        choice = "scissors"
        pg.mixer.Sound.play(scissors_sound)
    else:
        print("You clicked on nothing...")
    # if mouse_coords[0] <= 300 and mouse_coords[1] <= 300:
    # # if mouse_coords == pg.mouse.get_pos():
    #     print("I clicked on the rock...")
    compare(choice)

# draws the text boxes and the "rectangles" in which they are in. Also sets different x/y coordinates for the rectangles that determine where they will lie on the screen. 
def draw_rps():
    rock_rect.y = 150
    rock_rect.x = 110
    paper_rect.y = 150
    paper_rect.x = 360
    scissors_rect.y = 320
    scissors_rect.x = 200

    screen.blit(scissors_image, scissors_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(rock_image, rock_rect)

running = True

# background = black again 
screen.fill(BLACK)

# yes/no button at the start of the game and their outcomes
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            if game_started == False and yesRect.collidepoint(mouse_coords):
                print("start game")
                game_started = True
                screen.fill(BLACK)
                draw_rps()
            elif game_started == False and noRect.collidepoint(mouse_coords):
                print("close game")
                pg.quit()
            elif game_started == True:
                find_collision(mouse_coords)
            # print(mouse_coords)
            # print(mouse_coords[0])
            # print(mouse_coords[1])

# option to start the game or not, determines whether or not to display the images in the second stage of the game
    if game_started == False:
        font = pg.font.SysFont('timesnewroman',  30)
        title = font.render('Would you like to play rock paper scissors?', True,  pg.Color(WHITE))
        titleRect = title.get_rect()
        titleRect.center = (300, 200)

        font = pg.font.SysFont('timesnewroman',  30)
        yes = font.render('YES', True,  pg.Color(GREEN))
        yesRect = yes.get_rect()
        yesRect.center = (300, 300)

        font = pg.font.SysFont('timesnewroman',  30)
        no = font.render('NO', True,  pg.Color(RED))
        noRect = no.get_rect()
        noRect.center = (300, 400)

        screen.blit(title, titleRect)
        screen.blit(yes, yesRect)
        screen.blit(no, noRect)
    # updates what is on the display 
    pg.display.flip()
# quits the program
pg.quit()