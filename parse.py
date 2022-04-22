import requests
import datetime
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# options = webdriver.ChromeOptions()
# options.add_argument()


path = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=path)
url = 'https://www.avito.ru/rossiya?q=710%2F45-26.5'


class DataAvito:
    def __init__(self, time_data, href_data):
        self.time_data = time_data
        self.href_data = href_data


try:
    driver.get(url=url)
    data = driver.find_element(By.CLASS_NAME, "iva-item-content-rejJg")
    href_data = driver.find_element(By.XPATH, '//*[@id="i2345087615"]/div/div[2]/div[2]/a')
    time_data = driver.find_element(By.CSS_SELECTOR, '#i2345087615 > div > div.iva-item-body-KLUuy > div.iva-item-dateInfoStep-_acjp > div')
    # print('Ссылка ' + href_data.get_attribute('href'))
    # print(time_data.text)
    # print(data.text)

    a = DataAvito(time_data.text, href_data.get_attribute('href'))
    print(a.time_data, '  ', a.href_data)

    # time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
