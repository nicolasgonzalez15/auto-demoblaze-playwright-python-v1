import pytest
from playwright.sync_api import Page, expect, sync_playwright
import time

def test_signup_ok(page: Page,generate_username):

    #Arrange
    page.goto("https://www.demoblaze.com/")

    #Act
    #-------Click on signup button
    page.locator('id=signin2').click()

    #-------Fill with valid data and Sign up
    username = generate_username
    password = 'nino123'
    page.locator('id=sign-username').fill(username)
    page.locator('id=sign-password').fill(password)
    page.locator('xpath=//*[@id="signInModal"]/div/div/div[3]/button[2]').click()

    #-------Wait 3 seconds
    time.sleep(3)

    expect(page.get_by_text('Home')).to_be_visible()
