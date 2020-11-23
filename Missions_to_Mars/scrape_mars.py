# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import os
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
# Set Executable Path & Initialize Chrome driver

executable_path = {'executable_path':"chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# Create python dictionary that can be imported into Mongo
mars_news = {}
mars_urls = []

# NASA MARS NEWS

def scrape_news():
# Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

    # Scrape and collect the latest News Title and Paragraph Text
    latest_news_title = nasa_soup.find('div', class_='list_text').find('div', class_='content_title').find('a').text
    latest_news_p = nasa_soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
    # print(f"The latest Mars News Title is: {latest_news_title}")
    # print(f"The latest Mars News Paragraph is: {latest_news_p}")

    # Populate dictionary
    mars_news['latest_news_title']=latest_news_title
    mars_news['latest_news_p']=latest_news_p

    browser.quit()
    return mars_news

    # ## JPL Mars Space Images

    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)

    browser.quit()

    # In[7]:


    # Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    # and assign the url string to a variable

    img_html = browser.html

    img_soup = BeautifulSoup(img_html, "html.parser")

    parsed_img_url = img_soup.find('div', class_="carousel_items").find('article')['style'].    replace('background-image: url(', '').replace(');', '')[1:-1]

    root_img_url = "http://www.jpl.nasa.gov"

    featured_image_url = root_img_url + parsed_img_url

    featured_image_url


    # ## Mars Facts

    # In[8]:


    fact_url = "https://space-facts.com/mars/"
    browser.visit(fact_url)

    # Use Pandas to scrape the table fact 
    tables = pd.read_html(fact_url)

    tables                       


    # In[9]:


    # tables - find Mars Facts
    fact_df = tables[1]

    # Assign Columns
    fact_df.columns = ["Mars_Earth_Comparison", 'Mars_Fact', 'Earth_Fact']

    fact_df.set_index('Mars_Earth_Comparison', inplace=True)

    fact_df
        


    # In[10]:


    # Convert the dataframe to html
    fact_html_tb = fact_df.to_html(classes = 'table table-striped')

    fact_html_tb


    # In[11]:


    # Strip unwanted new lines
    fact_html_tb.replace('\n', '')


    # ## Mars Hemispheres

    # ## Cerberus Hemisphere Enhanced

    # In[12]:


    cer_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

    browser.visit(cer_url)
    cer_html = browser.html
    cer_soup = BeautifulSoup(cer_html, "html.parser")
    cer_url = cer_soup.find_all('div', class_= 'downloads')[0].li.a.get('href')

    cer_url


    # ## Schiaparelli Hemisphere Enhanced

    # In[13]:


    sch_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

    browser.visit(sch_url)
    sch_html = browser.html
    sch_soup = BeautifulSoup(sch_html, "html.parser")
    sch_url = sch_soup.find_all('div', class_= 'downloads')[0].li.a.get('href')

    sch_url


    # ## Syrtis Major Hemisphere Enhanced

    # In[14]:


    sm_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

    browser.visit(sm_url)
    sm_html = browser.html
    sm_soup = BeautifulSoup(sm_html, "html.parser")
    sm_url = sm_soup.find_all('div', class_= 'downloads')[0].li.a.get('href')

    sm_url


    # ##  Valles Marineris Hemisphere Enhanced

    # In[15]:


    vm_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    browser.visit(vm_url)
    vm_html = browser.html
    vm_soup = BeautifulSoup(vm_html, "html.parser")
    vm_url = vm_soup.find_all('div', class_= 'downloads')[0].li.a.get('href')

    vm_url


    # In[16]:


    # Create a dictionary with hemisphere title and full imagine url
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": vm_url},
        {"title": "Cerberus Hemisphere", "img_url": cer_url},
        {"title": "Schiaparelli Hemisphere", "img_url": sch_url},
        {"title": "Syrtis Major Hemisphere", "img_url": sm_url},
    ]

    hemisphere_image_urls


    # In[17]:


browser.quit()

