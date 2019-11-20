#Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import datetime
import time
import pymongo

# Initialize browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
# NASA Mars News      

    # Target URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)
    
    # Scrape page into Soup
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    mars_info_dict = {}

    # Get the first news title
    news_title = soup.find('div', class_='content_title').text

    # Get the first news paragraph
    news_p = soup.find('div', class_='article_teaser_body').text

# JPL Mars Space Images - Featured Image

    # Target URL
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    time.sleep(1)

    # Scrape page into Soup
    # HTML object
    html2 = browser.html
    # Parse HTML with Beautiful Soup
    soup2 = bs(html2, 'html.parser')

    # Retrieve the image url for the current Featured Mars Image and assign the url string to a variable
    # https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/
    image_url = soup2.find('article')['style'][23:-3]

    # Establishing the full url for the image source
    featured_image_url = f'{url2[0:24]}{image_url}'
        
# Mars Weather

    # Target URL
    url3 = 'https://twitter.com/marswxreport'
    browser.visit(url3)

    time.sleep(1)

    # Scrape page into Soup
    # HTML object
    html3 = browser.html
    # Parse HTML with Beautiful Soup
    soup3 = bs(html3, 'html.parser')

    # Retrieve the latest tweet about weather
    mars_weather = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

# Mars Facts

    # Target URL
    url4 = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(url4)

    # Assign the first list of tables to a DataFrame
    df_1 = tables[0]

    # Assign the column names
    df_1.columns = ["Specifications", "Values"]

    # Generate HTML table from DataFrame
    html_table_1 = df_1.to_html()

# Mars Hemispheres

    # Target URL
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    time.sleep(1)

    # Scrape page into Soup
    # HTML object
    html5 = browser.html
    # Parse HTML with Beautiful Soup
    soup5 = bs(html5, 'html.parser')

    # Find all information about the items on the page
    all_items = soup5.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    list_of_urls = []

    # Assign a variable named main_url 
    main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in all_items: 
        # Store title
        title = i.find('h3').get_text()
            
        # Assign url to a variable that leads to the page where full images are stored
        source_img_url = i.find('a', class_='itemLink product-item')['href']
            
        # Visit the page where full images are stored 
        browser.visit(main_url + source_img_url)

        time.sleep(1)

        # Scrape page into Soup    
        # HTML Object
        source_img_html = browser.html
        # Parse HTML with Beautiful Soup
        soup6 = bs(source_img_html, 'html.parser')
            
        # Pull full image source url information
        img_url = main_url + soup6.find('img', class_='wide-image')['src']

        # Append the retrieved information into a list of dictionaries 
        list_of_urls.append({"title" : title, "img_url" : img_url})

    # Store data in a dictionary
    mars_info_dict = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": html_table_1,
        "list_of_urls": list_of_urls,
        "last_updated": datetime.datetime.utcnow()
    }
 

    # Return Mars Info dictionary
    return mars_info_dict
