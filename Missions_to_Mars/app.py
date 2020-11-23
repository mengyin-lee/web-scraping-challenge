# Set up dependences
from flask import Flask, render_template
from flask import request
from flask import redirect
import scrape_mars
from pymongo import MongoClient
import pymongo

# Create an instance of Flask

# app = Flask(__name__, template_folder='../templates')
app = Flask(__name__)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars

@app.route("/")
def index():

    mars = db.mars.find_one()
    
    # Return template and data
    return render_template("index.html", mars = mars)

# Route that will trigger the scrape function    
@app.route("/scrape")
def scrape():

    # Run the scrape function
    # mars = client.db.mars
    mars = db.mars
    mars_news = scrape_mars.scrape_news()
    mars_news = scrape_mars.scrape_img()
    mars_news = scrape_mars.scrape_marsfact()
    mars_news = scrape_mars.scrape_cerhemi()
    mars_news = scrape_mars.scrape_schhemi()
    mars_news = scrape_mars.scrape_smhemi()
    mars_news  = scrape_mars.scrape_vmhemi()
    
    # Update the Mongo Database using update and upsert=True
    mars.update({}, mars_news, upsert=True)
    
    # Redirect back to home page
    return redirect("/", code=302)

# # Given Already
if __name__ == "__main__":
    app.run(debug=True)
