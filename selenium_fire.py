import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parsingexcel
from parsingexcel import parse_excel

class PythonOrgSearch(unittest.TestCase,parsingexcel.parse_excel):
    #Default username and password if no values supplied 
    username = "pankaj"
    password = "mishra"

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        self.assertIn("Facebook", driver.title)
        elem_user = driver.find_element_by_xpath("//input[@id='email']")
        elem_user.send_keys(self.username)
        elem_password=driver.find_element_by_xpath("//input[@id='pass']")
        elem_password.send_keys(self.password)
        import time
        time.sleep(5)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    ab=parse_excel()
    parsed_data=ab.convert_data_dict()
    for key, value in parsed_data.items():
        PythonOrgSearch.username=key
        PythonOrgSearch.password=value
        #suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
        #unittest.TextTestRunner(verbosity=2).run(suite)
        unittest.main(exit=False)