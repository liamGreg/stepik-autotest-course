from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
)

browser.find_element_by_id('book').click()

x = browser.find_element_by_id('input_value').text
y = calc(x)
browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id("solve").click()
