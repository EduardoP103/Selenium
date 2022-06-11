import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

website = 'http://www.google.com'
path = 'C:\Program files (x86)\chromedriver'


class prueba_selenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=path)

    def test_buscar_por_nombre(self):
        driver = self.driver
        driver.get(website)
        buscar_por_nombre = driver.find_element(By.NAME, 'q')
        time.sleep(2)
        buscar_por_nombre.send_keys("Ingresar a Portal Certus", Keys.ARROW_DOWN)
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if  __name__ == '__main__':
    unittest.main()

