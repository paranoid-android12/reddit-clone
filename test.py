from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = 'why do you call it oven if you of in the cold food and out hot eat the food'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://inventwithpython.com/')

elements = driver.find_elements(By.CLASS_NAME, 'col-sm-12')
for element in elements:
    print("===\n" + element.text + "\n===\n\n")

driver.quit()