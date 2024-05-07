from flask import Flask, request, abort
import json
from infra.functions.filter_dict import filter_dict_items
from infra.services.database import Datastore
from datetime import datetime, timezone

app = Flask(__name__)

# List of exams
@app.route("/exams", methods = ["GET"])
def exams_list():
    
    database = Datastore()
    questions = database.query_data("questions")

    exams = set()
    for entity in questions:
        exams.add(entity["exam_id"])

    return list(exams)

# Get exam questions
@app.route("/exams/questions/<exam_id>", methods = ["GET"])
def questions_exam (exam_id):

    database = Datastore()

    filters = [
        {
            "field": "exam_id",
            "operator": "=",
            "value": exam_id
        }
    ]

    questions = database.query_data("questions", *filters)
    fields = ["question", "a", "b", "c", "d"]
    questions_json = filter_dict_items(questions, fields)

    return questions_json


# Get exam answers

@app.route("/exams/answers/<exam_id>", methods = ["GET"])
def answers_exam (exam_id):

    database = Datastore()

    filters = [
        {
            "field": "exam_id",
            "operator": "=",
            "value": exam_id
        }
    ]

    questions = database.query_data("questions", *filters)
    fields = ["answer", "explanation", "source"]
    questions_json = filter_dict_items(questions, fields)

    return questions_json

@app.route("/user-answers/", methods = ["POST"])
def upload_user_answers():

    data = request.json
    database = Datastore()

    for key, value in data.items():
        with database:

            database.update_data(
                value,
                "questions",
                key
            )

    return "Success!"

if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    app.run()