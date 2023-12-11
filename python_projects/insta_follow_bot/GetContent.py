from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementClickInterceptedException
import time

URL = "https://thinkwritten.com/365-creative-writing-prompts/"
chrome_driver_path = "E:\Dif\chromedriver_win32\chromedriver.exe"


def main():
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url=URL)
    time.sleep(5)
    count = 1
    content = ""
    prompts = driver.find_elements(By.CSS_SELECTOR, 'p')
    for item in prompts:
        print(item.text)
    for i in range(len(prompts)):
        item_data = prompts[i].text.split('.')[0].strip()
        print(item_data)
        item_number = int(item_data)
        if count == item_number:
            content += f"{prompts[i].text}\n"
            count += 1
            print(f"item {count} processed")
    driver.close()

    with open("prompts.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
