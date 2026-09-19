import random
item_list = ["rock", "paper", "scissor"]

computer_choice = random.choice(item_list)


while True:
    user_choice = input ("Enter your move = Rock, Paper or Scissor = ").lower()
    print ("User choice =", user_choice, "; computer choice =", computer_choice)
    if user_choice == "rock":
        if computer_choice == "paper":
            print ("Paper covers rock, YOU LOOSE")
        elif computer_choice == "rock":
            print ("It's a TIE")
        else:
            print ("Rock smashes Scissor, YOU WIN")        
        x = input ("Would you like to play again?").title()
        if x == "Yes":
            continue   
        else:
            break 


    elif user_choice == "paper":
        if computer_choice == "paper":
            print ("It's a TIE")
        elif computer_choice == "rock":
            print ("Paper covers Rock, YOU WIN")
        else:
            print ("Scissor cuts paper, YOU LOOSE") 
        x = input ("Would you like to play again?").title()
        if x == "Yes":
            continue  
        else:
            break 

    elif user_choice == "scissor":
        if computer_choice == "paper":
            print ("Scissor cuts paper, YOU WIN")
        elif computer_choice == "scissor":
            print ("It's a TIE")
        else:
            print ("Rock smashes scissor, YOU LOOSE")   
        x = input ("Would you like to play again?").title()
        if x == "Yes":
            continue
        else:
            break

    else:
        print ("Wrong input, try again!")
        continue
