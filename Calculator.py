class Calculator:
    def __init__(self, history):
        self.history = []

    def ask_user_input(self):
        x = float(input("x: "))
        y = float(input("y: "))

    def add(self, x, y):
        result = x + y
        self.history.apppend(result)
        return result

calc = Calculator

print(calc.add)