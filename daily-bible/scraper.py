from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class WebScraper:
    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), 
                                options=options)
        
    def scrape_verse(self, query):
    # Navigate to the url
        self.driver.get('https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/')

        # Clear Text from the search bar
        self.driver.find_element(By.NAME, "quicksearch").clear()

        # Enter Text
        self.driver.find_element(By.NAME, "quicksearch").send_keys(query)

        # CLick Button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[1]/div/form/div[1]/div[2]/button").click()

        #Get the passage location
        self.verse_ref = self.driver.find_element(By.CLASS_NAME, "dropdown-display-text").text
        #Get the verse
        verse = self.driver.find_element(By.CLASS_NAME, "passage-text" ).text
        print(verse)
        #Closes Driver
        self.driver.quit()