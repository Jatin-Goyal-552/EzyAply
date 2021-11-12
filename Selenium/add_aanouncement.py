
from selenium import webdriver
from selenium.webdriver.common.by import By

excutablePath = "C:\webdrivers\chromedriver.exe"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=excutablePath, options=options)

driver.get("http://ezzyaply.pythonanywhere.com/login/?next=/")
driver.maximize_window()

nameInput = driver.find_element(By.ID, "your_name")
nameInput.send_keys("admin")

passInput = driver.find_element(By.ID, "your_pass")
passInput.send_keys("admin")

signInBtn = driver.find_element(By.ID, "signin")
signInBtn.click()

makeAnnouncementBtn = driver.find_element(By.LINK_TEXT, "Make Announcement")
makeAnnouncementBtn.click()

dateInput = driver.find_element(By.ID, "id_announcement_date")
dateInput.click()
dateInput.send_keys("09/11/2021")

announcementTextField = driver.find_element(By.ID, "id_announcement_text")
announcementTextField.click()
announcementTextField.send_keys("Viva is scheduled today ")

submitBtn = driver.find_element(By.CSS_SELECTOR, ".contact100-form-btn")
submitBtn.click()
driver.close()
