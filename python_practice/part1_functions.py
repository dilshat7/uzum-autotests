
# Part 1. Functions
# Practice 1. Basic Functions

# Task 1.1
def greet_user(name):
    """Accepts a username and prints a greeting message."""
    print(f"Hello, {name}!")

# Task 1.2
def sum_numbers(a, b):
    """Accepts two numbers and prints their sum."""
    print(a + b)

# Task 1.3
def print_length(s):
    """Accepts a string and prints its length."""
    print(len(s))

# Task 1.4
def calculate_price_with_discount(price, discount_percent):
    """Accepts price and discount percent, then prints the final cost."""
    final_price = price * (1 - discount_percent / 100)
    print(f"Final price: {final_price}")


# Practice 2. Functions with Return Values

# Task 2.1
def multiply(a, b):
    """Accepts two numbers and returns their product."""
    return a * b

# Task 2.2
def check_number_sign(n):
    """Accepts a number and returns a string indicating if it's positive, negative, or zero."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Task 2.3
def find_max_value(numbers):
    """Accepts a list of numbers and returns the maximum value."""
    if not numbers:
        return None
    return max(numbers)

# Task 2.4
def get_user_description(name, age):
    """Accepts name and age, returning a formatted description string."""
    return f"Name: {name}, Age: {age}"


# Practice 3. Functions for QA

# Task 3.1
def check_equality(actual, expected):
    """Accepts actual and expected values, returns True or False."""
    return actual == expected

# Task 3.2
def is_success_status(status_code):
    """Accepts a status code and returns whether it is successful (200–299)."""
    return 200 <= status_code <= 299

# Task 3.3
def validate_credentials(login, password):
    """Accepts login and password, returns validation result (mock implementation)."""
    # Simple check example
    valid_login = "admin"
    valid_password = "password123"
    return login == valid_login and password == valid_password

# Task 3.4
def generate_email(username):
    """Generates an email based on the username."""
    return f"{username.lower()}@example.com"

if __name__ == "__main__":
    print("=== PART 1: FUNCTIONS ===")
    print("\n--- Practice 1 ---")
    greet_user("Alex")
    sum_numbers(10, 5)
    print_length("Automation")
    calculate_price_with_discount(1000, 15)

    print("\n--- Practice 2 ---")
    print(f"2.1 Multiply 4 * 5 = {multiply(4, 5)}")
    print(f"2.2 Number sign -10: {check_number_sign(-10)}")
    print(f"2.3 Max of [3, 1, 9, 2]: {find_max_value([3, 1, 9, 2])}")
    print(f"2.4 Description: {get_user_description('Bob', 30)}")

    print("\n--- Practice 3 ---")
    print(f"3.1 5 == 5? {check_equality(5, 5)}")
    print(f"3.2 Status 200 is success? {is_success_status(200)}")
    print(f"3.3 Login success? {validate_credentials('admin', 'password123')}")
    print(f"3.4 Generated Email: {generate_email('TestUser')}")
