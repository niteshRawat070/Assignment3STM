from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

driver.get("https://www.asos.com/")
time.sleep(3)
search_bar = driver.find_element("id","chrome-search")
search_bar.send_keys("shirt")

search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

assert "shirt" in driver.title

select_radio = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/header/section/div/div/div/a[1]");
select_radio.click()

time.sleep(5)

laptop_link = driver.find_element("xpath","/html/body/div[1]/div/main/div/div/div[1]/div[2]/div/div[1]/section/article[1]/a/div[1]/img");

laptop_link.click()

time.sleep(5)


# Closing the webdriver
driver.close()
