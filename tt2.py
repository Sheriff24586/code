def calculate(expression):
    try:
        # Evaluate a simple arithmetic expression safely
        allowed_names = {
            'abs': abs,
            'round': round,
            'pow': pow,
        }
        return eval(expression, {'__builtins__': None}, allowed_names)
    except Exception:
        return None


def main():
    print('Simple Calculator')
    print('Enter an expression like 2 + 3 * 4 or type quit to exit')

    while True:
        expr = input('> ').strip()
        if expr.lower() in ('quit', 'exit'):
            break
        if not expr:
            continue

        result = calculate(expr)
        if result is None:
            print('Invalid expression')
        else:
            print(result)


if __name__ == '__main__':
    main()
