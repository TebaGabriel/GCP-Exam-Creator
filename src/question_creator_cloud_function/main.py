from infra.functions.generate_question import generate_question_json
from infra.functions.storage_json_file import storage_json_file
from infra.services.logger import log
import logging


@log
def create_question(resquest):
    
    logger = logging.getLogger('log_decorator.create_question')

    questions = []
    topics_already_used = []

    for i in range(12):
        logger.warning(f"Generating question {i+1} ...")
        logger.info("Starting generate question JSON file ...")
        question  = generate_question_json(topics_already_used)
        logger.info("Question JSON file sucessfully generated ...") 

        logger.info("Adding topic to the topics list ...")
        topics_already_used.append(question["topic"])

        logger.info("Adding question to the questions list ...")
        questions.append(question)

    logger.info("Starting storage questions JSON ...")
    storage_json_file(questions, local_storage=False)

    return {
        "status_code": 200,
        "message": "Success"
    }

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    questions = create_question(None)
    