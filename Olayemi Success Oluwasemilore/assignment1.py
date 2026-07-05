print("      BASIC MATHEMATICAL CALCULATOR (MC)    ")
print("Available operations: +, -, *, /, \\, ^, %, C, OFF")
current_value = None
while True:
    if current_value is None:
        user_input = input("\nEnter first number (or type 'OFF' to quit): ").strip()
        if user_input.upper() == 'OFF':
            print("Calculator turning off. Goodbye!")
            break
        current_value = float(user_input)

    operator = input(f"Current Value [{current_value}]. Enter operator: ").strip()

    if operator.upper() == 'OFF':
        print("Calculator turning off. Goodbye!")
        break
    elif operator.upper() == 'C':
        print("Resetting calculator screen...")
        current_value = None
        continue

    if operator not in ['+', '-', '*', '/', '\\', '^', '%']:
        print("Invalid operator choice. Try again.")
        continue

    next_input = input("Enter next number: ").strip()
    if next_input.upper() == 'OFF':
        print("Calculator turning off. Goodbye!")
        break
    next_num = float(next_input)

    if operator == '+':
        current_value += next_num
    elif operator == '-':
        current_value -= next_num
    elif operator == '*':
        current_value *= next_num
    elif operator == '^':
        current_value = current_value ** next_num
    elif operator == '/':
        if next_num == 0:
            print("Error: Cannot divide by zero!")
            current_value = None
        else:
            current_value /= next_num
    elif operator == '\\':
        if next_num == 0:
            print("Error: Cannot divide by zero!")
            current_value = None
        else:
            current_value = current_value // next_num
    elif operator == '%':
        if next_num == 0:
            print("Error: Cannot divide by zero!")
            current_value = None
        else:
            current_value = current_value % next_num

    if current_value is not None:
        print(f"Result: {current_value}")