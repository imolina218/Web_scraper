import unittest
from selenium import webdriver
import page


class PythonOrSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_title(self):
        main_page = page.MainPage()
        assert main_page.is_title_matches()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


