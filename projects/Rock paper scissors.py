import random
user_choice=int(input("enter your choice: type 0 for rock, 1 for paper, 2 for scissors: "))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number, you lose")
computer_choice=random.randint(0,2)
print("computer choose:")
print("computer_choice")

if computer_choice==user_choice:
    print("it is a draw")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
