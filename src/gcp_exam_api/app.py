from flask import Flask, request, abort
import json
app = Flask(__name__)

# List of exams
@app.route("/exams", methods = ["GET"])
def exams_list():
    from google.cloud import datastore

    db = datastore.Client(
        project = "gcp-exam-automation",
        database = "gcp-exam-data"
    )


    query = db.query(kind="questions")

    exams = set()
    for entity in [*query.fetch()]:
        exams.add(entity["exam_id"])

    return list(exams)

# Get exam questions
@app.route("/questions/<exam_id>", methods = ["GET"])
def questions_exam (exam_id):

    from google.cloud import datastore

    db = datastore.Client(
        project = "gcp-exam-automation",
        database = "gcp-exam-data"
    )


    query = db.query(kind="questions")
    query.add_filter(filter=("exam_id", "=", exam_id))

    exam_questions = [*query.fetch()]
    exam_json = {}
    fields = ["question", "a", "b", "c", "d"]
    for question in exam_questions:
        id = question["question_id"]
        exam_json[id] = {
            field: question[field]
            for field in fields
        }

    return json.dumps(exam_json)

# Get exam answers

@app.route("/answers/<exam_id>", methods = ["GET"])
def answers_exam (exam_id):

    from google.cloud import datastore

    db = datastore.Client(
        project = "gcp-exam-automation",
        database = "gcp-exam-data"
    )


    query = db.query(kind="questions")
    query.add_filter(filter=("exam_id", "=", exam_id))

    exam_questions = [*query.fetch()]
    exam_json = {}
    fields = ["answer", "explanation", "source"]
    for question in exam_questions:
        id = question["question_id"]
        exam_json[id] = {
            field: question[field]
            for field in fields
        }

    return json.dumps(exam_json)


if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    app.run()