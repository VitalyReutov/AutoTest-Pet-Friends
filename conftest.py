import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/tests_drivers/chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():

   element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element(By.ID,'email').send_keys('vit.reutoff@gmail.com')

   element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element(By.ID,'pass').send_keys('123456')

   element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()