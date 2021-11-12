from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()    
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe",chrome_options=options)

driver.get("http://ezzyaply.pythonanywhere.com/login/?next=/")
driver.maximize_window()

element=driver.find_element(By.ID, "your_name")
element.send_keys("jatin2")

element=driver.find_element(By.ID, "your_pass")
element.send_keys("123789lk")

element=driver.find_element(By.ID, "signin")
element.click()

element=driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/a/button")
element.click()


element=driver.find_element(By.XPATH, "/html/body/div/div/form/div[11]/button")
element.click()

  
