import transformers
import streamlit as st
import pandas as pd

def display(csv_file):
    df = pd.read_csv(csv_file)
    st.write("Top 10 Contents of the CSV File:")
    st.write(df.head(10))

def app():
    st.set_page_config(page_title="FinO", page_icon=":moneybag:", layout="wide")
    st.header("FinO 🗺")

    csv = st.file_uploader('Upload a CSV file', type='csv')
    if csv is not None:
        
        st.write("File uploaded successfully")
        display(csv)
    
    user_question = st.text_input("Enter a headline")

    if user_question:
        st.write("You entered: ", user_question)


    

if __name__ == "__main__": 
    app()

