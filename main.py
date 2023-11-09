from Bank import Bank
from User import User, Admin

def main():
    # Creating Bank
    bank = Bank('Programming Bank', 'Tongi')
    
    # Create Admin
    admin = Admin('Admin', '1234')
    bank.add_admin(admin)

    current_user = None
    
    while (True):
        print('\n============================')
        print(f'Welcome to {bank.name}')
        print('============================')

        if current_user == None:
            print('\n No user logged in.')

            ch = input('\nLogin / Registration? (L/R): ')
            # Registration
            if ch == 'R':
                name = input('Name: ')
                email = input('Email: ')
                password = input('Password: ')
                address = input('Address: ')
                a_t = input('Savings or Current? (S/C): ')

                if a_t == 'S':
                    account_type = 'Savings'
                    user = User(name, email, password, address, account_type)
                    bank.add_account(user)
                    current_user = user
                elif a_t == 'C':
                    account_type = 'Current'
                    user = User(name, email, password, address, account_type)
                    bank.add_account(user)
                    current_user = user
                else:
                    print('\nWrong Account Type! Please, select "S" or "C"')

            
            # Login
            elif ch == 'L':
                user_type = input('User or Admin login? (U/A): ')
                # User Login
                if user_type == 'U':
                    name = input('Name: ')
                    password = input('Password: ')
                    current_user = bank.user_login(name, password)
                    if current_user == None:
                        print('\nInvalid Name and Password!')
                
                # Admin Login
                elif user_type == 'A':
                    name = input('Name: ')
                    password = input('Password: ')
                    current_user = bank.admin_login(name, password)
                
                else: 
                    print('\nWrong user type! Please, select "U" or "A"')

            else:
                print('\nWrong Option selected! Please, select "L" or "R"')

        else:
            if current_user.name == 'Admin':
                print(f'\nHello {current_user.name}.\n')
            else:
                print(f'\nHello {current_user.name}. | Account No: {current_user.account_number}\n')

            # Admin Options
            if current_user.name == 'Admin':
                print('1. Create an Account')
                print('2. Delete an User Account')
                print('3. Check All Accounts')
                print('4. Check Total Available Balance of the Bank')
                print('5. Check Total Loan Amount')
                print('6. Turn OFF Loan Feature')
                print('7. Turn ON Loan Feature')
                print('8. Make Account Bankrupt')
                print('9. Log Out')
                print('10. Exit')

                ch = input('Choose Option: ')

                if ch == '1':
                    name = input('Name: ')
                    email = input('Email: ')
                    password = input('Password: ')
                    address = input('Address: ')
                    a_t = input('Savings or Current? (S/C): ')
                    if a_t == 'S':
                        account_type = 'Savings'
                        user = User(name, email, password, address, account_type)
                        bank.add_account(user)
                    elif a_t == 'C':
                        account_type = 'Current'
                        user = User(name, email, password, address, account_type)
                        bank.add_account(user)
                    else:
                        print('\nWrong Account Type! Please, select "S" or "C"')

                elif ch == '2': 
                    acc_no = int(input('Account No: '))
                    admin.delete_account(bank, acc_no)

                elif ch == '3':
                    admin.check_accounts(bank)

                elif ch == '4':
                    admin.total_bank_balance(bank)

                elif ch == '5':
                    admin.total_loan_amount(bank)

                elif ch == '6':
                    admin.off_loan_feature(bank)

                elif ch == '7':
                    admin.on_loan_feature(bank)

                elif ch == '8':
                    ac_no = int(input('Account No: '))
                    admin.make_account_bankrupt(bank, ac_no)

                elif ch == '9':
                    current_user = None

                elif ch == '10':
                    break

                else:
                    print('Wrong Option Choosen. Please, choose between 1 to 10')

            # User Options
            else:
                print('1. Deposit Amount')
                print('2. Withdraw Amount')
                print('3. Check Available Balance')
                print('4. Check Transaction History')
                print('5. Take Loan')
                print('6. Transfer Amount')
                print('7. Log Out')
                print('8. Exit')

                ch = input('Choose Option: ')

                if ch == '1':
                    amount = int(input('Enter Deposit Amount: '))
                    current_user.deposit(amount)

                elif ch == '2': 
                    amount = int(input('Enter Withdraw Amount: '))
                    current_user.withdraw(amount)

                elif ch == '3':
                    current_user.check_balance()

                elif ch == '4':
                    current_user.check_transaction_history()

                elif ch == '5':
                    amount = int(input('Enter Loan Amount: '))
                    current_user.take_loan(bank, amount)

                elif ch == '6':
                    ac_no = int(input('Receiver Account No: '))
                    amount = int(input('Enter Transefer Amount: '))
                    current_user.transfer_amount(bank, ac_no, amount)

                elif ch == '7':
                    current_user = None

                elif ch == '8':
                    break

                else:
                    print('Wrong Option Choosen. Please, choose between 1 to 8')


if __name__ == '__main__':
    main()