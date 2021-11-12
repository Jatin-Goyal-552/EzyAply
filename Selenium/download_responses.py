from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()    
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe",chrome_options=options)

driver.get("http://ezzyaply.pythonanywhere.com/login/?next=/")
driver.maximize_window()

element=driver.find_element(By.ID, "your_name")
element.send_keys("admin")

element=driver.find_element(By.ID, "your_pass")
element.send_keys("admin")

element=driver.find_element(By.ID, "signin")
element.click()

element=driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/a[1]/img")
element.click()

element=driver.find_element(By.XPATH, "/html/body/div[1]/a[1]/button")
element.click()


