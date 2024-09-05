
# this is for local machine.  
# from dotenv import load_dotenv 
# load_dotenv() 

# for cloud, set up a secret key GOOGLE_API_KEY

import streamlit as st 
import os 
import sqlite3 

import google.generativeai as genai 

## configure genai key 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load google gemini model and provide queries 

def get_gemini_response(question, prompt): 
    model = genai.GenerativeModel('gemini-pro')
    response =model.generate_content([prompt[0], question])
    return response.text 


## function to retrive query from db 

def read_sql_query(sql, db):
    
    conn =sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute(sql)
    rows=cur.fetchall() 

    for row in rows: print(row)

    return rows 


## defining your prompt 

prompt=[
      """
      You are an expert in converting English questions to SQL query!
      The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
      SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
      the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
      \nExample 2 - Tell me all the students studying in Data Science class?, 
      the SQL command will be something like this SELECT * FROM STUDENT 
      where CLASS="Data Science"; 
      also the sql code should not have ``` in beginning or end and sql word in output

      """


]

## streamlit app 

st.set_page_config(page_title="I can retrive any sql query")
st.header("Gemini App to Retrive SQL data")

question=st.text_input("Input: ", key="input")

submit=st.button("Go ahead. Submit the question")


# if submit is clicked 

if submit: 
    response_sql = get_gemini_response(question, prompt )
    print(response_sql)

    response = read_sql_query(response_sql, "student.db")

    st.subheader("Query results:")


    for row in response: 
        print(row)
        st.header(row)

    



