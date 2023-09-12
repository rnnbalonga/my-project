from selenium import webdriver


class Scraper:
    def __init__(self):
        self.chrome_driver_path = r"D:\Installers\chromedriver_win32\chromedriver.exe"
        #This opens selenium browser
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/")
        input()
        self.driver.quit()

