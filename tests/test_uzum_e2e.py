from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def debug_selectors():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        print("1. Opening Uzum.uz...")
        driver.get("https://uzum.uz/ru")

        print("2. Searching for 'Смартфон'...")
        try:
            search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="input__search"]')))
            search.clear()
            search.send_keys("Смартфон")
            search.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Search failed: {e}")
            # Try generic input if test-id fails
            search = driver.find_element(By.TAG_NAME, "input")
            if search:
                search.send_keys("Смартфон")
                search.send_keys(Keys.ENTER)

        print("3. Waiting for results...")
        time.sleep(5)  # Give it time to render

        print("4. Dumping page info...")
        # Save source to inspect later if needed
        with open("uzum_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Saved page source to 'uzum_source.html'")

        # Look for potential product links
        print("\n--- Potential Product Selectors Found ---")

        # Check standard common classes or tags
        links = driver.find_elements(By.TAG_NAME, "a")
        product_links = []
        for a in links:
            href = a.get_attribute("href")
            if href and "/product/" in href:
                product_links.append(a)

        print(f"Found {len(product_links)} links containing '/product/'")
        if product_links:
            print(f"First product link classes: {product_links[0].get_attribute('class')}")
            print(f"First product link data-test-id: {product_links[0].get_attribute('data-test-id')}")
            print(f"First product link outerHTML: {product_links[0].get_attribute('outerHTML')[:150]}...")

        # Also list all data-test-ids visible
        ids = driver.find_elements(By.CSS_SELECTOR, "[data-test-id]")
        print(f"\nFound {len(ids)} elements with data-test-id. First 10:")
        for el in ids[:10]:
            print(f"- {el.get_attribute('data-test-id')} ({el.tag_name})")

    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    debug_selectors()
