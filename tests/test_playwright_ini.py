import pytest
import time
import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    
    #Go to page
    page.goto('https://playwright.dev')

    #expect get started
    expect(page).to_have_title(re.compile('Playwright'))
                               
def test_get_started_link(page: Page):

    #Go to page
    page.goto('https://playwright.dev')                          

    #Click the get started link
    page.get_by_role('link',name='Get Started').click()

    #expects page to have header with installation

    expect(page.get_by_role('heading',name='Installation')).to_be_visible()