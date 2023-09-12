from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), 
                          options=options)

# Navigate to the url
driver.get('https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/')
# driver.maximize_window()

driver.find_element(By.NAME, "quicksearch").clear()

	# Enter Text
driver.find_element(By.NAME, "quicksearch").send_keys("psa 1" )

driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[1]/div/form/div[1]/div[2]/button").click()

verse_ref = driver.find_element(By.CLASS_NAME, "dropdown-display-text").text
verse = driver.find_element(By.CLASS_NAME, "passage-text" ).text
print(verse)

driver.quit()

# Close the driver
# driver.quit()

# class Scraper:
#     def __init__(self):
#         self.chrome_driver_path = r"D:\Installers\chromedriver_win32\chromedriver.exe"
#         #This opens selenium browser
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/")
#         input()
#         self.quit = self.driver.quit()

# scraper = Scraper()
# scraper.quit()