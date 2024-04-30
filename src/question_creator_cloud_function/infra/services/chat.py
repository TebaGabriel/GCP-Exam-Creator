from openai import OpenAI
import logging
import os

class ChatGPT():

    def __init__(self):

        self.logger = logging.getLogger('log_decorator.chat_gpt')

        self.client = OpenAI(
            api_key = os.getenv("OPENAI_API_KEY")
        )

        self.messages = []

        self.json_output_keys = ["topic", "question", "a", "b", "c", "d", "answer", "explanation", "source"]

    def create_message (self, role, system_message):

        self.logger.info(f"Adding message for {role} role into messages list...")
        message = {
            "role": role,
            "content": system_message
        }
        
        self.messages.append(message)
        self.logger.info(f"Message was created and added into messages list!")

    def chat_completions(self):

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=self.messages
        )

        self.logger.info("Chat completion successfully requested!")

        return response
    
    def validate_GCP_question(self, question):

        if any(
            [
                key not in self.json_output_keys 
                for key in question.keys()
            ]
        ):

            self.logger.error("There are more keys than expected in question JSON!!!")

            return False


        if not all(
            [
                key in self.json_output_keys 
                for key in question.keys()
            ]
        ):

            self.logger.error("It is missing some keys in question JSON!!!")

            return False
        
        self.logger.info("Question has only the essencials keys!")
        return True


        
