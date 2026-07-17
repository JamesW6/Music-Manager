
# Source - https://stackoverflow.com/a/35905689
# Posted by Florent B., modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-16, License - CC BY-SA 3.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import sys
import time

def scrape_yt(): 
    url=sys.argv[1]
    url+="/playlists"
    driver = webdriver.Firefox()
    driver.get(url)
    
    time.sleep(5)
    links=driver.find_elements(By.TAG_NAME, "a")
    
    for playlist in links:
        link=playlist.get_attribute("href")
        if type(link)!=type(None) and  "/playlist?" in link: 
            print(playlist.text.replace(" ","_")+" ",end="")
            print(link+" ",end="")
scrape_yt()


