import random
print("               Start Game               ")
print("          ROCK PAPER SCISSOR            ")

options=["rock","paper","scissor"] 
u_win=0
c_win=0
tie=0
while True:
    user_choice=input("Enter your choice(rock,paper,scissor)  ").lower()
    
    if user_choice not in options:
        print("Please choose rock,paper,scissor  ")
        continue
    
    computer_choice=random.choice(options)
    
    print(f"user choice:     {user_choice}")
    print(f"computer choice: {computer_choice}")
    
    if user_choice==computer_choice:
        print("              TIE              ")
        tie +=1
        
    elif(user_choice=="paper" and computer_choice=="rock") \
    or(user_choice=="rock" and computer_choice=="scissor") or (user_choice=="scissor" and computer_choice=="paper"):
        print("            YOU WIN            ")
        u_win +=1
    
    else:
        print("            YOU LOSE            ")
        c_win +=1
    
    
    while True:
        p_again=input("Want to play again? y or n: ").lower()
        if p_again=="n":
            print()
            print("  Win  ",u_win)
            print("  Lose ",c_win)
            print("  Tie  ",tie,"\n")
            exit()
        elif p_again=="y":
            break
        else:
            print("          Please choose y or n         ")
            continue
 
        
         
     

   
    
