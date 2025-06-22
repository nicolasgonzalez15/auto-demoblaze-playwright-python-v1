import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):

    #Arrange
    page.goto("https://playwright.dev/")

    #Assert
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_lint(page: Page):

    #Arrange
    page.goto("https://playwright.dev/")

    #Click get started link
    page.get_by_role('link',name='Get Started').click()
    #page.get_by_text('Get Started').click()

    #Assert
    expect(page.get_by_role('heading',name='Installation')).to_be_visible()