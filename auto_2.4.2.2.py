from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #browser
    browser = webdriver.Chrome()
    browser.get(link)
    #step 2 w8 and click

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    book = browser.find_element(By.ID, "book").click()

    # step3 Math x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    Submit = browser.find_element(By.ID, "solve").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()