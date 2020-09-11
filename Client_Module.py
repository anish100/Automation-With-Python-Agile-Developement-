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

# Input the User email id for lofing the Qlicr Engine
user_ele.send_keys("tarun.soni@arlabhq.in")
time.sleep(5)
# Input the Password for loging the Qlicr Engine
pwd_ele.send_keys("Arlab@01")
time.sleep(5)

driver.find_element_by_name("btnLogin").click()  # Click the Login Button

time.sleep(10)

# Open the Parent Module

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))   # How many links are available in Qlicr Engine

Par_ent = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientParents")
print(Par_ent)

time.sleep(5)
# Click On Client Module
Clie_nt = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clients")
print(Clie_nt)

time.sleep(5)

Client_add = driver.get("http://migration.arlabhq.com.s3-website-ap-southeast-2.amazonaws.com/clientInfo")
print(Client_add)

# General Section of the Client -------------------------------------


time.sleep(5)
Client_name = driver.find_element_by_name('clientName').send_keys("Thomson")
print(Client_name)
#Save the Client Profiles
driver.find_element_by_name("Save").click()
time.sleep(10)


# Edit the Client Profile
Edit_Profile = driver.find_element_by_css_selector("#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(2)").send_keys(Keys.RETURN)
print(Edit_Profile)


time.sleep(5)
Client_depart = driver.find_element_by_name('department').send_keys('Hr')
print(Client_depart)

#time.sleep(5)
Client_type = driver.find_element_by_name('clientType')
drp = Select(Client_type)
drp.select_by_visible_text('Professional')
time.sleep(5)
drp.select_by_visible_text('Trades & Industrial')
#time.sleep(5)
#drp.select_by_visible_text('White Collar Office')  ########

# Count the Parent Owner  in the dropdown list
print(len(drp.options))
# Check all the Parent Owner Name from the Dropdown list
all_options = drp.options
for option in all_options:
    print(option.text)

'''Client_status = driver.find_element_by_name('status')   # Status fields of the Parent Module
User_stat = Select(Client_status)
print(User_stat)
time.sleep(5)
User_stat.select_by_visible_text('Active')'''


time.sleep(5)
Client_owner = driver.find_element_by_name('clientOwnerId')
drp_down = Select(Client_owner)
#drp.select_by_visible_text('bhanu singh')

time.sleep(5)

off_code = driver.find_element_by_name('officeCodeId')   # Office Fields of the Client  Module
code = Select(off_code)
print(code)
time.sleep(5)
code.select_by_visible_text('300 - Torque VIC')

# Count  the Office Code from the dropdown list
print(len(code.options))
time.sleep(5)
# Check all the Office Code from the dropdown list
'''all_code = code.options
for code in all_code:
    print(code.text)'''

'''Land_line = driver.find_element_by_css_selector('#general > section > div > div > div:nth-child(10) > div > div > input').send_keys(Keys.RETURN)

print(Land_line)'''

Abn_no = driver.find_element_by_css_selector('#general > section > div > div > div:nth-child(13) > div > div > input').send_keys(Keys.HOME,'51824753556')
print(Abn_no)

time.sleep(10)


# Address Section of the Parent Module

Address = driver.find_element_by_link_text('Address').click()
time.sleep(5)
Add_line1 = driver.find_element(By.NAME,'mainAddress1').send_keys('street')
print(Add_line1)

Add_line2 = driver.find_element(By.NAME,'mainAddress2').send_keys('line')
print(Add_line2)

City_Sub = driver.find_element_by_css_selector("#ctab3 > section > section > div > div > div:nth-child(5) > div > input").send_keys("line")
print(City_Sub)

State_prov = driver.find_element_by_name('mainState')
Sel_state = Select(State_prov)
Sel_state.select_by_visible_text('NSW')

Post_code = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(7) > div > input').send_keys('3333')
print(Post_code)

# Mailing Address

time.sleep(5)
Mail_Add1 = driver.find_element(By.NAME,'mailingAddress1').send_keys('street')
Mail_Add2 = driver.find_element(By.NAME,'mailingAddress2').send_keys('line')

City_Sub1 = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(14) > div > input').send_keys('Line')
print(City_Sub1)

State_prov1 = driver.find_element_by_name('mailingState')
Sel_state1 = Select(State_prov1)
Sel_state1.select_by_visible_text('NSW')

Post_code1 = driver.find_element_by_css_selector('#ctab3 > section > section > div > div > div:nth-child(16) > div > div > input').send_keys('3333')
print(Post_code1)





# Workplace Section

Work_place = driver.find_element_by_link_text('Workplace').click()
print(Work_place)
time.sleep(5)
Work_des = driver.find_element_by_name('workplaceDescription').send_keys('Yes')
print(Work_des)
time.sleep(5)

Cloth_des = driver.find_element_by_name('clothingDressRequirements').send_keys('Yes')
print(Cloth_des)
time.sleep(5)

Travel_ins = driver.find_element_by_name('travelInstructions').send_keys('Yes')
print(Travel_ins)
time.sleep(5)

Meal_Amen = driver.find_element_by_name('mealAmenities').send_keys('Yes')
print(Meal_Amen)

Inspection_date = driver.find_element_by_css_selector('#Workplace > section > div > div > div.col-lg-3.col-md-3.col-sm-4.col-xs-12 > div > div > div.react-datepicker-wrapper > div > input').send_keys('10102011')
print(Inspection_date)
#print(Inp_select)



#Save the Client Profile
'''driver.find_element_by_name("Save").click()
time.sleep(10)


# Edit the Client Profile
Edit_Profile = driver.find_element_by_css_selector("#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(2)").send_keys(Keys.RETURN)
print(Edit_Profile)'''


#Linking of the Contact
Link_Contact = driver.find_element_by_link_text('Contacts').click()
print(Link_Contact)

Add_contact = driver.find_element_by_css_selector('#linkedContact > header > button:nth-child(3)').click()
print(Add_contact)
time.sleep(10)

# Contact Profile
First_name = driver.find_element_by_name('firstName').send_keys('Flintop')
print(First_name)
time.sleep(5)

Last_name = driver.find_element_by_name('lastName').send_keys('Andrew')
print(Last_name)
time.sleep(5)

Contact_title = driver.find_element_by_name('contactTitle').send_keys('Hr')
print(Contact_title)
time.sleep(5)
Contact_email = driver.find_element_by_name('email').send_keys("and1@example.com")
print(Contact_email)


Contact_land_no = driver.find_element_by_css_selector('#ctab1 > section > section > div > div > div:nth-child(11) > div > div > input').send_keys(Keys.HOME,'123456789')
print(Contact_title)
time.sleep(5)


time.sleep(10)
Contact_email = driver.find_element_by_name('email').send_keys("andxx@example.com")
print(Contact_email)
time.sleep(10)
Contact_save = driver.find_element_by_name("Save").click()
print(Contact_save)

time.sleep(10)
Contact_Back = driver.find_element_by_css_selector('#content > section > div > div > div:nth-child(3) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(1)').click()
print(Contact_Back)


time.sleep(10)
# Paybill section of the Client profile

Pay_bill = driver.find_element_by_link_text('Pay / Bill').click()
print(Pay_bill)
Edit_paybill =driver.find_element_by_css_selector('#content > section > div > div > div:nth-child(4) > div.pull-right.text-right.mt-5.mb-10 > div > button:nth-child(2)').click()
print(Edit_paybill)
time.sleep(10)
Work_cover = driver.find_element_by_name('workCoverStateId')
Work_sel = Select(Work_cover)
Work_sel.select_by_visible_text('New South Wales')
time.sleep(10)

'''Work_cover_code = driver.find_element_by_name('workCoverCodeId')
Work_sel = Select(Work_cover_code)
Work_sel.select_by_visible_text('trt')'''

Payroll_tax = driver.find_element_by_name('payrollTaxStateId')
Payroll_sel = Select(Payroll_tax)
Payroll_sel.select_by_visible_text('New South Wales')
time.sleep(10)

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



# Job Section of the clicent Profile

Job_Sec = driver.find_element_by_link_text('Jobs').click()
print(Job_Sec)

time.sleep(10)


# Template of the clicen Module

Temp_late = driver.find_element_by_link_text('Template').click()
print(Temp_late)

time.sleep(10)


# Task section of the Client Module

'''Task_sec = driver.find_element_by_link_text('Tasks').click()
print(Task_sec)'''





# Attachment section of the Client Module
time.sleep(10)
Attach_mnt = driver.find_element_by_link_text('Attachment').click()
print(Attach_mnt)





