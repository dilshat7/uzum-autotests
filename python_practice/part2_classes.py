
import random
import string

# Part 2. Classes
# Practice 4. Basics of Classes

# Task 4.1
class User:
    """User class with name and age attributes."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Task 4.2
class Product:
    """Product class with title and price attributes."""
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def print_description(self):
        """Prints a short description of the product."""
        print(f"Product: {self.title}, Price: {self.price}")

# Task 4.3
class Rectangle:
    """Rectangle class with width and height attributes."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height


# Practice 5. Class Methods

# Task 5.1
class GreeterUser:
    """User class with a greeting method."""
    def __init__(self, name):
        self.name = name

    def greet(self):
        """Prints a greeting message."""
        print(f"Hello, I am {self.name}!")

# Task 5.2
class Counter:
    """Counter class with methods to change the value."""
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

# Task 5.3
class NumberChecker:
    """Class for checking numbers."""
    def __init__(self, number):
        self.number = number

    def is_even(self):
        """Checks if the number is even."""
        return self.number % 2 == 0


# Practice 6. Classes in QA

# Task 6.1
class TestCase:
    """TestCase class simulation."""
    def __init__(self, name):
        self.name = name

    def success(self):
        print(f"Test '{self.name}' passed.")

    def fail(self):
        print(f"Test '{self.name}' failed.")

# Task 6.2
class LoginTest:
    """Class for login verification."""
    def __init__(self, correct_login, correct_password):
        self.correct_login = correct_login
        self.correct_password = correct_password

    def run(self, login, password):
        """Verifies the entered credentials."""
        if login == self.correct_login and password == self.correct_password:
            return True
        return False

# Task 6.3
class CalculatorTest:
    """Class with a set of tests for a calculator."""
    def test_add(self, a, b, expected):
        if a + b == expected:
            print(f"ADD {a}+{b}={expected}: OK")
        else:
            print(f"ADD {a}+{b}={expected}: FAIL")

    def test_sub(self, a, b, expected):
        if a - b == expected:
            print(f"SUB {a}-{b}={expected}: OK")
        else:
            print(f"SUB {a}-{b}={expected}: FAIL")

    def test_mul(self, a, b, expected):
        if a * b == expected:
            print(f"MUL {a}*{b}={expected}: OK")
        else:
            print(f"MUL {a}*{b}={expected}: FAIL")
    
    def test_div(self, a, b, expected):
        if b != 0 and a / b == expected:
            print(f"DIV {a}/{b}={expected}: OK")
        else:
            print(f"DIV {a}/{b}={expected}: FAIL")

# Task 6.4
class APIResponse:
    """API Response simulation class."""
    def __init__(self, status_code):
        self.status_code = status_code

    def is_successful(self):
        """Checks if the response is successful."""
        return 200 <= self.status_code <= 299

# Task 6.5
class DataGenerator:
    """Test data generator."""
    def generate_email(self, name):
        return f"{name.lower()}{random.randint(100, 999)}@test.com"

    def generate_password(self, length=8):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("=== PART 2: CLASSES ===")
    print("\n--- Practice 4 ---")
    u = User("John", 25)
    print(f"4.1 User: {u.name}, Age: {u.age}")
    
    p = Product("Laptop", 1500)
    p.print_description()
    
    rect = Rectangle(10, 5)
    print(f"4.3 Rectangle area (10x5): {rect.get_area()}")

    print("\n--- Practice 5 ---")
    gu = GreeterUser("Alice")
    gu.greet()
    
    c = Counter(10)
    c.increment()
    print(f"5.2 Counter after increment: {c.count}")
    
    nc = NumberChecker(8)
    print(f"5.3 Is 8 even? {nc.is_even()}")

    print("\n--- Practice 6 ---")
    tc = TestCase("LoginTest")
    tc.success()
    
    lt = LoginTest("admin", "secret")
    print(f"6.2 Login result: {lt.run('admin', 'secret')}")
    
    ct = CalculatorTest()
    ct.test_add(2, 2, 4)
    
    api = APIResponse(404)
    print(f"6.4 Is 404 success? {api.is_successful()}")
    
    dg = DataGenerator()
    print(f"6.5 Generated Password: {dg.generate_password()}")
