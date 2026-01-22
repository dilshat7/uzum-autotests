
from part1_functions import (
    greet_user, sum_numbers, print_length, calculate_price_with_discount,
    multiply, check_number_sign, find_max_value, get_user_description,
    check_equality, is_success_status, validate_credentials, generate_email
)
from part2_classes import (
    User, Product, Rectangle, GreeterUser, Counter, NumberChecker,
    TestCase, LoginTest, CalculatorTest, APIResponse, DataGenerator
)
from part3_combined import (
    create_user, validate_age, Logger, test_login, Calculator, run_tests
)

def main():
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

    print("\n\n=== PART 2: CLASSES ===")
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

    print("\n\n=== PART 3: COMBINED ===")
    print("\n--- Practice 7 ---")
    new_user = create_user("Marina", 22)
    print(f"7.1 Created user: {new_user}")
    
    print(f"7.2 Valid age? {validate_age(new_user)}")
    
    logger = Logger()
    test_login(logger)
    
    calc = Calculator()
    run_tests(calc)

if __name__ == "__main__":
    main()
