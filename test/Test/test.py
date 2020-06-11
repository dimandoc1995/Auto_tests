from selenium import webdriver
import time

driver = webdriver.Chrome("..\drivers\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://automationpractice.com/")
driver.find_element_by_css_selector('.header_user_info').click()
time.sleep(4)
driver.find_element_by_name("email").send_keys("seleniumisgood@mail.com")
driver.find_element_by_name("passwd").send_keys("123456")
driver.find_element_by_css_selector('.icon-lock.left').click()
time.sleep(4)

