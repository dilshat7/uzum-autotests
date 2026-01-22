
# Part 3. Combined Tasks (Functions + Classes)
# Practice 7. Working with Functions and Classes Together

class User:
    """Helper User class for Tasks 7.1 and 7.2."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"

# Task 7.1
def create_user(name, age):
    """Accepts name and age, returning a User object."""
    return User(name, age)

# Task 7.2
def validate_age(user):
    """Accepts a User object and validates the age."""
    # Assume age must be non-negative and realistic
    if user.age < 0 or user.age > 120:
        return False
    return True

# Task 7.3
class Logger:
    """Logger class."""
    def log(self, text):
        print(f"[LOG]: {text}")

def test_login(logger):
    """Uses the logger to record steps."""
    logger.log("Starting login test")
    # ... test logic ...
    logger.log("Entering login...")
    logger.log("Entering password...")
    logger.log("Verification successful")

# Task 7.4
class Calculator:
    """Simple calculator."""
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

def run_tests(calc):
    """Runs a series of checks for the passed calculator object."""
    print("Running calculator tests...")
    
    res_add = calc.add(2, 3)
    if res_add == 5:
        print("Test ADD passed")
    else:
        print("Test ADD failed")

    res_sub = calc.sub(10, 4)
    if res_sub == 6:
        print("Test SUB passed")
    else:
        print("Test SUB failed")

if __name__ == "__main__":
    print("=== PART 3: COMBINED ===")
    print("\n--- Practice 7 ---")
    new_user = create_user("Marina", 22)
    print(f"7.1 Created user: {new_user}")
    
    print(f"7.2 Valid age? {validate_age(new_user)}")
    
    logger = Logger()
    test_login(logger)
    
    calc = Calculator()
    run_tests(calc)
