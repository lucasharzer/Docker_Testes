from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
import os


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_default_timeout(0)

    load_dotenv(find_dotenv())

    page.goto(os.getenv("URL"))

    page.wait_for_selector("//*[@id='root']/div[2]/div/div[1]/div/div[3]/div[2]/form/div[2]/input")
    valor = page.locator(
        "//*[@id='root']/div[2]/div/div[1]/div/div[3]/div[2]/form/div[2]/input"
    ).get_attribute("value")

    print(f"\nO valor do dólar hoje é \033[32mR${valor}\033[m")
