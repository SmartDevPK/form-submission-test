from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()

file_path = "file://" + os.path.abspath("web-form.html")
driver.get(file_path)

driver.find_element(By.ID, "first_name").send_keys("MIchael")
driver.find_element(By.ID, "last_name").send_keys("Emmanuel")
driver.find_element(By.ID, "phone").send_keys("09056941102")
driver.find_element(By.ID, "email").send_keys("emmanuelmichaelpk3@gmail.com")
driver.find_element(By.ID, "state").send_keys("Plateau")
driver.find_element(By.ID, "city").send_keys("Jos")
driver.find_element(By.ID, "hobby").send_keys("Coding")
driver.find_element(By.ID, "subject").send_keys("Python")

driver.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(7)
message = driver.find_element(By.ID, "message").text

assert "successfully" in message.lower()

print("Test passed")

driver.quit()