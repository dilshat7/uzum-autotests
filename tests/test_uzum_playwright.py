import pytest
from playwright.sync_api import Page, expect
from re import compile as re_compile

def test_uzum_e2e_playwright(page: Page):
    """
    E2E test flow for Uzum.uz using Playwright.
    Playwright handles lazy loading and dynamic content automatically.
    """
    # 1. Заходим на https://uzum.uz/ru
    print("1. Opening Uzum.uz...")
    page.goto("https://uzum.uz/ru")
    
    # 2. Если уточняет город, нажимаем "Да"
    print("2. Checking for location confirmation...")
    accept_btn = page.locator("button.tooltip__accept-btn.small")
    if accept_btn.is_visible(timeout=5000):
        accept_btn.click()
        print("Location confirmed.")
    else:
        print("Location confirmation not found or timed out, proceeding.")

    # 3. Нажать на "Каталог"
    print("3. Clicking 'Каталог'...")
    # Playwright's auto-wait helps find the element even if it's being rendered
    catalog_btn = page.get_by_text("Каталог", exact=False).first
    catalog_btn.click()

    # 4. Выбрать "Товары недели"
    print("4. Selecting 'Товары недели'...")
    # Using data attribute for stability if possible, otherwise text
    items_of_week = page.locator("li.parent-category-link[data-data*='250']")
    if items_of_week.is_visible(timeout=5000):
        items_of_week.click()
    else:
        # Fallback to text search
        page.get_by_text("Товары недели", exact=False).click()

    # 5. Выбрать 1 товар (нажать на кнопку корзины)
    print("5. Clicking cart button on the first product...")
    # Playwright will automatically scroll the element into view before clicking
    cart_button = page.locator("[data-test-id='product-card__cart']").first
    cart_button.click()

    # 6. В модальном окне выбрать "6GB | 128GB" (если модалка появилась)
    # Note: Depending on the product, a modal might or might not appear.
    print("6. Checking for product options modal...")
    option_selector = "div.radio-text-wrapper:has-text('6GB | 128GB')"
    add_to_cart_modal_selector = "[data-test-id='button__add-cart']"
    
    # Wait for either the modal button or the option
    try:
        page.wait_for_selector(add_to_cart_modal_selector, timeout=5000)
        print("Modal appeared.")
        option = page.locator(option_selector)
        if option.is_visible():
            print("Selecting '6GB | 128GB'...")
            option.click()
        
        # 7. Нажать "Добавить в корзину" в модалке
        print("7. Clicking 'Добавить в корзину' in modal...")
        page.locator(add_to_cart_modal_selector).click()
    except Exception:
        print("No choice modal appeared or timed out, assuming added to cart directly.")

    # 8. Нажать на иконку корзинки в хедере
    print("8. Clicking cart icon in header...")
    header_cart = page.locator("[data-test-id='header__cart']")
    header_cart.click()

    # Verify we are on the cart page
    expect(page).to_have_url(re_compile(r".*/cart.*"))

    # 9. Нажать "Оформить"
    print("9. Clicking 'Оформить'...")
    checkout_btn = page.get_by_role("button", name="Оформить").or_(page.get_by_text("Оформить"))
    checkout_btn.first.click()

    # 10. Ожидание 5 секунд (как в оригинальном запросе)
    print("10. Waiting for 5 seconds as requested...")
    page.wait_for_timeout(5000)
    
    print("Test completed.")
