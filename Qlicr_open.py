from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com")
user_ele = driver.find_element_by_name("username")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("anish@arlabhq.in")
pwd_ele.send_keys("Arlab@01")

#driver.find_element_by_name("Login").click()
driver.find_element_by_name("btnLogin").click()




