import pytest
import time
from playwright.sync_api import Page, expect

def test_login_ok(page: Page):

    #Arrange
    page.goto('https://www.demoblaze.com/')

    #time.sleep(3)

    #Act
    #-----Click on login link
    page.locator('id=login2').click()

    #-----Fill with valid data and click login
    username = 'nicolas15'
    page.locator('id=loginusername').fill(username)
    page.locator('id=loginpassword').fill('nino123')
    page.locator('xpath=//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

    time.sleep(3)

     #Assert
    expect(page.get_by_text('Home')).to_be_visible()
    expect(page.get_by_text('Welcome '+username)).to_be_visible()
    #expect(page.get_by_role('heading',name='Welcome nicolas15')).to_be_visible()

def test_login2_ok(page: Page):
    assert True