# Simple python banking program

# In our banking program, we would like to allow users to show balance, make a deposit and withdraw.

def show_balance(balance):
    print(f'Your balance is ${balance: .2f}')


def deposit():
    amount = float(input('How much you would like to deposit: $ '))
    if amount < 0:
        print('That is not a valid amount. Please try again.')
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input('How much would you like to withdraw? $ '))
    if amount > balance:
        print('You have insufficient funds. Please top up your account.')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0')
        return 0
    else:
        return amount

def main():
    balance = 0

    # placeholder to store zero balance

    is_Running = True

    # when this reads false, we exit the program.

    while is_Running:
        print('**********************************************')
        print('      Welcome to XZY Bank USSD Service      ')
        print('**********************************************')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Make Withdrawal')
        print('4. Exit')
        print('**********************************************')
        choice = input('Enter your choice (1-4): ')
        print('**********************************************')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_Running = False
        else:
            print('That is not a valid input!! Please enter a number between (1-4)')
    print('**********************************************')
    print('Thank you for banking with us. Have a nice day!')

if __name__ == '__main__':
    main()