import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/DOM/Downloads/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://adviserinfo.sec.gov/IAPD/InvestmentAdviserData.aspx');
driver.find_element_by_link_text("Investment Adviser Representatives Report").click()
time.sleep(120) #wait until the file gets saved before closing the browser
driver.quit()
print('Process ended')