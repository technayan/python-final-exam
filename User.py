from Bank import Bank

class Person:
    def __init__(self, name) -> None:
        self.name = name

class User(Person):
    def __init__(self, name, email, password, address, account_type) -> None:
        super().__init__(name)
        self.email = email
        self.password = password
        self.address = address
        self.account_type = account_type
        self.__balance = 0
        self.account_number = None
        self.__remain_loan_no = 2
        self.is_bankrupt = False
        self.transaction_history = []
        self.__loan = 0

    @property
    def balance(self):
        return self.__balance
    
    @property
    def loan(self):
        return self.__loan
    
    @property
    def is_bankrupt(self):
        return self.__is_bankrupt
    
    @is_bankrupt.setter
    def is_bankrupt(self, value):
        self.__is_bankrupt = value

    def check_balance(self):
        print(f'\nAvailable Balance: {self.balance}tk')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f'Deposit         : {amount}tk')
            print(f'\n{amount}tk has deposited to your account.')
        else:
            print(f'\nNot enough money to deposit!')
    
    def withdraw(self, amount):
        if self.__is_bankrupt == False:
            if amount <= self.__balance:
                self.__balance -= amount
                self.transaction_history.append(f'Withdraw        : {amount}tk')
                print(f'\n{amount}tk has withdrawn from your account.')
            else:
                print('\nWithdrawal amount exceeded.')
        else:
            print('\nThe bank is bankrupt.')

    def check_transaction_history(self):
        print('\nTransection History:')
        print('----------------------')
        for history in self.transaction_history:
            print(history)

    def take_loan(self, bank, amount):
        if self.__is_bankrupt == False:
            if bank.is_loan_available == True:
                if self.__remain_loan_no > 0:
                    self.__balance += amount
                    self.__loan += amount
                    self.transaction_history.append(f'Loan            : {amount}tk')
                    self.__remain_loan_no -= 1
                    print(f'\nLoan of {amount}tk has taken.')
                else:
                    print('\nYour have taken loan maximum(2) times.')
            else:
                print('\nLoan feature is disabled')
        else:
            print('\nThe bank is bankrupt.')

    def transfer_amount(self, bank, account_no, amount):
        if self.__is_bankrupt == False:
            if amount <= self.__balance:
                if account_no in bank.accounts:
                    self.__balance -= amount
                    bank.accounts[account_no].__balance += amount
                    self.transaction_history.append(f'Transfer Amount : {amount}tk to AC_No: {account_no}')
                    history = f'Received Amount : {amount}tk from AC_No: {self.account_number}'
                    bank.accounts[account_no].transaction_history.append(history)
                    print(f'\n{amount}tk has transfered to Account No: {account_no}')
                else:
                    print('\nAccount does not exist.')
            else:
                print('\nNot enough money to transfer.')
        else:
            print('\nThe bank is bankrupt.')

    
        
class Admin(Person):
    def __init__(self, name, password) -> None:
        super().__init__(name)
        self.password = password

    def delete_account(self, bank, account_no):
        if account_no in bank.accounts:
            # bank.accounts[account_no].remove()
            bank.accounts.pop(account_no)
            print(f'\nAccount No: {account_no} has deleted')
        else:
            print('\nAccount does not exist.')
    
    def check_accounts(self, bank):
        print('\nAll Accounts: ')
        for account in bank.accounts:
            print(f'Ac No: {bank.accounts[account].account_number},     Name: {bank.accounts[account].name},     Balance: {bank.accounts[account].balance}tk')
            
    
    def total_bank_balance(self, bank):
        total = 0
        for account in bank.accounts:
            total += bank.accounts[account].balance
        print(f'\nTotal Bank Balance: {total}tk')

    def total_loan_amount(self, bank):
        total = 0
        for account in bank.accounts:
            total += bank.accounts[account].loan
        print(f'\nTotal Bank Loan Amount: {total}tk')

    def off_loan_feature(self, bank):
        bank.is_loan_available = False
        print('\nTurned OFF loan feature')

    def on_loan_feature(self, bank):
        bank.is_loan_available = True
        print('\nTurned ON loan feature')

    def make_account_bankrupt(self, bank, account_no):
        if account_no in bank.accounts:
            bank.accounts[account_no].is_bankrupt = True
            print(f'\nAccount No: {account_no} became bankrupt')
        else:
            print('\nAccount does not exist.')


