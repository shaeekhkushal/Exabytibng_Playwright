import pytest
from config import Config


@pytest.fixture
def set_up(page):
    url = Config.url
    print("Opening URL: " + url)
    page.goto(url)
    page.set_default_timeout(50000)

    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 1024,
        }
    }
