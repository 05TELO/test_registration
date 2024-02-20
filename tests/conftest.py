from typing import Generator

import pytest
from playwright.sync_api import Browser
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

from pages.registration_page import RegistrationPage


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser: Browser) -> Generator[Page, None, None]:
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def registration_page(page: Page) -> RegistrationPage:
    registration_page = RegistrationPage(page)
    registration_page.navigate()
    return registration_page
