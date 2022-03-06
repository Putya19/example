from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #запуск бразуера и переход по ссылке

    browser = webdriver.Chrome()
    browser.get(link)

    #поиск и рассчет формулы
    valuex = browser.find_element(By.ID, "input_value")
    x = valuex.text
    y = calc(x)
    #работа со страницей
    answer = browser.find_element(By.ID,"answer").send_keys(y)

    # Отправляем заполненную форму
    checkbox = browser.find_element(By.ID,"robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    robots_rule = browser.find_element(By.ID,'robotsRule')
    robots_rule.click()

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
