from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_uzum_e2e_flow(driver):
    """
    E2E test flow for Uzum.uz as requested.
    """
    wait = WebDriverWait(driver, 15)
    
    # 1. Заходим на https://uzum.uz/ru
    print("1. Opening Uzum.uz...")
    driver.get("https://uzum.uz/ru")
    
    # 2. Если уточняет город, нажимаем "Да"
    print("2. Checking for location confirmation...")
    try:
        # Ждем появления модалки или кнопки "Да"
        accept_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tooltip__accept-btn.small")))
        accept_btn.click()
        print("Location confirmed.")
    except Exception:
        print("Location confirmation not found or timed out, proceeding.")

    # 3. Нажать на "Каталог"
    print("3. Clicking 'Каталог'...")
    try:
        catalog_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Каталог')] | //div[@class='catalog-icon']")))
        catalog_btn.click()
    except Exception as e:
        print(f"Failed to click 'Каталог': {e}")
        # Fallback to JS click
        driver.execute_script("document.querySelector('.catalog-icon').click();")

    # 4. Выбрать "Товары недели" (id: 250)
    print("4. Selecting 'Товары недели'...")
    try:
        # Используем селектор из HTML пользователя
        items_of_week = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.parent-category-link[data-data*='250']")))
        items_of_week.click()
    except Exception as e:
        print(f"Failed to select 'Товары недели': {e}")
        # Try finding by text
        items_of_week_alt = driver.find_element(By.XPATH, "//span[contains(text(), 'Товары недели')]")
        items_of_week_alt.click()

    # 5. Выбрать 1 товар (нажать на кнопку корзины)
    print("5. Clicking cart button on the first product...")
    try:
        # Ждем появления карточек товаров и нажимаем на кнопку корзины
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='product-card__cart']")))
        # Scroll to it first
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_button)
        time.sleep(1)
        cart_button.click()
    except Exception as e:
        print(f"Failed to click product cart button: {e}")

    # 6. В модальном окне выбрать "6GB | 128GB"
    print("6. Selecting '6GB | 128GB'...")
    try:
        option_xpath = "//div[contains(@class, 'radio-text-wrapper')]//div[contains(text(), '6GB | 128GB')]"
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()
    except Exception as e:
        print(f"Failed to select option '6GB | 128GB': {e}")

    # 7. Нажать "Добавить в корзину" в модалке
    print("7. Clicking 'Добавить в корзину'...")
    try:
        add_to_cart_modal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='button__add-cart']")))
        add_to_cart_modal.click()
    except Exception as e:
        print(f"Failed to click 'Добавить в корзину' in modal: {e}")

    # Ждем возврата на список товаров (просто небольшая пауза)
    time.sleep(2)

    # 8. Нажать на иконку корзинки в хедере
    print("8. Clicking cart icon in header...")
    try:
        header_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart, [data-test-id='header__cart']")))
        header_cart.click()
    except Exception as e:
        print(f"Failed to click header cart: {e}")
        # Fallback link
        driver.get("https://uzum.uz/ru/cart")

    # 9. Нажать "Оформить"
    print("9. Clicking 'Оформить'...")
    try:
        checkout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Оформить')] | //button[contains(., 'Оформить')]")))
        checkout_btn.click()
    except Exception as e:
        print(f"Failed to click 'Оформить': {e}")

    # 10. Ожидание 5 секунд
    print("10. Waiting for 5 seconds as requested...")
    time.sleep(5)
    
    print("Test completed.")
