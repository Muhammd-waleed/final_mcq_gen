import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from src.mcqgenerator.utils import pdf_text


key=os.getenv("google_api_key")
def mcq_gen_fun(text,quantity,level,subject):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=key)

    structure = '''
    1 : multiple choice question.
    a: choice here
    b: choice here
    c: choice here
    d: choice here

    correct: correct answer

    2 : multiple choice question.
    a: choice here
    b: choice here
    c: choice here
    d: choice here

    correct: correct answer
    3 : multiple choice question
    a: choice here
    b: choice here
    c: choice here
    d: choice here

    correct: correct answer


    '''

    prompt_template = PromptTemplate.from_template(
    '''You are an expert MCQ maker. Text For the quiz is Here {input_text}. it is your job to create {quantity} Conceptual and real use case multiple choice questions from the  {subject} Domains students and Your Question Difficuuilty Level sould be  {level}.

    - Here are some instruction You Must folow Otherwise You will Be Penelaized
    No intro needed, just jump straight into the MCQs
    Mcqs Should be in the Given Format and here is this format {input_format} .
    USe different type of MCqs asking Technique to generate the Mcqs
    Generate the Mcqs for test the ability of the Students About the {subject}
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Ensure to make {quantity} MCQs 
    You have to Give Only the  Only Mcqs and not give any type of information  About the {subject} and only  tell the correct answer  Number in the end of Each MCQ'''
    )


    prompt=prompt_template.format(input_text=text,quantity=quantity,subject=subject,level=level,input_format=structure)

    response=llm.invoke(prompt)

    response=response.replace("*","")

    return response

result=mcq_gen_fun(text=pdf_text(r"E:/final_mcq_gen/linear_algebra_chap_01_mit.pdf"),
            quantity=5,
            level="Easy",
            subject='Advance Programming',
            )

print(result)