class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name




class Customer(Person):

    def __init__(self, first_name, last_name, account_number, balance = 0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance


    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}\nAccount({self.account_number}): ${self.balance}"


    def deposit(self, amount_to_add):
        self.balance += amount_to_add
        print(f"You've added ${amount_to_add} to your account")


    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount_to_withdraw
            print(f"You've withdrawn ${amount_to_withdraw} from your account")



def create_client():
    first_name_ct = input("Enter your first name: ")
    last_name_ct = input("Enter your last name: ")
    account_number = input("Enter a 3 digit account number: ")
    customer1 = Customer(first_name_ct, last_name_ct, account_number)

    return customer1

def start():
    print("WELCOME TO PYTHON BANK")
    my_customer = create_client()
    print(my_customer)
    option = 0

    while option != 'E':
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        option = input()

        if option == 'D':
            dep_amount = int(input("Enter the amount to deposit: "))
            my_customer.deposit(dep_amount)
        elif option == 'W':
            withdraw_amount = int(input("Enter the withdraw amount: "))
            my_customer.withdraw(withdraw_amount)

        print(my_customer)

    print("Thank you for using Python Bank")

start()







