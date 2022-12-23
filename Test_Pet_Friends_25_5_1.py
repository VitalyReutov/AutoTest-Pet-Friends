import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets(go_to_my_pets):
   '''Присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   time.sleep(5)

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   number_of_pets = len(pets)

   assert number == number_of_pets

def test_photo_half(go_to_my_pets):
   '''Хотя бы у половины питомцев есть фото'''

   element = WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
   time.sleep(5)

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   half = number // 2

   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1
   assert number_а_photos >= half
   print(f' Количество фото: {number_а_photos}')
   print(f' Половина от числа питомцев: {half}')

def test_name_gender_age(go_to_my_pets):
   '''У всех питомцев есть имя, возраст и порода'''

   element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   time.sleep(5)

   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3

def test_all_pets_have_different_names(go_to_my_pets):
   '''У всех питомцев разные имена'''

   element = WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   time.sleep(5)

   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   cnt = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         cnt += 1
   assert cnt == 0

def test_no_duplicate(go_to_my_pets):
    '''В списке нет повторяющихся питомцев'''

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    time.sleep(5)

    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    list_line = line.split(' ')

    set_list_line = set(list_line)

    a = len(list_line)
    b = len(set_list_line)

    result = a - b
    assert result == 0