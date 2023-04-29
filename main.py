import mysql.connector
import time
connection = mysql.connector.connect(host = "localhost", user = "root", database = "sys", password = "Boopybozo8")

testQuery = ('SELECT * FROM BankDatabase')

cursor = connection.cursor(buffered=True)

def create_account():
    username = input('Create an account\nUsername: ').lower()
    password = input('Password: ').lower()
    cursor.execute(f"insert into BankDatabase (AccountName, AccountPassword) VALUES ('{username}', '{password}');")
    print('Success! Your account has been created!')
    return username, password

def log_in():
    passed = False
    while passed == False:
        usernameExisting = input('Sign in\nUsername: ').lower()
        passwordExisting = input('Password: ').lower()
        cursor.execute(f"select AccountPassword from BankDatabase where AccountName = '{usernameExisting}';")
        dataPass = cursor.fetchmany(size=1)
        dataPass = str(dataPass)
        passCheck = ""
        for i in dataPass:
            if i.isalpha():
                passCheck = "".join([passCheck, i])
        if passwordExisting == passCheck:
            print(f'Success! You have been logged in {usernameExisting}!')
            passed = True
        else:
            print('Your user information is incorrect.\nPlease try again.')
    return usernameExisting, passwordExisting

def delete_account(newUser, username, password, usernameExisting, passwordExisting):
    if newUser == True:
        cursor.execute(f"DELETE from BankDatabase where AccountName = '{username}' and AccountPassword = '{password}'")
        print('Your account has been deleted.\nYou have been signed out.\nPlease restart to sign into another account or create a new one!')
        quit()
    if newUser == False:
        cursor.execute(f"DELETE from BankDatabase where AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}'")
        print('Your account has been deleted.\nYou have been signed out.\nPlease restart to sign into another account or create a new one!')
        quit()

def check_balance(newUser, username, password,  usernameExisting, passwordExisting):
    if newUser == True:
        cursor.execute(f"select Balance from BankDatabase where AccountName = '{username}' and AccountPassword = '{password}'")
        money = cursor.fetchmany(size=1)
        money = str(money)
        removeList = ['[','(',',',')',']']
        for char in removeList:
            money = money.replace(char, "")
        print(f"Your current balance is: {money}")
    if newUser == False:
        cursor.execute(f"select Balance from BankDatabase where AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}'")
        moneyExisting = cursor.fetchmany(size=1)
        moneyExisting = str(moneyExisting)
        removeList = ['[','(',',',')',']']
        for char in removeList:
            moneyExisting = moneyExisting.replace(char, "")

        print(f"Your current balance is: {moneyExisting}")

def log_out():
    quit()

def modify_account(newUser, username, usernameExisting):
    if newUser == True:
        cursor.execute(f"select AccountPassword from BankDatabase where AccountName = '{username}';")
        dataPass = cursor.fetchmany(size=1)
        dataPass = str(dataPass)
        key = ""
        for i in dataPass:
            if i.isalpha():
                key = "".join([key, i])
        print(f"Your current password is {key}")
        newpass = input("Enter your new pasword: ")
        cursor.execute(f"update BankDatabase Set AccountPassword = '{newpass}' WHERE AccountName = '{username}';")
        print("Your new password has been set!\nPlease restart to sign back into your account.")
        quit()
    if newUser == False:
        cursor.execute(f"select AccountPassword from BankDatabase where AccountName = '{usernameExisting}';")
        dataPass = cursor.fetchmany(size=1)
        dataPass = str(dataPass)
        key = ""
        for i in dataPass:
            if i.isalpha():
                key = "".join([key, i])
        print(f"Your current password is {key}")
        newpass = input("Enter your new pasword: ")
        cursor.execute(f"update BankDatabase Set AccountPassword = '{newpass}' WHERE AccountName = '{usernameExisting}';")
        print("Your new password has been set!")
        print("Your new password has been set!\nPlease restart to sign back into your account.")
        quit()

def deposit(newUser, username, password,  usernameExisting, passwordExisting):
    depositedValue = float(input("How much money would you like to deposit?\nEnter value here: "))
    if newUser == True:
        cursor.execute(f"update BankDatabase Set Balance = {depositedValue} WHERE AccountName = '{username}' and AccountPassword = '{password}';")
        print("Your money has been deposited! Navigate to 'check balance' to view your current and updated balance!")
    if newUser == False:
        cursor.execute(f"select Balance from BankDatabase where AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}'")
        moneyExisting = cursor.fetchmany(size=1)
        moneyExisting = str(moneyExisting)
        removeList = ['[','(',',',')',']']
        for char in removeList:
            moneyExisting = moneyExisting.replace(char, "")
        moneyExisting = float(moneyExisting)
        totalMoney = depositedValue+moneyExisting
        cursor.execute(f"update BankDatabase Set Balance = {totalMoney} WHERE AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}';")
        print("Your money has been deposited! Navigate to 'check balance' to view your current and updated balance!")

def withdraw(newUser, username, password,  usernameExisting, passwordExisting):
    withdrawnValue = float(input("How much money would you like to withdraw?\nEnter value here: "))
    if newUser == True:
        currentMoney = cursor.execute(f"select Balance from BankDatabase where AccountName = '{username}' and AccountPassword = '{password}'")
        moneyCheck = cursor.fetchmany(size=1)
        moneyCheck = str(moneyCheck)
        removed = ['[','(',',',')',']']
        for char in removed:
            moneyCheck = moneyCheck.replace(char, "")
        if moneyCheck == None:
            print(f'If you withdraw {withdrawnValue} from your balance, you will get a negative value.\nPlease withdraw an acceptable amount from your balance.')
            print(f'You balance is: {moneyCheck}')
        else:
            cursor.execute(f"select Balance from BankDatabase where AccountName = '{username}' and AccountPassword = '{password}'")
            money = cursor.fetchmany(size=1)
            money = str(money)
            removeList = ['[','(',',',')',']']
            for char in removeList:
                money = money.replace(char, "")
            money = float(money)
            totalMoney = money-withdrawnValue
            if totalMoney < 0:
                print(f'If you withdraw {withdrawnValue} from your balance, you will get a negative value.\nPlease withdraw an acceptable amount from your balance.')
                print(f'You balance is: {money}')
            else:
                cursor.execute(f"update BankDatabase Set Balance = {totalMoney} WHERE AccountName = '{username}' and AccountPassword = '{password}';")
                print("Your money has been withrdawn! Navigate to 'check balance' to view your current and updated balance!")
    if newUser == False:
        cursor.execute(f"select Balance from BankDatabase where AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}'")
        moneyExisting = cursor.fetchmany(size=1)
        moneyExisting = str(moneyExisting)
        removeList = ['[','(',',',')',']']
        for char in removeList:
            moneyExisting = moneyExisting.replace(char, "")
        moneyExisting = float(moneyExisting)
        totalMoney = moneyExisting-withdrawnValue
        if totalMoney < 0:
            print(f'If you withdraw {withdrawnValue} from your balance, you will get a negative value.\nPlease withdraw an acceptable amount from your balance.')
            print(f'You balance is: {moneyExisting}')
        else:
            cursor.execute(f"update BankDatabase Set Balance = {totalMoney} WHERE AccountName = '{usernameExisting}' and AccountPassword = '{passwordExisting}';")
            print("Your money has been withrdawn! Navigate to 'check balance' to view your current and updated balance!")

def user_selection():
    print("""
-------------------------------
           * Bank *
-------------------------------
1. Check Balance ------------->
2. Deposit ------------------->
3. Withdraw ------------------>
4. Delete Account ------------>
5. Modify Account ------------>
6. Log Out ------------------->
-------------------------------
""")

    user_choice = int(input("Select an operation based on the number(1-6): "))

    if user_choice == 1:
        #DONE  
        print('Check Balance')
        check_balance(new, username, password, usernameExisting, passwordExisting)
    elif user_choice == 2: 
        #DONE
        print('Deposit')
        deposit(new, username, password, usernameExisting, passwordExisting)
    elif user_choice == 3:
        #DONE
        print("Withdraw")
        withdraw(new, username, password, usernameExisting, passwordExisting)
    elif user_choice == 4: 
        #DONE
        print('Delete Account')
        delete_account(new, username, password, usernameExisting, passwordExisting)
    elif user_choice == 5:
        #DONE
        print('Modify Account')
        modify_account(new, username, usernameExisting)
    elif user_choice == 6:
        #DONE
        print("Thank you for visting!")
        log_out()
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")

print('Welcome to the bank!')
done = False

username = ''
password = ''
usernameExisting = ''
passwordExisting = ''

while done == False:
    signOrCreate = input('Do you have an account? ')
    if (signOrCreate == 'yes') or (signOrCreate == 'Yes') or (signOrCreate == 'y'):
        new = False
        usernameExisting, passwordExisting = log_in()
        done = True
    elif (signOrCreate == 'no') or (signOrCreate == 'No') or (signOrCreate == 'n'):
        new = True
        username, password = create_account()
        done = True
    else:
        print("I'm sorry, that is not an acceptable answer. Try answering 'yes' or 'no'.")


while True:
    time.sleep(1)
    user_selection()
    cursor.execute(testQuery)
    connection.commit()