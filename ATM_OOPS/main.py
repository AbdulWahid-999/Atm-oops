class ATMmachine:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"💰 Your balance is: ${self.balance}")

    def deposit(self):
        try:
            pin = int(input("🔐 Enter Your PIN: "))
            if self.check_pin(pin):
                amount = int(input("💵 Enter the deposit amount: "))
                if amount > 0:
                    self.balance += amount
                    print(f"✅ ${amount} deposited.")
                    self.check_balance()
                else:
                    print("❌ Deposit amount must be positive.")
            else:
                print("❌ Wrong PIN.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    def withdraw(self):
        try:
            pin = int(input("🔐 Enter Your PIN: "))
            if self.check_pin(pin):
                amount = int(input("💸 Enter the withdraw amount: "))
                if amount <= 0:
                    print("❌ Withdraw amount must be positive.")
                elif amount > self.balance:
                    print("❌ Insufficient balance.")
                else:
                    self.balance -= amount
                    print(f"✅ ${amount} withdrawn successfully.")
                    self.check_balance()
            else:
                print("❌ Wrong PIN.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    def start(self):
        while True:
            print("\n======= 🏧 ATM Machine =======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            try:
                choice = int(input("👉 Choose an option (1–4): "))

                if choice == 1:
                    pin = int(input("🔐 Enter Your PIN: "))
                    if self.check_pin(pin):
                        print("✅ PIN Verified.")
                        self.check_balance()
                    else:
                        print("❌ Wrong PIN.")

                elif choice == 2:
                    self.deposit()

                elif choice == 3:
                    self.withdraw()

                elif choice == 4:
                    print("👋 Exiting the ATM Machine. Thank you!")
                    break

                else:
                    print("❌ Invalid option. Try again.")
            except ValueError:
                print("⚠️ Please enter a number from 1 to 4.")


atm = ATMmachine()
atm.start()
