import pytest
import re

import playwright
from playwright.sync_api import Page, expect

#Arrange

@pytest.mark.ui
def test_bank_login(page: Page):

    #Arrange
    page.goto('https://demo.applitools.com')

    #Act
    page.locator('id=username').fill('Nino')
    page.locator('id=password').fill('nino123')
    page.locator('id=log-in').click()

    #Assert
    expect(page.locator('id=time')).to_be_visible()
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('Credit cards')).to_be_visible()