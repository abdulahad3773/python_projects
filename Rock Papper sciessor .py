import random

while True:

    choice = ["rock", "paper", "scissor"]
    comp_choice = random.choice(choice)
    user_choice = input("Enter Rock Paper Scissor or N to quit").lower()
    
    if user_choice == "n":
        break

    elif user_choice == "rock" and comp_choice == "rock":
        result = "Tie"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "rock" and comp_choice == "paper":
        result = "Comp Win"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "rock" and comp_choice == "scissor":
        result = "You Won"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "paper" and comp_choice == "rock":
        result = "You Win"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")

    elif user_choice == "paper" and comp_choice == "scissor":
        result = "Comp Won"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "paper" and comp_choice == "paper":
        result = "Tie"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "scissor" and comp_choice == "scissor":
        result = "Tie"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "scissor" and comp_choice == "paper":
        result = "You  Win"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    elif user_choice == "scissor" and comp_choice == "rock":
        result = "comp Win"
        print(f"you choose {user_choice} and computer choose {comp_choice} so {result}")
    else:
        print("enter valid option")
