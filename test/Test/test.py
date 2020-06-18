import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("..\drivers\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://automationpractice.com/")
SignIn = driver.find_element_by_css_selector('.header_user_info')
SignIn.click()
time.sleep(4)
Login = driver.find_element_by_name("email")
Login.send_keys('seleniumisgood@mail.com')
Password = driver.find_element_by_name("passwd")
Password.send_keys('123456')
Enter = driver.find_element_by_css_selector('.icon-lock.left')
Enter.click()
element = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]")
time.sleep(2)
assert element.text == 'Sign out'
driver.close()


#assert "Sign out" == driver.find_elements_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]")
# driver_new = driver.current_url
# print('Новая страница: ', driver_new)
# driver.get(driver_new)
