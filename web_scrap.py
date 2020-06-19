from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Part_1
# print(driver.title)
#
# search = driver.find_element_by_name("as_word")
# search.send_keys("rtx2060")
# search.send_keys(Keys.RETURN)
#
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "searchResults"))
#     )
#     print(main.text)
# finally:
#     driver.quit()
#
# Part 2
# link = driver.find_element_by_link_text("Computación")
# link.click()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Computación"))
#     )
#     element.clear()
#     element.click()
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Mouses"))
#     )
#     element.click()
#
#     driver.back()
#     driver.back()
#     driver.forward()
# except:
#     driver.quit()
#
# Part03
#
# driver.implicitly_wait(5)
#
# cookie = driver.find_element_by_id("bigCookie")
# cookie_count = driver.find_element_by_id("cookies")
# items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]
#
# actions = ActionChains(driver)
# actions.click(cookie)
#
# for i in range(5000):
#     actions.perform()
#     count = int(cookie_count.text.split(" ")[0])
#     for item in items:
#         value = int(item.text)
#         if value <= count:
#             upgrade_actions = ActionChains(driver)
#             upgrade_actions.move_to_element(item)
#             upgrade_actions.click()
#             upgrade_actions.perform()





