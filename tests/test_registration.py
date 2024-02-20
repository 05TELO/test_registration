from pages.registration_page import RegistrationPage


class TestRegistration:

    def test_register_with_empty_fields(
        self, registration_page: RegistrationPage
    ) -> None:
        registration_page.register("", "", "")
        assert registration_page.get_error_message(0) == "Поле не заполнено"
        assert registration_page.get_error_message(1) == "Поле не заполнено"
        assert registration_page.get_error_message(2) == "Поле не заполнено"

    def test_register_with_empty_username(
        self, registration_page: RegistrationPage
    ) -> None:
        registration_page.register("", "xxx@gmail.com", "Password123")
        assert registration_page.get_error_message(0) == "Поле не заполнено"
        assert registration_page.get_error_message(1) == ""
        assert (
            registration_page.get_error_message(2)
            == "Сложность пароля: средняя"
        )

    def test_register_with_bad_email(
        self, registration_page: RegistrationPage
    ) -> None:
        registration_page.register("username", "xxx", "Password123")
        assert registration_page.get_error_message(0) == ""
        assert (
            registration_page.get_error_message(1)
            == "Формат e-mail: somebody@somewhere.ru"
        )
        assert (
            registration_page.get_error_message(2)
            == "Сложность пароля: средняя"
        )

    def test_register_with_short_password(
        self, registration_page: RegistrationPage
    ) -> None:
        registration_page.register("username", "xxx@gmail.com", "pass")
        assert registration_page.get_error_message(0) == ""
        assert registration_page.get_error_message(1) == ""
        assert (
            registration_page.get_error_message(2)
            == "Пароль должен содержать минимум 8 символов"
        )

    def test_register_with_low_password(
        self, registration_page: RegistrationPage
    ) -> None:
        registration_page.register("username", "xxx@gmail.com", "11111111")
        assert registration_page.get_error_message(0) == ""
        assert registration_page.get_error_message(1) == ""
        assert (
            registration_page.get_error_message(2)
            == "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"
        )
