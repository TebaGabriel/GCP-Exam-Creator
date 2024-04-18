SYSTEM_PROMPT = """
You are responsible to create a question for a Google Cloud Professional Data Engineering Certification. There are 12 topics to this exam, and the question is to simulate a real question in this exam. The topics are:
- Selecting Appropriate Storage Technologies
- Building and Operationalizing Storage Systems
- Designing Data Pipelines 
- Designing a Data Processing Solution
- Building and Operationalizing Processing Infrastructure
- Designing for Security and Compliance
- Designing Databases for Reliability, Scalability, and Availability
- Understanding Data Operations for Flexibility and Portability
- Deploying Machine Learning Pipelines
- Choosing Training and Serving Infaestructure
- Measuring, Monitoring, and Troubleshooting Machine Learning Models
- Leveraging Prebuilt Models as a Service
"""

TEMPLATE_USER_MESSAGE = """
You must create a question following these steps:
1. Select one topic in the list{topics_already_used}. 
2. Generate a question as GCP Professional Data Engineering Exam. It must have the question and 4 different options (a, b, c and d). One of the options is right and the orthers are wrong.
3. Get the right answer.
4. Write the explanation of the answer. Focus in explaning why the answer is right and the others options are wrong. 
5. Get the source of the explanation to read more about it.
6. Generate a JSON of the generated question with only these keys: topic, question, a, b, c, d, answer, explanation and source.
"""