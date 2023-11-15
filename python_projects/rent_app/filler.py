from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
import os
import time

PATH = os.environ["path"]
FORM = os.environ["form"]


class FormFiller:

    def __init__(self):
        self.service = Service(executable_path=PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(FORM)

    def fill_form(self, tuple_data):
        time.sleep(2)
        try:
            input_name = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

            input_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

            input_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            apply_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        except NoSuchElementException as exc:
            print(exc)
        else:
            input_name.send_keys(tuple_data[0])
            input_price.send_keys(tuple_data[1])
            input_link.send_keys(tuple_data[2])
            apply_button.click()

        time.sleep(2)

        try:
            return_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        except NoSuchElementException as exc:
            print(exc)
        else:
            return_button.click()

    def close_window(self):
        self.driver.quit()