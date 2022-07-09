# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 01:02:53 2022

@author: Mohamed
"""

import PySimpleGUI as sg
import random

# Initializing the wins of each player
computer_wins = 0
player_wins = 0
draws = 0

# Initializing the list of legal moves
moves = ['Rock', 'Paper', 'Scissors']      

# Setting the application GUI up
sg.theme('DarkAmber')

layout = [[sg.Text("Let's Play Rock Paper Scissors!")],      
          [sg.Text("Pick an option to play!")],
          # This could be improved by using a for loop to add a button for each 
          [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors'), sg.Button('Exit')],
          [sg.Text("", key='winner')],
          [sg.Text("Player wins: "), sg.Text(player_wins, key='player_wins'), sg.Text("Draws: "), sg.Text(draws, key='draws'), sg.Text("Computer wins: "), sg.Text(computer_wins, key='computer_wins')]]      

window = sg.Window('Rock, Paper, Scissors!', layout)


# The main application
while True:                             # To run the application indefinitely or until the game is closed

    #Initialize the window
    event, values = window.read() 
    print(event, values)    

    # Close the game
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # Play the game
    else:
        computer_choice = moves[random.randint(0, 2)]
        user_input = event
        
        # If both the computer and player chose the same move
        if user_input == computer_choice:
            window['winner'].update("You Drew!")
            draws += 1
            window['draws'].update(draws)
            continue
        
        # Player chooses rock against Scissors
        if user_input == moves[0] and computer_choice == moves[2]:
            window['winner'].update("You won!")
            player_wins += 1
            window['player_wins'].update(player_wins)
            continue
        
        # Player chooses paper against rock        
        elif user_input == moves[1] and computer_choice == moves[0]:
            window['winner'].update("You won!")
            player_wins += 1
            window['player_wins'].update(player_wins)
            continue
        
        # Player chooses scissors against paper
        elif user_input == moves[2] and computer_choice == moves[1]:
            window['winner'].update("You won!")
            player_wins += 1
            window['player_wins'].update(player_wins)
            continue
        
        # Player loses every other scenario
        else:
            window['winner'].update("Computer won!")
            computer_wins += 1
            window['computer_wins'].update(computer_wins)
            continue
        

window.close()