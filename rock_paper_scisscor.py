#rock,paper,scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You have eneted incorrect digit, Game Over")
else:
    print(game_images[user_choice])

    computer_choice=random.randint(0,2)
    print("Computer has choosen :")
    print(game_images[computer_choice])

    #game logic

    if user_choice==computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lost")
    elif user_choice > computer_choice:
        print("You Win")
    elif computer_choice > user_choice:
        print("you Lost")
