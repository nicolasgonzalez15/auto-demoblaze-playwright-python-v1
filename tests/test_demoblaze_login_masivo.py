import time
import csv
from playwright.sync_api import Page, expect, sync_playwright, Playwright

def test_csv_file(page:Page):
    #Accedo a archivo de csv y lo leo
    with open("excel/datos_entrada.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:

            #Ingreso a sitio web
            page.goto('https://www.demoblaze.com')

            #Act
            #-----Click on login link
            page.locator('id=login2').click()


            #Completar con datos del csv
            page.locator('id=loginusername').fill(line[0])
            page.locator('id=loginpassword').fill(line[1])

            #Click en Login
            page.locator('xpath=//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

