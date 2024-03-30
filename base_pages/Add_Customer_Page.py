import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Add_Customer_Page:

    # locators from add customer page
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuoption_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"
    link_addnew_xpath = "//div[@class='float-right']/a"
    text_email_id = "Email"
    text_password_id = "Password"
    text_fname_id = "FirstName"
    text_lname_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_dob_id = "DateOfBirth"
    text_companyname_id = "Company"
    chbx_tax_exempt_id = "IsTaxExempt"
    newsletter_cusrole_list_xpath = "//div[@role='listbox']"  # it gives 2 elements
    cusrole_guests_xpath = "//li[contains(text(),'Guests')]"
    cusrole_administrators_xpath = "//li[contains(text(),'Administrators')]"
    cusrole_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    cusrole_registered_xpath = "//li[contains(text(),'Registered')]"
    cusrole_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdwn_mngrofvendor_id = "VendorId"
    text_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()

    def click_customers_from_menu_options(self):
        self.driver.find_element(By.XPATH,self.link_customer_menuoption_xpath).click()

    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.link_addnew_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID, self.text_fname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID, self.text_lname_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()

    def enter_dob(self,dob):
        self.driver.find_element(By.ID, self.text_dob_id).send_keys(dob)

    def enter_companyname(self,companyname):
        self.driver.find_element(By.ID, self.text_companyname_id).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID,self.chbx_tax_exempt_id).click()
        time.sleep(3)

    def select_newsletter(self,value):
        elements = self.driver.find_elements(By.XPATH,self.newsletter_cusrole_list_xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH,"//li[contains(text(),'Your store name')]").click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH,"//li[contains(text(),'Test store 2')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()

    def select_customer_role(self,role):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)
        cusrole_field = elements[1]
        cusrole_field.click()
        time.sleep(3)
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(3)
            cusrole_field.click()
            self.driver.find_element(By.XPATH, self.cusrole_guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH,self.cusrole_administrators_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH,self.cusrole_forummoderators_xpath).click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH,self.cusrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.cusrole_administrators_xpath).click()

    def select_manager_of_vendor(self,value):
        drp_dwn = Select(self.driver.find_element(By.ID, self.drpdwn_mngrofvendor_id))
        drp_dwn.select_by_visible_text(value)

    def enter_admin_comments(self,admincomments):
        self.driver.find_element(By.ID, self.text_admincomment_id).send_keys(admincomments)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()

