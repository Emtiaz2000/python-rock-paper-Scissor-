# rock paper scissure game

#importing random
import random
computer_pick = random.randint(0,3)#random intiger 
game_elements=["rock",'paper','scissor']#list
user_input=input('Select Rock Paper or Scissure ') #user input
user_input = user_input.lower() #making user input to lowerCase

#Check if the user entered the right word
if user_input == 'rock' or user_input == 'paper' or user_input == 'scissor':
    #user entered the entered right word
    if user_input == game_elements[computer_pick]:
        print("Draw!")
        print(game_elements[computer_pick] )
        print(user_input )
    elif user_input == "scissor" and game_elements[computer_pick] =='rock':
        print('OOps you loss!')
        print(game_elements[computer_pick] )
    elif user_input == "rock" and game_elements[computer_pick] =='paper':
        print('OOps you loss!')
        print(game_elements[computer_pick] )
    elif user_input == "paper" and game_elements[computer_pick] =='scissor':
        print('OOps you loss!')
        print(game_elements[computer_pick] )
    else:
        print('You win!')
        print(game_elements[computer_pick] )
else:#user entered wrong word
    print("You have to Choose Rock Paper or Seissure!")
