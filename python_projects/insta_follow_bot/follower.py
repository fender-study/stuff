from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

URL = "https://www.instagram.com/"
chrome_driver_path = os.environ["my_path"]
EMAIL = os.environ["my_email"]
PASSWORD = os.environ["my_password"]
SIMILAR_ACCOUNT = "blizzard"


class InstaFollower:
    def __init__(self):
        self.service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(url=URL)
        self.driver.maximize_window()

    def login(self):
        time.sleep(2)
        email_input = self.driver.find_element(By.NAME, 'username')
        email_input.send_keys(EMAIL)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(url=URL+SIMILAR_ACCOUNT)
        time.sleep(5)
        try:
            followers_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        except NoSuchElementException as exc:
            print(exc)
        else:
            followers_button.click()

    def follow(self):
        time.sleep(5)
        print("Executing follow")
        try:
            buttons = self.driver.find_elements(By.CLASS_NAME, "_aj1-")
        except NoSuchElementException as exc:
            print(exc)
        except ElementClickInterceptedException as exc:
            print(exc)
        else:
            for action in buttons:
                try:
                    if action.text == "Подписаться":
                        action.click()
                        print("followed...")
                except ElementClickInterceptedException as exc:
                    print(exc)
                time.sleep(1)
        self.driver.close()
