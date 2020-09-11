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
time.sleep(5)
# Enter the Password of the Qlicr Engine
pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

# Input the User email id for lofing the Qlicr Engine
user_ele.send_keys("tarun.soni@arlabhq.in")

# Input the Password for loging the Qlicr Engine
pwd_ele.send_keys("Arlab@01")

driver.find_element_by_name("btnLogin").click()  # Click the Login Button

time.sleep(10)

Edit_client = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientInfo/300015155")
print(Edit_client)
time.sleep(5)

Edit_Profile = driver.find_element_by_css_selector("#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(2)").send_keys(Keys.RETURN)
print(Edit_Profile)

Link_Contact = driver.find_element_by_link_text('Contacts').click()
print(Link_Contact)

Contact_lin = driver.find_element_by_css_selector('#adv-search-component1 > div > div > div').click()
print(Contact_lin)

Contact_link_name = driver.find_element_by_css_selector('#searchboxmodal1 > div > div > div.modal-body > div:nth-child(1) > div > div > input').send_keys('600000112')
print(Contact_link_name)

Contact_search_click = driver.find_element_by_css_selector('#searchboxmodal1 > div > div > div.modal-body > div:nth-child(1) > div > div > span').click()
print(Contact_search_click)

Contact_sel = driver.find_element_by_css_selector('#adv-search-component1 > div > div > input').send_keys('600000112')
print(Contact_sel)
sel = Select(Contact_sel)
print(sel)
#Linked_contact = driver.find_element_by_css_selector('#linkedContact > header > button:nth-child(2)').click()
#print(Link_Contact)









''''Pay_bill = driver.find_element_by_link_text('Pay / Bill').click()
print(Pay_bill)

Work_cover = driver.find_element_by_name('workCoverStateId')
Work_sel = Select(Work_cover)
Work_sel.select_by_visible_text('New South Wales')
time.sleep(10)

Work_cover_code = driver.find_element_by_name('workCoverCodeId')
Work_sel = Select(Work_cover_code)
Work_sel.select_by_visible_text('trt') 

Payroll_tax = driver.find_element_by_name('payrollTaxStateId')
Payroll_sel = Select(Payroll_tax)
Payroll_sel.select_by_visible_text('New South Wales')

Work_cover_code = driver.find_element_by_name('workCoverCodeId')
Work_sel = Select(Work_cover_code)
Work_sel.select_by_visible_text('trt')

time.sleep(10)

Trade_ref_check = driver.find_element_by_css_selector('#pay > section > div > div:nth-child(4) > div.col-lg-10.col-md-10.col-sm-10.col-xs-12 > label:nth-child(1) > label').click()
print(Trade_ref_check)

Credit_check = driver.find_element_by_css_selector('#pay > section > div > div:nth-child(4) > div.col-lg-10.col-md-10.col-sm-10.col-xs-12 > label:nth-child(2) > label').click()
print(Credit_check)

Term_condition = driver.find_element_by_css_selector('#pay > section > div > div:nth-child(4) > div.col-lg-10.col-md-10.col-sm-10.col-xs-12 > label:nth-child(3) > label').click()
print(Term_condition)
time.sleep(5)

Save_Button = driver.find_element_by_name("Save").click()
print(Save_Button)
time.sleep(10)


Edit_button = driver.find_element_by_css_selector("#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(2)").send_keys(Keys.RETURN)
print(Edit_button)

time.sleep(10)









Job_Sec = driver.find_element_by_link_text('Jobs').click()
print(Job_Sec)

Temp_late = driver.find_element_by_link_text('Template').click()
print(Temp_late)

Task_sec = driver.find_element_by_link_text('Tasks').click()
print(Task_sec)

Attach_mnt = driver.find_element_by_link_text('Attachment').click()
print(Attach_mnt)'''


#driver.find_element(By.CLASS_NAME,"pull-right text-right mt-5 mb-10").click()

