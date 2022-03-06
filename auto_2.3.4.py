from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    #browser
    browser = webdriver.Chrome()
    browser.get(link)
#1step
    btn1 = browser.find_element(By.CLASS_NAME, "btn").click()
#toStep2
    confirm = browser.switch_to.alert
    confirm.accept()
#step3
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    Submit = browser.find_element(By.CLASS_NAME, "btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()