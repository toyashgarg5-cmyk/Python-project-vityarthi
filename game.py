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
        while True:      
            x = input ("Would you like to play again?").title()
            if x == "Yes":
                break
            elif x == "No":
                break   
            else:
                print("Invalid response, try again") 
        if x == "No":
            break


    elif user_choice == "paper":
        if computer_choice == "paper":
            print ("It's a TIE")
        elif computer_choice == "rock":
            print ("Paper covers Rock, YOU WIN")
        else:
            print ("Scissor cuts paper, YOU LOOSE") 
        while True:
            x = input ("Would you like to play again?").title()
            if x == "Yes":
                break  
            elif (x== "No"):
                break
            else:
                print("invalid response, try again") 
                continue
        if x =="No":
            break

    elif user_choice == "scissor":
        if computer_choice == "paper":
            print ("Scissor cuts paper, YOU WIN")
        elif computer_choice == "scissor":
            print ("It's a TIE")
        else:
            print ("Rock smashes scissor, YOU LOOSE")   
        while True:
            x = input ("Would you like to play again?").title()
            if x == "Yes":
                break
            elif x == "No":
                break
            else:
                print("Invalid response, try again")
        if x == "No":
            break

    else:
        print ("Wrong input, try again!")
        continue
