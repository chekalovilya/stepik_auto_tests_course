from selenium import webdriver
import math
import time

# from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    browser.find_element_by_tag_name("button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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