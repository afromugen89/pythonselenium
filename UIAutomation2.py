from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

init_url = 'https://www.topdanmark.dk/'
topdanmarLogo = 'img[class="navbar-brand__logo"]'

try:
    #Open Chrome browser and go to topdanmark website
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.get(init_url)
    
    try:
        webPageIsLoaded = chromeBrowser.find_element_by_css_selector(topdanmarLogo)
    except:
        print("Webpage is not loaded on Chrome browser")

finally:
    chromeBrowser.close()

try:
    #Open Chrome browser and go to topdanmark website
    firefoxBrowser = webdriver.Firefox()
    firefoxBrowser.get(init_url)
    
    try:
        webPageIsLoaded = firefoxBrowser.find_element_by_css_selector(topdanmarLogo)
    except:
        print("Webpage is not loaded on Firefox browser")
          
finally:
    firefoxBrowser.close()

try:
    #Open Chrome browser and go to topdanmark website
    ieBrowser = webdriver.Ie()
    ieBrowser.get(init_url)
    
    try:
        webPageIsLoaded = ieBrowser.find_element_by_css_selector(topdanmarLogo)
    except:
        print("Webpage is not loaded on Chrome browser")
          
finally:
    ieBrowser.close()

