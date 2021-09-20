from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    #Find one record of data from the mongo database
    data = mongo.db.mars.find_one()
    return render_template("index.html", mars= data)

#Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    #run the scrape function and save the results to a varaiable
    mars_info =scrape_mars.init_browser()
    mongo.db.mars.update({}, mars_info, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)