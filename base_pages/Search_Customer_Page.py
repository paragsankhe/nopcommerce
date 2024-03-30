import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Search_Customer_Page:
    # locators from search customer page
    text_email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    text_cmpname_id = "SearchCompany"

    rows_table_xpath = "//table[@id='customers-grid']/tbody//tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self,driver):
        self.driver = driver

    def enter_customer_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_customer_firstname(self,fname):
        self.driver.find_element(By.ID, self.text_firstname_id).clear()
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(fname)

    def enter_customer_lastname(self,lname):
        self.driver.find_element(By.ID, self.text_lastname_id).clear()
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lname)

    def enter_customer_companyname(self,comp_name):
        self.driver.find_element(By.ID, self.text_cmpname_id).clear()
        self.driver.find_element(By.ID, self.text_cmpname_id).send_keys(comp_name)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_results_table_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.rows_table_xpath))

    def get_results_table_cols(self):
        return len(self.driver.find_elements(By.XPATH,self.columns_table_xpath))

    def search_customer_by_email(self,email):
        email_present_flag = False
        for r in range(1,self.get_results_table_rows()+1):
            cus_email = self.driver.find_element(By.XPATH,
                                                 "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[2]").text
            if cus_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self,name):
        name_present_flag = False
        for r in range(1, self.get_results_table_rows() + 1):
            cus_name = self.driver.find_element(By.XPATH,
                                                "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[3]").text
            if cus_name == name:
                name_present_flag = True
                break
        return name_present_flag

    def search_customer_by_company(self,company_name):
        cmpname_present_flag = False
        for r in range(1, self.get_results_table_rows() + 1):
            cus_name = self.driver.find_element(By.XPATH,
                                                "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[5]").text
            if company_name == company_name:
                cmpname_present_flag = True
                break
        return cmpname_present_flag




