import pytest
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def registration_page(page: Page) -> RegistrationPage:
    registration_page = RegistrationPage(page)
    registration_page.navigate()
    registration_page.click_privacy_policy_button()
    return registration_page
