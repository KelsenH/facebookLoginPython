from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "")
driver.get ("https://www.facebook.com/")

usernameInput = driver.find_element_by_id ("email")
passwordInput = driver.find_element_by_id ("pass")
loginButton = driver.find_element_by_id ("loginbutton")

usernameInput.send_keys ("")
passwordInput.send_keys ("")
loginButton.click()





