# Uzum E2E Test Automation Suite (Selenium & Playwright)

This repository contains a professional end-to-end (E2E) test automation suite for the **Uzum.uz** marketplace. It showcases E2E UI testing best practices using both **Selenium WebDriver** and **Playwright**, implemented in **Python** with **Pytest**.

---

## 🚀 Features

*   **Dual-Framework Implementation**: Showcase of identical E2E checkout flows using both Selenium and Playwright to compare stability and performance.
*   **Anti-Bot Detection Bypass**: Custom configurations in WebDriver options (`AutomationControlled` disabled, custom user-agent strings) to successfully bypass typical marketplace scrapers protections.
*   **Auto-Waiting & Resilience**: Playwright-based tests utilizing implicit auto-waiting, significantly reducing test flakiness on dynamic content.
*   **Structured Test Configurations**: Reusable Pytest fixtures and setups defined in `conftest.py`.

---

## 🛠️ Tech Stack

*   **Language**: Python 3.8+
*   **Testing Framework**: Pytest
*   **Automation Engines**: Selenium WebDriver & Playwright
*   **Drivers**: Webdriver Manager for automated Chrome binary management
*   **Reporting (Planned)**: Allure Framework

---

## 📂 Project Structure

```
uzum-autotests/
├── conftest.py               # Shared pytest fixtures (Selenium driver configuration)
├── requirements.txt          # Python project dependencies
├── README.md                 # Project documentation (this file)
└── tests/
    ├── test_uzum_e2e.py      # Selenium E2E purchase flow test
    └── test_uzum_playwright.py  # Playwright E2E purchase flow test
```

---

## ⚙️ Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/dilshat7/uzum-autotests.git
cd uzum-autotests
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers
```bash
playwright install
```

---

## 🧪 Running the Tests

To execute all test suites, simply run:
```bash
pytest -s -v
```

### Run specific test files:

*   **Selenium Tests**:
    ```bash
    pytest tests/test_uzum_e2e.py -s -v
    ```
*   **Playwright Tests**:
    ```bash
    pytest tests/test_uzum_playwright.py -s -v
    ```

---

## 📈 Project Management
The roadmap, backlog, and bug-tracking for this project are actively managed on the **[Uzum-Autotests Project Board](https://github.com/users/dilshat7/projects/4/views/1)**.