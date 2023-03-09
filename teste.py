from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.youtube.com")

driver.find_element_by_id("search").send_keys('eminem cleanin out my closet')

driver.find_element_by_css_selector("#search-icon-legacy").click()

sleep(3)

res = driver.find_element_by_css_selector('#title-wrapper > h3').text

driver.find_element_by_partial_link_text('Eminem - Cleanin').click()

print(res)
sleep(5)
driver.close()


