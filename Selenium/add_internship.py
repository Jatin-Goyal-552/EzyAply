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

element=driver.find_element(By.LINK_TEXT, "Add Internship")
element.click()

element=driver.find_element(By.ID, "id_company_name")
element.send_keys("Siemens")

element=driver.find_element(By.ID, "id_intern_role")
element.send_keys("Deep Learning Developer")

element=driver.find_element(By.ID, "id_description")
element.send_keys("Siemens work in field of deep learning.")

element=driver.find_element(By.ID, "id_duration")
element.send_keys("6")

element=driver.find_element(By.ID, "id_cpi")
element.send_keys("7")

element=driver.find_element(By.ID, "id_semester")
element.send_keys("6")

element=driver.find_element(By.ID, "id_stipend")
element.send_keys("50000")

element=driver.find_element(By.ID, "id_date")
element.send_keys("09-11-2021 15:00")

element=driver.find_element(By.ID, "id_other_qualifications")
element.send_keys("Candidate should be good in coding and know how to train a deep learning model.")

element=driver.find_element(By.CSS_SELECTOR, ".contact100-form-btn")
element.click()
