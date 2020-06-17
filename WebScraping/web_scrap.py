from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mercadolibre.com.ar/")
print(driver.title)

search = driver.find_element_by_name("as_word")
search.send_keys("rtx2060")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchResults"))
    )
    publications = main.find_elements_by_class_name("item__price")
    print(main.text)
    # for publication in publications:
    #     publication_title = publications.find_elements_by_tag_name("main-title")
    #     print(publication_title.text)
    #     price = publications.find_elements_by_tag_name("price__fraction")
    #     print(price.text)
finally:
    driver.quit()

