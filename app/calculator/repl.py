from app.calculation.factory import CalculationFactory


class CalculatorREPL:
    """Command-line REPL interface for calculator."""

    def __init__(self):
        self.history = []

    def show_help(self):
        print("""
Commands:
 add      - Addition
 sub      - Subtraction
 mul      - Multiplication
 div      - Division
 history  - Show calculation history
 help     - Show this help
 exit     - Exit program
""")

    def show_history(self):

        if not self.history:
            print("No calculations yet.")
            return

        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item}")

    def get_number(self, prompt):

        # EAFP: try first, then handle error
        try:
            return float(input(prompt))
        except ValueError:
            raise ValueError("Invalid number")

    def run(self):

        print("Welcome to Calculator System!")
        self.show_help()

        while True:  # pragma: no cover


            command = input(">>> ").strip().lower()

            if command == "exit":
                print("Goodbye!")  # pragma: no cover
                break  # pragma: no cover


            if command == "help":
                self.show_help()
                continue  # pragma: no cover

            if command == "history":
                self.show_history()
                continue  # pragma: no cover

            try:
                a = self.get_number("Enter first number: ")
                b = self.get_number("Enter second number: ")

                calc = CalculationFactory.create(command, a, b)

                result = calc.result()

                entry = f"{a} {command} {b} = {result}"
                self.history.append(entry)

                print("Result:", result)

            except Exception as e:
                print("Error:", e)  # pragma: no cover

