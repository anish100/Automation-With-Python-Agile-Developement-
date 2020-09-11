from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

# Connect the Qlicr Engine with Selenium
driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com")

# Enter the User Name for Loging the Qlicr Engine
user_ele = driver.find_element_by_name("username")
print(user_ele.is_displayed())    # Username is Displayed if user name is enter
print(user_ele.is_enabled())      # Username is enabled
time.sleep(10)
# Enter the Password of the Qlicr Engine
pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

# Input the User email id for loging the Qlicr Engine
user_ele.send_keys("tarun.soni@arlabhq.in")
time.sleep(5)
# Input the Password for loging the Qlicr Engine
pwd_ele.send_keys("Arlab@01")
time.sleep(5)

driver.find_element_by_name("btnLogin").click()  # Click the Login Button

Client_module = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientInfo/300015163")
print(Client_module)
time.sleep(10)
Debtor_click = driver.find_element_by_css_selector('#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button.btn.btn-xs.left-15.btn-danger').click()
print(Debtor_click)

Deb_Abn_no = driver.find_element_by_css_selector('#debtors > div.modal-dialog > div > div.modal-body > div.container-fluid > div > div:nth-child(3) > div > div > input').send_keys(Keys.HOME,'55620817665')
print(Deb_Abn_no)

Same_as_client_mail_address = driver.find_element_by_css_selector('#contact_tab > div > div > div.col-md-12 > label').click()
print(Same_as_client_mail_address)

Debtor_Invoice = driver.find_element_by_link_text('Invoice Details').click()
print(Debtor_Invoice)





