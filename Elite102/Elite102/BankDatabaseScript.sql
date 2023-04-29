#insert into BankDatabase (AccountName, AccountPassword, Balance) VALUES ('jim', 'hello', 50);
#Add account


#select Balance from BankDatabase where AccountName = 'jim'
#Check Balance

Update BankDatabase
set Balance = Balance-20
where AccountName = 'jim'

#DELETE from BankDatabase where AccountName = 'rohan'
#Delete account

