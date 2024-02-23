from typing import Optional

from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto("https://koshelek.ru/authorization/signup")

    def fill_username(self, username: str) -> None:
        username_input = self.page.get_by_label("Имя пользователя")
        username_input.fill(username)

    def fill_email(self, email: str) -> None:
        email_input = self.page.get_by_label("Электронная почта")
        email_input.fill(email)

    def fill_password(self, password: str) -> None:
        password_input = self.page.get_by_label("Пароль")
        password_input.fill(password)

    def click_privacy_policy_button(self) -> None:
        privacy_policy_checkbox = self.page.get_by_role("checkbox")
        privacy_policy_checkbox.click()

    def click_register_button(self) -> None:
        register_button = self.page.get_by_role("button", name="Далее")
        register_button.click()

    def register(self, username: str, email: str, password: str) -> None:
        self.fill_username(username)
        self.fill_email(email)
        self.fill_password(password)
        self.click_register_button()

    def get_error_message(self, error: int) -> Optional[str]:
        error_message_locator = self.page.locator(".v-messages__message").nth(
            error
        )
        return (
            error_message_locator.inner_text()
            if error_message_locator.is_visible()
            else None
        )
