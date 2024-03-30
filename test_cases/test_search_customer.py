import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Search_Customer_Page import Search_Customer_Page

class Test_04_Search_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("***********Test_04_001_Search_Customer with email started *************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("***********Login completed *************")
        self.logger.info("***********navigating to customer search page *************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** starting search customer by email *************")
        self.search_custmr = Search_Customer_Page(self.driver)
        self.search_custmr.enter_customer_email("arthur_holmes@nopCommerce.com")
        self.search_custmr.click_search_button()
        time.sleep(3)
        is_email_present = self.search_custmr.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.logger.info("***********Test_04_Search_customer by email test passed *************")
            self.driver.close()
        else:
            self.logger.info("***********Test_04_Search_customer by email test failed *************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.logger.info("***********Test_04_002_Search_Customer with name started *************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("***********Login completed *************")
        self.logger.info("***********navigating to customer search page *************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** starting search customer by name *************")
        self.search_custmr = Search_Customer_Page(self.driver)
        self.search_custmr.enter_customer_firstname("Arthur")
        self.search_custmr.enter_customer_lastname("Holmes")
        self.search_custmr.click_search_button()
        time.sleep(3)
        is_name_present = self.search_custmr.search_customer_by_name("Arthur Holmes")
        if is_name_present == True:
            assert True
            self.logger.info("***********Test_04_002_Search_customer by name test passed *************")
            self.driver.close()
        else:
            self.logger.info("***********Test_04_002_Search_customer by name test failed *************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_name.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_companyname(self,setup):
        self.logger.info("***********Test_04_003_Search_Customer with company name started *************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("***********Login completed *************")
        self.logger.info("***********navigating to customer search page *************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** starting search customer by company name *************")
        self.search_custmr = Search_Customer_Page(self.driver)
        self.search_custmr.enter_customer_companyname("Angel Star")
        self.search_custmr.click_search_button()
        time.sleep(3)
        is_cmpname_present = self.search_custmr.search_customer_by_company("Angel Star")
        if is_cmpname_present == True:
            assert True
            self.logger.info("***********Test_04_003_Search_customer by company name test passed *************")
            self.driver.close()
        else:
            self.logger.info("***********Test_04_003_Search_customer by company test failed *************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_companyname.png")
            self.driver.close()
            assert False
