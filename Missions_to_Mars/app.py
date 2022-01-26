import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Setup connection to mongodb
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)

    # Select database and collection to use
#db = client.store_mars_data
#mars_collection = db.mars_collection

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    Mars_original = mongo.db.Mars_data.find_one()
    print(Mars_original)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", Mars_data=Mars_original)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    Mars_collection = mongo.db.Mars_data
    Mars_dict = scrape_mars.scrape()
    Mars_collection.update_one({},{"$set":Mars_dict}, upsert=True)
    print(Mars_dict)
    #mars_collection.insert_many(Mars_data)

    # Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, Mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)

