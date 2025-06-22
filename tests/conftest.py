import pytest
import string
import random
from playwright.sync_api import sync_playwright, Playwright

@pytest.fixture()
def generate_username():
    characters = string.ascii_letters + string.digits + '._-'
    username = ''.join(random.choice(characters) for _ in range(random.randint(5, 32)))
    return username
