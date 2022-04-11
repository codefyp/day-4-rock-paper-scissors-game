#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
#player = 0

import random
computer = random.randint(0, 2)
#computer = 0
#print (computer)

if player == 0 and computer == 2 : 
 print (f"{rock} \n Computer chose: \n {scissors} \n You win!")

if player == 0 and computer == 1 : 
 print (f"{rock} \n Computer chose: \n {paper} \n You lose.")

if player == 2 and computer == 0 : 
 print (f"{scissors} \n Computer chose: \n {rock} \n You lose.")

if player == 1 and computer == 0 : 
 print (f"{paper} \n Computer chose: \n {rock} \n You win!")

if player == 1 and computer == 2 : 
 print (f"{paper} \n Computer chose: \n {scissors} \n You lose.")

if player == 2 and computer == 1 : 
 print (f"{scissors} \n Computer chose: \n {paper} \n You win!")

if player == 0 and computer == 0 : 
 print (f"{rock} \n Computer chose: \n {rock} \n It's a tie.")

if player == 1 and computer == 1 : 
 print (f"{paper} \n Computer chose: \n {paper} \n It's a tie.")

if player == 2 and computer == 2 : 
 print (f"{scissors} \n Computer chose: \n {scissors} \n It's a tie.")

else :
 print ("You've typed an invalid number.. You lose.")

#game_images = [rock, paper, scissors]

#user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#print(game_images[user_choice])

#computer_choice = random.randint(0, 2)
#print("Computer chose:")
#print(game_images[computer_choice])

#if user_choice >= 3 or user_choice < 0: 
#  print("You typed an invalid number, you lose!") 
#elif user_choice == 0 and computer_choice == 2:
#  print("You win!")
#elif computer_choice == 0 and user_choice == 2:
#  print("You lose")
#elif computer_choice > user_choice:
#  print("You lose")
#elif user_choice > computer_choice:
#  print("You win!")
#elif computer_choice == user_choice:
#  print("It's a draw")
