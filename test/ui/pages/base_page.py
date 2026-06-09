import allure
from playwright.sync_api import Page
from test_utils.env_reader import EnvReader
class BasePage:
    BASE_URL = EnvReader.get_env_variable_value("base_url_test_stage_ui")

    def __init__(self, page: Page):
        self.page = page

    def highlight_and_attach(self, locator, name="element"):
        locator.evaluate("""
        el => {
            el.style.outline = '4px solid green';
        }
        """)

        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )