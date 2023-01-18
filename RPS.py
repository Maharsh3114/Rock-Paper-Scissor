# <!-----------------------Rock,paper,scissors game-----------------!>

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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
if computer_choice == 2 and user_choice == 1:
    print("Computer choose",scissors)
    print("You choose",paper)
    print("Computer won")
    exit()

elif computer_choice == 1 and user_choice == 0:
    print("Computer choose",paper)
    print("You choose",rock)
    print("Computer won")
    exit()

elif computer_choice == 0 and user_choice == 2:
    print("Computer choose",rock)
    print("You choose",scissors)
    print("Computer won")
    exit()
elif computer_choice == 0 and user_choice == 1:
    print("Computer choose",rock)
    print("You choose",paper)
    print("You won")
    exit()
elif computer_choice == 1 and user_choice == 2:
    print("Computer choose",paper)
    print("You choose",scissors)
    print("You won")
    exit()
elif computer_choice == 2 and user_choice == 0:
    print("Computer choose",scissors)
    print("You choose",rock)
    print("You won")
    exit()
elif computer_choice == user_choice:
    # print("Computer choose",computer_choice)
    # print("You choose",user_choice)
    print("It's a Draw")
    exit()
