import mysql.connector
connection = mysql.connector.connect(user = "root", database = "sys", password = "Boopybozo8")

testQuery = ('SELECT * FROM BankDatabase')

cursor = connection.cursor()

print('Welcome to the bank!')
signOrCreate = input('Do you have an account? ')

if (signOrCreate == 'yes') or (signOrCreate == 'Yes') or (signOrCreate == 'y'):
    usernameExisting = input('Sign in: ')
if (signOrCreate == 'no') or (signOrCreate == 'No') or (signOrCreate == 'n'):
    print('Create an account:')

cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()

connection.close()