class Operation:
    """Base class for all operations."""

    def execute(self, a, b):
        raise NotImplementedError


class Add(Operation):

    def execute(self, a, b):
        return a + b


class Subtract(Operation):

    def execute(self, a, b):
        return a - b


class Multiply(Operation):

    def execute(self, a, b):
        return a * b


class Divide(Operation):

    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
