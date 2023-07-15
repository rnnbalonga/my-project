from selenium import webdriver

chrome_driver_path = r"D:\Installers\chromedriver_win32\chromedriver.exe"

#This opens selenium browser
driver = webdriver.Chrome()

driver.get("https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/")

input()

driver.quit()

