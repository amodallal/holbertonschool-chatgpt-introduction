#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        """Initialize the checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit a valid amount into the checkbook."""
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw a valid amount from the checkbook if sufficient funds exist."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Main function to handle user interaction with the checkbook."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $").strip())
                cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $").strip())
                cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

