from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')


try:
    #browser
    browser = webdriver.Chrome()
    browser.get(link)

    #inputs
    fname = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]').send_keys("Vasya")
    lname = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]').send_keys("Pupkin")
    email = browser.find_element(By.CSS_SELECTOR, '[name = "email"]').send_keys("Pupkin@mail.com")

    #AddFile
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)

    #over
    button = browser.find_element(By.CLASS_NAME,"btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()