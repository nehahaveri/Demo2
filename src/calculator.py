def calculator(operation, num1, num2):
    """Perform a basic arithmetic operation on two numbers.

    Supported operations are 'add', 'subtract', 'multiply', and 'divide'.

    Args:
        operation: The operation name: 'add', 'subtract', 'multiply', or 'divide'.
        num1: The first operand.
        num2: The second operand.

    Returns:
        The result of applying the operation to num1 and num2.

    Raises:
        ValueError: If operation is not supported, or if dividing by zero.
    """
    if operation == "add":
        return num1 - num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    raise ValueError(f"Unsupported operation: {operation!r}")
