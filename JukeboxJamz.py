# This is the python Jukebox simulation
# Corey Hollins

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

######### Player Setup #########
class player:
    def __init__(self):
        self.name = ''
        self.change = 0
        self.bonus = 0
        self.location = 'Start'
myPlayer = player()

###### Title Screen #######

def title_screen_selections():
    option = input(">")
    if option.lower() ==("play"):
        start_game() #place holder
    elif option.lower() == ("help"):
        help.menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enger a valid command.")
        option = input("> ")
        if option.lower() ==("play"):
            start_game() #place holder
        elif option.lower() == ("help"):
            help.menu()
        elif option.lower() == ("quit"):
            sys.exit()

    def title_screen():
        os.sync('clear')
        print('################################')
        print('# Welcome to the Jukebox Diner #')
        print('################################')
        print('             - Play -           ')
        print('             - Help -           ')
        print('             - Quit -           ')
        print('     Copyright 2020 MrBallinz   ')
        print('################################')
        title_screen_selections()

    def help_menu():
        print('###################################')
        print('#   Welcome to the Jukebox Diner  #')
        print('###################################')
        print('- Use up, down, left, right to move')
        print('- Type your commands to do them    ')
        print('- Type "next" to skip song         ')
        print('- Type "back" to go previous song  ')
        print('###################################')
        title_screen_selections()
####### Game functionality #######
    def start_game():

####### Map #######
"""
a1 a2... #player starts at b2
-----
| | |
-----
| | | b2...
-----
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }
zonemap = {
    'a1': {
        ZONENAME: "At the Jukebox",
        DESCRIPTION = 'Your at the classic jukebox filled with some of the most classic hits'
        EXAMINATION = 'You see a coin slot. it reads "10 cents per song" you see a forward and back button to select song'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'b1'
        LEFT = 'left', 'west'
        RIGHT = 'a2'
    },
        'a2': {
        ZONENAME: "At the Booth",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
        'b1': {
        ZONENAME: "Inside the Diner",
        DESCRIPTION = 'This is the Jukebox diner'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
        'b2': {
        ZONENAME: "Outside the Jukebox Diner",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a2'
        DOWN = ''
        LEFT = 'b1'
        RIGHT = 'right', 'east'
    },
}