# web-scraping-challenge
## Mission to Mars
## Date: 11/24/2020

## *Step1*
> Jupyter Notebook mission_to_mars.ipynb - Scraping using BeautifulSoup, Splinter, Pandas
>> * NASA Mars News Site
>> * JPL Mars Space Images - Featured Image - Image changes when 'Scrape Mars Web Data' botton is clicked
>> * Mars Facts 
>> * Mars Hemispheres (4 Hemispheres) - Scraping from individual site to find the image url to the full resolution image

## *Step2* 
> MongoDB and Flask Application
>> * Run 'ipython nbconvert --to script mission_to_mars.ipynb
>> * Get mission_to_mars.py -> Rename to scrape_mars.py
>> * Modify scrape_mars.py to include functions and return scraped mars data
>> * Create app.py, including a route called /scrape that imports 'scrape_mars.py' script and call 'scrape' function
>> * Store the return scraped mars data in Mongo as a Python dictionary
>> * Create index.html in 'templates' directory that takes the mars data dictionary and display all of the data in the assigned html elements.

## *Output location*
>  Data export and webpage commited in the repository for reference
>> * Mongo data file: 'mars_db_collection_export.json'
>> * file folder: 'Mars Data_files'
>> * file folder: 'snapshots'



