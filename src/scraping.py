from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    # Set up Edge options to run in headless mode
    options = Options()
    options.headless = True

    # Initialize Edge WebDriver with the specified service and options
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    driver.get(url)

    driver.implicitly_wait(10)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')
    # strongs = soup.find_all('strong')
    # ems = soup.find_all('em')
    h1s = soup.find_all('h1')
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    h4s = soup.find_all('h4')
    h5s = soup.find_all('h5')
    h6s = soup.find_all('h6')

    scraped_data = ""

    # Create a text file and write the extracted data
    
    for p in paragraphs:
        scraped_data += p.text + '\n'
        
    for h in h1s:
        scraped_data += h.text + '\n'
        
    for h in h2s:
        scraped_data += h.text + '\n'
        
    for h in h3s:
        scraped_data += h.text + '\n'

    for h in h4s:
        scraped_data += h.text + '\n'

    for h in h5s:
        scraped_data += h.text + '\n'
    
    for h in h6s:
        scraped_data += h.text + '\n'

    driver.quit()

    print(scraped_data)

    return scraped_data

# x = scrape_website("https://www.amazon.eg/-/en/Laptops/b?ie=UTF8&node=21832907031")
# with open("scraped_data.txt", mode="w") as file:
#         file.write(x + '\n')
