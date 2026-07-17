from bs4 import BeautifulSoup
import requests
import sys

def scrape_soundcloud():
    url = sys.argv[1]
    url=url+"/sets"
    # Get the web page content
    response = requests.get(url)
 
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #get the user's profile ending
    user_url = url[22:]
    
    #Find and print all the links
    for link in soup.find_all('a'):
        link_string=link.get('href')
        if user_url in link_string and user_url!=link_string:
            print(link_string[link_string.index("sets/")+5:].replace(" ","_") + " ",end="")
            print(url[:22]+link_string + " ", end="")


scrape_soundcloud()
