class Bank_Account:
    def __init__(self):
        print("*******Opening a bank account*********")
        self.Account_Name = input("Enter Account Name: ")
        self.Account_Number = int(input("Enter Account Number: "))
        self.Account_Available_Amount = float(input("Enter Available Amount(Initital deposit): \n"))
    def display_info(self):
        print("Account Holder Name:", self.Account_Name)
        print("Account Number:", self.Account_Number)
        print("Account Available Amount ", self.Account_Available_Amount)
    def withdrawl(self):
        withdrawl_amount = float(input("Enter amount to witdhdrawl: "))
        if withdrawl_amount <= self.Account_Available_Amount:
            self.Account_Available_Amount = self.Account_Available_Amount - withdrawl_amount
            print(withdrawl_amount, "has been debited from", str(self.Account_Number)+".", "Current Balance is", self.Account_Available_Amount, '\n')
        else:
            print("Entered amount is more than yur funds")
    def deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Account_Available_Amount += deposit_amount
        print(deposit_amount, "has credited in", str(self.Account_Number)+".", "Avialable balance is", self.Account_Available_Amount, '\n')

b1 =  Bank_Account()
b1.display_info()
b1.withdrawl()