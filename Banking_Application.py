# Author: Ronan Roche
# This program gives the user the possibility to choose between 6 different banking options and performs a different task for each function.
# I have reused functions that I created during the labs and uploaded 2 other python files that contain the these functions.
# For example I used the get house name function from the harry potter exercise for the get option function in this project.
# I also used the function read_score from the GAA exercise, for the function that gets the amount of money in this project.
import random

def creating_three_lists(file): # Seperating the data in the bank.txt file into three different lists
    account_number_list = []    # Creating three empty lists
    balance_list = []
    name_list = []

    while True:
        line = file.readline() # read one line
        if line == "":  # if the line is empty, then break from the loop
            break
        line_list = line.split()
        account_number_list.append(int(line_list[0]))    # first index is account numbers
        balance_list.append(float(line_list[1]))   # second index is balance
        name_list.append(line_list[2:])  # third index is the name

    return account_number_list, balance_list, name_list

def get_option():   # Asking the user what he/she wants to do
    # Printng all the options possible
    print("1. Open an account\n2. Close an account\n3. Withdraw money\n4. Deposit money\n5. Generate a report for management\n6. Quit\n")
    # Getting an option from the user
    ok = False
    while ok == False:
        try:
            option = int(input("Enter a number between 1 and 6: "))
            if 1 <= option <= 6:
                ok = True
            else:
                print("Please select one of the options listed above.")
        except:
            print("Invalid input - Please enter a number between 1 and 6")

    return option

def get_account_number(account_number_list):    # Getting an account numebr from the user and checking its existence in the list
    ok = False
    while ok == False:
        try:
            account_number = int(input("\nPlease enter your account number: "))
            for i in account_number_list:
                if account_number == i:
                    ok = True
            if ok == False:
                print("We are sorry but your account does not exist - Please try again")
        except:
            print("Invalid input - Please enter a positive 6-digit number")

    return account_number

def get_amount_of_money_to_withdraw_or_deposit(balance_list):   # Getting an amount of money from the user
    ok = False
    while ok == False:
        try:
            amount_of_money = float(input("Please enter the amount of money you would like to withdraw/deposit: "))
            if amount_of_money >= 0.00:
                ok = True
            else:
                print("Please enter positive number")
        except:
            print("Invalid input - Please try again")
    return amount_of_money

def open_account(account_number_list, balance_list, name_list):
    # Getting user's full name
    new_user_full_name = [] # Creating an empty list for the new user's name
    ok = False
    while ok == False:
        try:
            new_user_first_name = input("\nPlease enter your first name: ")
            new_user_last_name = input("Please enter your last name: ")
            if len(new_user_first_name) > 2 and len(new_user_last_name) > 2 and new_user_first_name.isalpha() and new_user_last_name.isalpha():
                ok = True
            else:
                print("Please enter your first and last names.(They must be more than 2 characters long)")
        except:
            print("Invalid input - Please try again")

    new_user_full_name.append(new_user_first_name)  # Appending the first and last names to the empty list above
    new_user_full_name.append(new_user_last_name)
    new_user_balance = 0.00 # Balance for a new user is €0.00
    new_number = random.randint(100000, 999999) # Creating a random 6 digit number

    loop_count = 0  # count for while loop
    while loop_count < len(account_number_list):    # While the loop count is less than the length of the list of account numbers
        if new_number != account_number_list[loop_count]:  # If the new number is not in the list, then keep going through the list
            loop_count += 1
        else:   # If the new number is already in the list, then reset the loop count to 0 and create a new random number
            loop_count = 0
            new_number = random.randint(100000, 999999)

    # Appending the name, the balance and the account number to the correct lists
    account_number_list.append(new_number)
    balance_list.append(new_user_balance)
    name_list.append(new_user_full_name)

    print("\nThank you for opening an account with us.")
    print("Your Account Number is: ", new_number, " and your current Balance is: €", format(new_user_balance, ".2f"), sep="")

    return account_number_list, balance_list, name_list # Returning the lists

def close_account(account_number_list, balance_list, name_list):
    account_number = get_account_number(account_number_list) # Getting the account number from the user
    account_position = account_number_list.index(account_number) # Finding the position of the account number in the list

    # Using the accounts position to delete items from each list, in order to delete the full account
    del account_number_list[account_position], balance_list[account_position], name_list[account_position]
    print("Your account has been successfully closed")

    return account_number_list, balance_list, name_list  # Returning the lists

def withdraw_money(account_number_list, balance_list):
    account_number = get_account_number(account_number_list)   # Getting account number from the user
    account_position = account_number_list.index(account_number)    # Getting the position of the account number in the list

    ok = False
    while ok == False:
        try:
            amount_of_money_to_withdraw = get_amount_of_money_to_withdraw_or_deposit(balance_list) # Asking to the user how much many to withdraw
            if amount_of_money_to_withdraw > balance_list[account_position]:
                print("We are sorry but you do not have sufficient funds in your account.")
                print("Please withdraw a smaller amount or withdraw €0.00 to continue")
            elif amount_of_money_to_withdraw <= balance_list[account_position]:
                ok = True
        except:
            print("Invalid input - Please try again")
    new_balance = balance_list[account_position] - amount_of_money_to_withdraw  # Removing the amount asked from the current balance
    balance_list[account_position] = new_balance    # Replacing the old balance with the new one
    print("Your new balance in your account is : €", format(new_balance, ".2f"), sep="")

    return account_number_list, balance_list

def deposit_money(account_number_list, balance_list):
    account_number = get_account_number(account_number_list)   # Getting the account number from the user
    account_position = account_number_list.index(account_number)    # Getting the position of the account number in the list

    amount_of_money_to_deposit = get_amount_of_money_to_withdraw_or_deposit(balance_list)# Asking to the user how much money to deposit
    new_balance = balance_list[account_position] + amount_of_money_to_deposit  # Removing the amount asked from the actual balance
    balance_list[account_position] = new_balance    # Replacing the old balance with the new one
    print("Your new balance in your account is : €", format(new_balance, ".2f"), sep="")

    return account_number_list, balance_list

def generate_report_for_management(account_number_list, balance_list, name_list):
    largest_balance_account_holder = "" # Creating an empty string
    total_balance = sum(balance_list)   # Adding all the balances in the list together
    largest_balance = max(balance_list) # Finding the highest balance in the list

    print(format("\nAccount number", "20s"), format("Name", "30s"), "Balance")    # Printing column names
    for i, number in enumerate(balance_list):   # Creating a loop
        full_name = name_list[i][0] + " " + name_list[i][1] # The [0] and [1] are the first and last names respectively of each list(the names list is a list of lists, where each list contains a full name)
        print(format(str(account_number_list[i]), "20s"), format(full_name, "30s"), " ", format(balance_list[i], ".2f"), sep="")   # Printing each person's details
        if number == largest_balance:   # If the balance in the list equals the largest balance, then you add the person's details to the empty string created above
            largest_balance_account_holder += str(account_number_list[i]) + " " + full_name + "\n"

    print("\nTotal Balance: €", format(total_balance, ".2f"), sep="")
    print("Largest Balance: €", largest_balance, sep="")
    print("Holder(s):\n", largest_balance_account_holder, sep="")

def quit(account_number_list, balance_list, name_list):
    update_file = open("RonanRoche-bank.txt", "w") # Writing over the file
    for i in range(len(account_number_list)):   # Creating a loop
        update_file.write(str(account_number_list[i]) + " " + str(format(balance_list[i], ".2f") + " " + name_list[i][0] + " " + name_list[i][1] + "\n"))   # Rewriting the file with the updated lists
    update_file.close() # Closing the file

def main():
    file = open("RonanRoche-bank.txt") # Opening the bank text file
    account_number_list, balance_list, name_list = creating_three_lists(file) # Divide the file's content into three lists
    option = get_option()   # Getting an option from the user

    while True: # Creating a loop
        if option == 1: # Call a different function for every option
            open_account(account_number_list, balance_list, name_list)
        elif option == 2:
            close_account(account_number_list, balance_list, name_list)
        elif option == 3:
            withdraw_money(account_number_list, balance_list)
        elif option == 4:
            deposit_money(account_number_list, balance_list)
        elif option == 5:
            generate_report_for_management(account_number_list, balance_list, name_list)
        elif option == 6:
            quit(account_number_list, balance_list, name_list)
            break   # Quits the loop only if option 6 is chosen

        print("")
        print("What would you like to do next?")
        option = get_option()

main()