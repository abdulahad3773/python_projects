import random

while True:    
    num=[]
    for i in range(1,101):
        num.append(i)
    c_choice=random.choices(num)
    comp_choice=c_choice[0]
    count=0
    for i in range(5):
        user_input=int(input("enter you number from 1 -100"))
        if user_input == comp_choice:
            print("You win" )
            count+=1
            break
        elif user_input>comp_choice:
            print("chose a smaller num")
        elif user_input<comp_choice:
            print("choose a bigger number ")
        else:
            print("enter a valid number")
    print("the number you have to guess was",comp_choice)
    if count==0:
        print("You Lose")
    
    again_play=input(print("Do you Want to play again Y/N")).lower()
    if again_play!="y":
        break
    


