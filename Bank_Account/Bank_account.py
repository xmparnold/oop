# this class defines the Account object and its attributes and methods
class Account:
    # default attributes
    account_id = 0
    account_type = "Checking"
    account_blanace = 0
    interest_rate = .01
    # list of all accounts created
    list_accounts = []

    def __init__(self, account_type, starting_balance, interest_rate):
        # self.account_id = Account.list_accounts.length + 1
        self.account_type = account_type
        self.account_balanace = starting_balance
        # set interest rate to decimal by dividing by 100 to get the correct float value
        self.interest_rate = interest_rate / 100
        Account.list_accounts.append(self)
    
    # method to deposit money into account
    def deposit(self, amount):
        self.account_balanace += amount

    # method to withdraw from account
    def withdraw(self, amount):
        # make sure account has enough money for withdrawal
        if(self.account_balanace < amount): # if it doesnt, we will charge a $5.00 fee for insufficient funds
            print("Insufficient funds. Charging $5 fee")
            self.account_balanace -= 5
        else: # otherwise do the withdrawal
            self.account_balanace -= amount

    # method to display all account info of current instance
    def display_account_info(self):
        print( "Account Id:", self.account_id, "Account Type:", self.account_type, "Account Balance:", self.account_balanace, "Interest Rate:", self.interest_rate )

    # method to apply interest rate to current balance and increase balance by given result
    def yield_interest(self):
        if(self.account_balanace > 0): #make sure the account has money first
            self.account_balanace += ( self.account_balanace * self.interest_rate )

    # check the balance of current instance of account
    def check_balance(self):
        print("Account balance: $", self.account_balanace)


# define the user class
class User:
    # class attributes put here will be shared among all instances of the class
    bank_name = "First National Dojo"
    # array to hold all users that have been created
    list_users = []

    def __init__(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.accounts = [] # creating an array to hold all user's accounts
        self.accounts.append(Account("Checking", 0, 2)) # adding first default account with balance of 0
        # add self to the list of all users held in user class
        User.list_users.append(self) # add current instance of user to list of all users

    def print_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        # for loop to go through all user's accounts and get info
        for x in range(0,len(self.accounts),1):
            currentaccount = self.accounts[x]
            currentaccount.display_account_info()

    # method to add new accounts to a user
    def add_account(self, account_type, starting_balance, interest_rate):
        newaccount = Account(account_type, starting_balance, interest_rate)
        # add new account to the list of user's accounts
        self.accounts.append(newaccount)

    @classmethod
    def all_users( cls ):
        print("List of all bank users:")
        for User in cls.list_users:
            print(User.first_name, User.last_name, "Bank name:", User.bank_name)

    @classmethod
    def change_bank_name(cls, new_bank):
        for User in cls.list_users:
            User.bank_name = new_bank

    # static methods are basically functions that do not need to access any instances of the class or the class attributes to make changes, though objects can be passed through the parameters to be used in static methods
    @staticmethod
    def add_two_numbers( num1, num2):
        return num1 + num2

# james = User("James", "Charles", "asdf@gmail.com")
# john = User("John", "Andrews", "asdfds@gmail.com")

# User.all_users()
# User.change_bank_name("New Bank")
# User.all_users()

# newaccount = Account( "Checking", 10, 4 )
# newaccount.display_account_info()
# newaccount.deposit(10)
# newaccount.display_account_info()
# newaccount.yield_interest()
# newaccount.display_account_info()
# newaccount.withdraw(5)
# newaccount.display_account_info()
# newaccount.withdraw(1000)
# newaccount.display_account_info()

newuser = User("Mark", "Andrews", "asdfds@gmail.com")
newuser.print_info()
newuser.add_account("Checking", 100, 2)
newuser.print_info()
newuser.accounts[0].deposit(300)
newuser.print_info()
newuser.accounts[0].check_balance()