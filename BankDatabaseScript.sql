#insert into BankDatabase (AccountName, AccountPassword, Balance) VALUES ('jim', 'hello', 50);
#Add account
#select Balance from BankDatabase where AccountName = 'john';
#update BankDatabase Set Balance = Balance+10 where AccountName = 'john';
#select Balance from BankDatabase where AccountName = 'john';

select Balance from BankDatabase where AccountName = 'mz' and AccountPassword = 'mz';

#update BankDatabase
#Set Balance = 10.00
#where AccountName = 'john';



#where AccountName = 'jim'
#Withdraw

#Update BankDatabase
#set Balance = Balance+50
#where AccountName = 'jim'
#Deposit

#DELETE from BankDatabase where AccountName = 'rohan'
#Delete account

#select AccountPassword from BankDatabase where AccountName = 'jim'