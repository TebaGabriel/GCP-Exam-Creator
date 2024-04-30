from infra.services.chat import ChatGPT
from chat_gpt_params import SYSTEM_PROMPT, TEMPLATE_USER_MESSAGE
import json
import logging
import time
from datetime import datetime, timezone

def generate_question_json(topics = None):
    
    logger = logging.getLogger('log_decorator.generate_question_json')
    question_validated = False

    while question_validated is False:

        complete_prompt = ", with a topic that it is not in this list: [" + ", ".join(topics) + "]" if topics else ""
        logger.info("Initializing ChatGPT class ...")
        client = ChatGPT()

        logger.info("Creating chatGPT messages ...")
        client.create_message("system", SYSTEM_PROMPT)
        client.create_message("user", TEMPLATE_USER_MESSAGE.format(topics_already_used = complete_prompt))

        logger.info("Requesting chat completion to Chat GPT API ...")
        response = client.chat_completions()

        try:

            logger.info("Extracting question from Chat GPT response ...")
            question = json.loads(response.choices[0].message.content)

        except:
            logger.warning("Question could not parse to JSON!!!")
            continue
        
        logger.info("Validating question keys ...")
        question_validated = client.validate_GCP_question(question)
        time.sleep(5)

    question["created_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
    
    return question