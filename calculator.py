"""Basic interactive calculator.

Usage:
    python calculator.py

Supports +, -, *, / and quit.
"""

def calculate(expression: str) -> float:
    """Evaluate a simple arithmetic expression safely."""
    allowed_chars = "0123456789+-*/(). "
    if not expression:
        raise ValueError("Empty expression")
    if any(ch not in allowed_chars for ch in expression):
        raise ValueError("Invalid character in expression")

    # very simple safety: only math operators and digits are allowed
    return eval(expression, {"__builtins__": None}, {})


def main() -> None:
    print("Basic Calculator")
    print("Enter an expression to evaluate (e.g. 2+2*3). Type 'quit' or 'exit' to stop.")

    while True:
        try:
            expression = input("calc> ").strip()
            if expression.lower() in {"quit", "exit"}:
                print("Goodbye!")
                break
            if expression == "":
                continue

            result = calculate(expression)
            print(result)
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
