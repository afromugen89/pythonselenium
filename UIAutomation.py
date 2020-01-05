from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

init_url = 'http://www.google.com/'
googleSearchBox = 'input[title="Search"]'
googleSearchBoxTopResultDropdownList = 'ul[class="erkvQe"] > li:nth-child(1) >div >div span'

try:
    #Open Chrome browser and go to google.com
    browser = webdriver.Chrome()
    browser.get(init_url)

    #Perform test and assert
    browser.find_element_by_css_selector(googleSearchBox).send_keys('topdanmark')
    waitForDropdown = WebDriverWait(browser,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,googleSearchBoxTopResultDropdownList)))
    firstRecord = browser.find_element_by_css_selector(googleSearchBoxTopResultDropdownList).text

    assert firstRecord == "topdanmark", "first record should be topdanmark"

finally:
    #Close browser after test is done
    browser.close()



