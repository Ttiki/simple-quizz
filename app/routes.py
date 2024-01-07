from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app
from flask_pymongo import PyMongo
import json



main_routes = Blueprint('main', __name__)
mongo = PyMongo(app)

@main_routes.route('/quiz/<string:seed>')
def index(seed):
    quiz_collection = mongo.db.quizzes
    quiz_data = quiz_collection.find_one({"seed": seed})
    if quiz_data:
        questions = quiz_data.get("questions", [])
    else:
        questions = []

    questions_json = json.dumps(questions)
    return render_template('index.html', questions_json=questions_json)



@main_routes.route('/')
def index():
    # Logic to fetch questions here
    questions = ...
    return render_template('index.html', questions=questions)

@main_routes.route('/results', methods=['POST'])
def results():
    # Logic to calculate results based on user input
    answers = request.form
    score = ...
    return render_template('results.html', score=score)
