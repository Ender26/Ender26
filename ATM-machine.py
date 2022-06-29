import time

def ATM_Machine():
    repeats = 3
    money = 100

    while True :
        print(" ")
        print("Welcome to our ATM Machine")
        print(" ")
        username = input("Please enter your username: ")
        print(" ")
        password = input("Please enter your password: ")


        if username == "Todor"  :
            if password == "Todor":
                    print(" ")
                    print("****************")
                    print("*Hello Todor!!!*")
                    print("****************")
                    time.sleep(1)
                    print( "Your balance is ", money)

                    choice = input("Would you like to check how much money you have , withdraw or deposit: ")

                    if choice == "Withdraw" or choice == "withdraw" :
                        withdraw = int(input("How much money would you like to withdraw: "))

                        if withdraw > money :
                            print("Error: You cannot withdraw more money than you have")
                            returnBeginint = input("Press Enter to return")
                            print(" ")
                            continue

                        while repeats > 0:
                            print("Working.")

                            time.sleep(1)
                            print("Working..")
                            time.sleep(1)

                            print("Working...")
                            time.sleep(1)
                            repeats-=1

                        money -= withdraw
                        print("Done, now you have " , money , "$ in your bank accout")
                    else :

                        if choice == "Deposit" or choice == "deposit":
                            indraw = int(input("How much money would you like to indraw: "))

                            while repeats > 0:
                                print("Working.")
                                time.sleep(1)

                                print("Working..")
                                time.sleep(1)

                                print("Working...")
                                time.sleep(1)
                                repeats-=1

                            money += indraw
                            print("Done, now you have " , money , "$ in your bank account")
                        else:
                            if choice == "Check" or "check":
                                print(" ")
                                print("You have " , money , "$ in your bank account")

                    repeats = 3
                    returnBeginint = input("Press anything to continue ")
                    print(" ")
                    continue
            else :
                print("Wrong password")
                print(" ")
                time.sleep(1)

        else :
            print("Wrong username")
            print(" ")
            time.sleep(1)
ATM_Machine()