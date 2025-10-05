print("               TO DO LIST               ")
task=[]
while True:
    print(" 1.Add Task          ","    2.View Tasks")
    print(" 3.Remove Task        ","   4.Exit\n")
    print(" Enter your choice  :")
    
    user_choice=input()

    if user_choice=="1":
        add=input("Add Task: \n")
        task.append(add)
        print("   ----     Task Added    ----    \n")
    
    elif user_choice=="2":
        print("      ----      View      ----     \n",task,"\n")
        
    elif user_choice=="3":
        remove=input("Remove Task: \n")
        task.remove(remove)
        print("    ----    Task Removed     ----    \n")
    
    elif user_choice=="4":
        print("    ----    Come Again     ----    \n")
        exit()
    
    else:
        print("\nPlease enter your choice\n")
    
    