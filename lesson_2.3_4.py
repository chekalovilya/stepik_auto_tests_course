from selenium import webdriver
import math
import time
# from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    pole = browser.find_element_by_id("answer")
    pole.send_keys(y)
    browser.find_element_by_class_name("btn-primary").click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()