class Bank:
    def __init__(self, name, branch) -> None:
        self.name = name
        self.branch = branch
        self.accounts = {}
        self.admin = None
        self.is_loan_available = True

    def add_account(self, account):
        ac_no = 1000 + len(self.accounts) + 1
        account.account_number = ac_no
        self.accounts[ac_no] = account

    def add_admin(self, admin):
        self.admin = admin

    def user_login(self, name, password):
        for ac in self.accounts:
            print(ac)
            if name == self.accounts[ac].name and password == self.accounts[ac].password:
                return self.accounts[ac]
            
        return None

    def admin_login(self, name, password):
        if name == self.admin.name and password == self.admin.password:
            return self.admin
        else:
            print('\nInvalid Name and Password!')