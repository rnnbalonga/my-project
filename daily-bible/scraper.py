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
        self.path = "today_verse.txt"
    
    def open_site(self):
        # Navigate to the url
        self.driver.get('https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/')
        
    def scrape_verse(self, query):
        """
        This function will scrape the verse from the website using a string 'query' as input.
        """
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

        return verse
        #Closes Driver

    def collect_output_verse(self, current_verse):
        """
        Takes a list of verses and scrapes them one by one. Returns a dictionary of reference and verses.
        """
        
        current_day_output = []

        self.open_site()

        current_day_output = [{'reference': verse, 'verse': self.scrape_verse(verse)} for verse in current_verse]

        self.quit()

        self.store_verse(current_day_output)
    
    def store_verse(self, verse_list):
        """
        Store verse in a txt file for easy access
        """
        with open(self.path, 'w', encoding= "utf-8") as file:
            for item in verse_list:
                x = item['reference']
                y = item['verse']

                file.write(f'{x}\n')
                file.write(f'{y}')
                file.write("\n--------------------------- \n\n")


    def quit(self):
        """
        Closes the browser
        """
        self.driver.quit()



