from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# specify the path to the chromedriver.exe file and login credentials
chromedriver_path = '/usr/bin/chromedriver'
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
product_name = "Samsung Galaxy A54"

options = Options()
custom_user_agent = "Mozilla/5.0 (Linux; Android 11; 100011886A Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Safari/537.36"
options.add_argument(f'user-agent={custom_user_agent}')

# create a new instance of the Chrome driver
driver = webdriver.Chrome(chromedriver_path, options=options)


# navigate to Amazon.de and login to your account
driver.get('https://www.amazon.de/')
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID, 'ap_email').send_keys(email)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'ap_password').send_keys(password)
driver.find_element(By.ID, 'signInSubmit').click()

# search for the product you want to buy, click on its link and add it to the cart
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys(product_name)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element(By.XPATH, '//div[contains(@class,"s-result-item")]//span[contains(text(),"Amazon\'s")]').click()
time.sleep(2)
driver.find_element(By.ID, 'buy-now-button').click()
time.sleep(5)
# proceed to checkout
print(driver.find_element(By.XPATH, '//*[@id="subtotals-marketplace-table"]/tbody/tr[4]/td[2]').text)
time.sleep(10)
# close the browser
driver.quit()
