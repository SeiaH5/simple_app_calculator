class MDAS:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def divide(self):
        if self.num_2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.num_1 / self.num_2

    def add(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2


class ask_user:
    MENU = {
        "1": ("Multiplication", "*"),
        "2": ("Division",       "/"),
        "3": ("Addition",       "+"),
        "4": ("Subtraction",    "-"),
    }
    
    def run(self):
        print("\n===========================")
        print("\033[1m         Calculator      \033[0m")
        print("===========================")
        
        while True:
            print()
            for key, (name, symbol) in self.MENU.items():
                print(f"  {key}. {name} ({symbol})")
            choice = input("\n\033[1mChoose an operation (1-4): \033[0m").strip()

            if choice not in self.MENU:
                print("\n\033[31mInvalid choice. Try again.\033[0m")
                print("-"*27)
                continue

            try:
                num_1 = int(input("Enter first integer : "))
                num_2 = int(input("Enter second integer: "))

            except ValueError:
                print("\n\033[31mInvalid input. Please enter an integer.\033[0m")
                print("-"*45)
                continue

            numbers = MDAS(num_1, num_2)

            try:
                if choice == "1":
                    result = numbers.multiply()
                elif choice == "2":
                    result = numbers.divide()
                elif choice == "3":
                    result = numbers.add()
                else:
                    result = numbers.subtract()

                print(f"\n\033[1mResult: \033[32m{result}\033[0m")

            except ZeroDivisionError as e:
                print(f"\033[31mError: {e}\033[0m")
                print("-"*30)

            while True:
                try_again = input("\n\033[1mDo you want to try again? \033[35m[yes/no]: \033[0m").strip().lower()
                if try_again in ("yes", "no"):
                    print("\n")
                    break
                print("\n\033[31m\033[1mPlease enter 'yes' or 'no' only.\033[0m")

            if try_again in ("no"):
                print("\033[1mThank you!\033[0m\n")
                break

ask_user().run()
