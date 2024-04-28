import os
import streamlit as st

from src.mcqgenerator.mcq_generator import mcq_gen_fun
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from src.mcqgenerator.utils import pdf_text

key=os.getenv("google_api_key")
st.header("MCQS GENERATORS")
st.caption(" Mcqs Will Diplay Below After Generating:")
file_address=st.sidebar.file_uploader("PDF File Upload ")
quantity=st.sidebar.number_input("No. of MCQs",min_value=5,max_value=20)
subject=st.sidebar.text_input("Subject",max_chars=75)
level=st.sidebar.selectbox("Difficulity Level",options=['None','Basic','Moderate','Advance'])
submit=st.sidebar.button("Generate MCQs")


if submit is not False:
    if file_address is not None:
        if quantity is not None:
                if subject !='':
                                if level != 'None':
                                    result=mcq_gen_fun(text=pdf_text(file_address.name),
                                    quantity=quantity,
                                    level=level,
                                    subject=subject,
                                    )
                                    with st.container(border= True):
                                        st.text(result)
                                else:
                                    st.error("Select Level")
                else:
                    st.error("Enter Subject")

        else:
            st.error("Mention No of MCQs")
        
    else:
        st.error("Upload File")


