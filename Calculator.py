class Calculator:
    def __init__(self, history=[]):
        self.history = history

    def ask_user_input(self):
        x = float(input("x: "))
        y = float(input("y: "))
        return x, y

    def add(self):
        x, y = self.ask_user_input()
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

def main():
    calculator = Calculator() # Create an instance of Calculator
    
    # Example usage:
    print("Let's perform an addition!")
    calculator.add() # Call the add method to get user input and perform addition
    
    print("\nCalculation History:")
    for entry in calculator.history:
        print(entry)

if __name__ == "__main__":
    main()
