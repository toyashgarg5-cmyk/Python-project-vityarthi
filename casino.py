import random
casino_cash = 10000000
while True:
    bet_amount = int(input(f"Enter the amount you want to bet(limit:{casino_cash}): "))
    if bet_amount <= casino_cash:
        break
    else:
        print("Invalid bet amount, try again")
        continue
while True:
    roll = random.randint(1, 6)
    bet = int(input("bet your amount on the roll of dice\n pick a number between 1 to 6: "))
    if bet == roll:
        casino_cash = casino_cash - bet_amount
        bet_amount = bet_amount * 2
        print("You won your bet amount is doubled")
        print(f"Your current Balance is {bet_amount}")
        while True:
            x = input("Do you want to continue betting?(y/n): ")
            if x == "y":
                while True:
                    reply = input("do you want to change the bet amount(y/n): " )
                    if reply == "y":
                        while True:
                            wit_des = input("would you like to withdraw or deposit?(w/d): ")
                            if wit_des == "w":
                                print(f"max amount that can be withdrawn is: {bet_amount - 1}")
                                while True:
                                    wit_amt = int(input("Enter the amount you want to withdraw: "))
                                    if wit_amt < bet_amount:
                                        bet_amount = bet_amount - wit_amt
                                        break
                                    else:
                                        print("Invalid amount!, try again")
                                        continue
                                break
                            elif wit_des == "d":
                                print(f"max amount that can be deposit is: {casino_cash - bet_amount}")
                            
                                while True:
                                    des_amt = int(input("Enter the amount you want to deposit: "))
                                    if des_amt < bet_amount:
                                        bet_amount = bet_amount + des_amt
                                        break
                                    else:
                                        print("Invalid amount!, try again")
                                        continue
                                break
                            else:
                                print("Invalid response!, try again")
                                continue

                    elif reply == "n":
                        break
                    else:
                        print("Invalid response!, try again")
                        continue
            
                break
            elif x == "n":
                break
            else:
                print("Invalid response! try again")
                continue
        if x == "n":
            break
        else:
            continue
    elif bet != roll:
        casino_cash = casino_cash + bet_amount
        bet_amount = bet_amount * 0
        print("You lost!")
        print(f"Your current Balance is {bet_amount}")
        while True:
            x = input("Do you want to continue betting?(y/n): ")
            if x == "y":
                 print("Your current balance is 0")
                 while True:
                    added_amnt = int(input(f"Add amount(limit:{casino_cash}): "))
                    if added_amnt <= casino_cash:
                        break
                    else:
                        print("Invalid amount, try again")
                        continue

                 bet_amount = bet_amount + added_amnt
                 
                 break
            elif x == "n":
                break
            else:
                print("Invalid response! try again")
                continue
        if x == "n":
            break
        else:
            continue



