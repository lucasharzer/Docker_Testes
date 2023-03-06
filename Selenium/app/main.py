from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    chrome_options=options
)

driver.get(os.getenv("URL"))
while True:
    try:
        if driver.find_element(By.ID, "comercial"):
            break
    except:
        pass

valor = driver.find_element(By.ID, "comercial").get_attribute("value")
print(f"\nO valor do euro hoje é \033[32mR${valor}\033[m")

driver.close()
