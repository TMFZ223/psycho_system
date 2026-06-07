import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@pytest.fixture(scope="session")
def browser() -> Browser:

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            channel="chrome",
            headless=False
        )

        yield browser

        browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:

    context = browser.new_context(
        viewport={
            "width": 1920,
            "height": 1080
        }
    )

    yield context

    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:

    page = context.new_page()

    page.set_default_timeout(15000)
    page.set_default_navigation_timeout(15000)

    yield page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.fixture
def main_page(page):
    return MainPage(page)