from infra.functions.generate_question import generate_question_json
from infra.functions.upload_to_database import data_to_database
from infra.services.metadata import Metadata
from infra.services.logger import log
import logging


@log
def create_question(resquest):
    
    logger = logging.getLogger('log_decorator.create_question')
    metadata = Metadata()

    for i in range(12):
        logger.warning(f"Generating question {i+1} ...")

        logger.info("Starting generate question ...")
        question  = generate_question_json(metadata.topics_already_used)
        
        question["question_id"] = i+1
        question["exam_id"] = metadata.exam_id
        logger.info("Question dict file sucessfully generated ...") 

        metadata.add_topic_as_already_used(question["topic"])

        logger.info("Adding question to the questions list ...")
        data_to_database(question)


    return {
        "status_code": 200,
        "message": "Success"
    }

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    questions = create_question(None)
    