# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:19:39 2022

@author: Mohamed
"""

import random

player_wins = 0
computer_wins = 0

moves = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper or Scissors to play, or Q to quit: ").lower()
    if user_input == "q":
        print("computer wins: ", computer_wins, ", Your wins: ", player_wins)
        break
        
    if user_input not in moves:
        print("That is not a valid input")
        continue
    else:
        computer_choice = moves[random.randint(0, 2)]
        print("Computer picked ", computer_choice + " ")
        
    if user_input == computer_choice:
        print("You Drew!")
        continue
    
    if user_input == moves[0] and computer_choice == moves[2]:
        print("You won!")
        player_wins += 1
        continue
    
    elif user_input == moves[1] and computer_choice == moves[0]:
        print("You won!")
        player_wins += 1
        continue
    
    elif user_input == moves[2] and computer_choice == moves[1]:
        print("You won!")
        player_wins += 1
        continue
    
    else:
        print("Computer won!")
        computer_wins += 1
        continue
        
        
        