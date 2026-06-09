import allure
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class MainPage(BasePage):
    @property
    def profile_button(self)-> Locator:
        return self.page.locator("#profile-BTN")

    @property
    def role_element(self)-> Locator:
        return self.page.locator("#user-role")

    @allure.step("Нажать на кнопку профиля")
    def click_profile(self):
        self.highlight_and_attach(self.profile_button, "Кнопка профиля")
        self.profile_button.click()
        return self

    @allure.step("Убедиться, что пользователь залогинен под ролью {expected_role}")
    def check_role(self, expected_role):
        self.highlight_and_attach(self.role_element, "Элемент роли пользователя в системе")
        expect(self.role_element).to_contain_text(expected_role)