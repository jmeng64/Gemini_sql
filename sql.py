
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
        
    try:
        # Execute the provided SQL query
        cur.execute(sql)
        
        # Fetch all rows from the executed query
        rows = cur.fetchall()
        
        # Print each row
        for row in rows:  print(row)
               
        # Return the fetched rows
        return rows
    
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"An error occurred: {e}")
        return [f"An error occurred: {e}"]
    
    finally:
        # Ensure the connection is closed
        conn.close()




## defining your prompt 

prompt=[
      """
      You are an expert in converting English questions to SQL query!
      The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
      SECTION, GRADE \n\nFor example,\nExample 1 - How many entries of records are present?, 
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

    response = read_sql_query(response_sql, "student2.db")

    st.subheader(response_sql)
    


    for row in response: 
        print(row)
        st.header(row)




