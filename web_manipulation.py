from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

username = "username"
password = "password"

driver = webdriver.Chrome(r"C:\Users\ACER\Desktop\Dev\Python\web_manipulation\chromedriver")

driver.get("https://github.com/login")
driver.find_element(By.ID, "login_field").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
time.sleep(1.5)
driver.find_element(By.NAME, "commit").click()
driver.quit()