from datetime import datetime, timezone
import logging

class Metadata():

    def __init__(self):

        self.logger = logging.getLogger('log_decorator.metadata')

        self.exam_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")

        self.topics_already_used = []

    def add_topic_as_already_used (self, topic):

        self.logger.info("Adding topic to the topics list ...")
        self.topics_already_used.append(topic)