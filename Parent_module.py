from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# set the Executable path in C drive
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
time.sleep(5)

# Input the User email id for lofing the Qlicr Engine
user_ele.send_keys("tarun.soni@arlabhq.in")

# Input the Password for loging the Qlicr Engine
pwd_ele.send_keys("Arlab@01")


driver.find_element_by_name("btnLogin").click()  # Click the Login Button

time.sleep(10)

# Open the Parent Module

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))   # How many links are available in Qlicr Engine

Par_ent = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientParents")
print(Par_ent)

time.sleep(5)
# User Add New Parent in the Qlicr Engine
Sec_class = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientparent")
print(Sec_class)

# check how many Input fields are presence in the General Section
input_box = driver.find_elements(By.CLASS_NAME,'text')
print(len(input_box))

# Input the name of the New Parent in the Name fields
Parent_name = driver.find_element_by_name('companyName').send_keys('Arlabcompany')
print(Parent_name)
#driver.find_element_by_name('companyAbn').send_keys("55 620 817 665")

# Select option from the dropdown list
time.sleep(5)
Par_owner = driver.find_element_by_name('parentOwnerId')    # Parent Fileds
drp = Select(Par_owner)
print(drp)
time.sleep(5)
drp.select_by_visible_text('vinay parashar')
time.sleep(5)
drp.select_by_visible_text('bhanu singh')
time.sleep(5)
'''drp.select_by_visible_text('Trun kumar')'''

# Count the Parent Owner  in the dropdown list
print(len(drp.options))

# Check all the Parent Owner Name from the Dropdown list
all_options = drp.options
for option in all_options:
    print(option.text)



off_code = driver.find_element_by_name('officeCodeId')   # Office Fields of the Parent Module
code = Select(off_code)
print(code)
time.sleep(5)
code.select_by_visible_text('600 - Torque WA')

# Count  the Office Code from the dropdown list
print(len(code.options))

# Check all the Office Code from the dropdown list
all_code = code.options
for code in all_code:
    print(code.text)


status = driver.find_element_by_name('companyStatus')   # Status fields of the Parent Module
User_stat = Select(status)
print(User_stat)
time.sleep(5)
User_stat.select_by_visible_text('Active')

# Count the status from the dropdown list
print(len(User_stat.options))



# Check all the Status from the dropdown list

all_status = User_stat.options
for User_stat in all_status:
    print(User_stat.text)


Par_type = driver.find_element_by_name('companyType')    # Parent Type fields
P_type = Select(Par_type)
P_type.select_by_visible_text('Professional')

# Count the Parent type from the dropdown list
print(len(P_type.options))

# Check all the Parent type from the dropdown list

all_Ptype = P_type.options
for P_type in all_Ptype:
    print(P_type.text)

time.sleep(10)
Abn_no = driver.find_element_by_css_selector('#ctab1 > section > section > div > div > div:nth-child(8) > div > div > input').send_keys(Keys.HOME,'51824753556')
print(Abn_no)
time.sleep(20)
#2 input the value in Input boxes
#driver.find_element(By.NAME,'companyAbn').send_keys('12 453 434 343')


# Profile Section of the Parent Module
profile = driver.find_element_by_link_text('Profile').click()
#print(profile)
time.sleep(5)
Par_com_profile = driver.find_element_by_name('companyProfile').send_keys('testing')
print(Par_com_profile)

Par_com_notes = driver.find_element_by_name('companyNotes').send_keys('Arlab Company')
print(Par_com_notes)


# Address Section of the Parent Module

Address = driver.find_element_by_link_text('Address').click()
print(Address)

time.sleep(5)
Add_line1 = driver.find_element(By.NAME,'mainAddress1').send_keys('Australia')
print(Add_line1)

Add_line2 = driver.find_element(By.NAME,'mainAddress2').send_keys('line')
print(Add_line2)

City_Sub = driver.find_element_by_css_selector("#ctab3 > section > section > div > div > div:nth-child(5) > div > input").send_keys("line")
print(City_Sub)

State_prov = driver.find_element_by_name('mainState')
Sel_state = Select(State_prov)
Sel_state.select_by_visible_text('VIC')

Post_code = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(7) > div > input').send_keys('3333')
print(Post_code)

# Mailing Address

Mail_Add1 = driver.find_element(By.NAME,'mailingAddress1').send_keys('Australia')
Mail_Add2 = driver.find_element(By.NAME,'mailingAddress2').send_keys('line')

City_Sub1 = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(14) > div > input').send_keys('Line')
print(City_Sub1)

State_prov1 = driver.find_element_by_name('mailingState')
Sel_state1 = Select(State_prov1)
Sel_state1.select_by_visible_text('VIC')

Post_code1 = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(16) > div > div > input').send_keys('3333')
print(Post_code1)
time.sleep(5)

#Add_line2 = driver.find_element_by_name('mainAddress2').send_keys('Line')
#Post_code = driver.find_element(By.xpath("/html/body/div/section/section/section/section/section/div/div/div[7]/div[3]/div/div[3]/section/section/div/div/div[7]/div/input")).send_keys("3333")
#print(Post_code)

Save_Parent  = driver.find_element_by_name("Save").click()
print(Save_Parent)



time.sleep(10)
Par_Edit_Profile = driver.find_element_by_css_selector("#content > section > div > div > div.col-md-4.col-sm-4.text-right.mb-10 > div > button").send_keys(Keys.RETURN)
print(Par_Edit_Profile)

Par_link_client = driver.find_element_by_link_text('Linked Client').click()
print(Par_link_client)

Par_link_contact = driver.find_element_by_link_text('Linked Contact').click()
print(Par_link_contact)

Par_Audit = driver.find_element_by_link_text('Audit Trail').click()
print(Par_Audit)

# Save the Profile of the Parent Module

Save_parent_module  = driver.find_element_by_name("Save").click()
print(Save_parent_module)