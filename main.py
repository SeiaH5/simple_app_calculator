# 1.  The application will ask the user to choose one of the 
#       four math operations (Addition, Subtraction, Multiplication and Division)
# 2.  The application will ask the user for two numbers
# 3.  Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during   
#     runtime.

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
    def run(self):
        print("\n===========================")
        print("\033[1m         Calculator      \033[0m")
        print("===========================")

        while True:
            print("""\n1. Multiply 
2. Divide
3. Add
4. Subtract
                  """)
            choice = input("Choose an operation (1-4): ").strip()

            if choice not in ("1", "2", "3", "4"):
                print("\033[31mInvalid choice. Try again.\033[0m")
                continue

ask_user().run()