from app.operation.operations import Add, Subtract, Multiply, Divide
from app.calculation.calculation import Calculation


class CalculationFactory:
    """Creates Calculation objects based on operation name."""

    OPERATIONS = {
        "add": Add,
        "sub": Subtract,
        "mul": Multiply,
        "div": Divide
    }

    @classmethod
    def create(cls, op_name, a, b):

        # LBYL: check before using
        if op_name not in cls.OPERATIONS:
            raise ValueError("Invalid operation")

        operation = cls.OPERATIONS[op_name]()
        return Calculation(a, b, operation)
