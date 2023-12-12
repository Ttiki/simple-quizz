from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Database configuration
app.config["MONGO_URI"] = "mongodb://mongo:27017/yourDatabase"
mongo = PyMongo(app)

# Import routes
import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
