import os
import streamlit as st
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app title
st.title(f""":rainbow[Extract Entities with Amazon Comprehend]""")
st.write("Detect built-in entities from the enriched document output.")

# Initialize Comprehend client
comprehend_client = boto3.client('comprehend')

# Function to detect entities using Amazon Comprehend
def detect_entities(text):
    # Call detect_entities function to detect the default, built-in entities from Comprehend
    response = comprehend_client.detect_entities(
        Text=text,
        # Choose the language code
        LanguageCode='en'
    )
    return response['Entities']

# Check if the new enriched outpt file exists
if 'enriched_output.txt' not in os.listdir('.'):
    st.error("File 'enriched_output.txt' not found!")
else:
    # Read the file content
    with open("enriched_output.txt", "r") as file:
        text_content = file.read()
    # Button to invoke the Comprehend analysis
    if st.button("Extract entities", type='primary'):
        with st.spinner('Detecting entities...'):
            entities = detect_entities(text_content)
        # Display detected entities with bold formatting for titles
        if entities:
            st.subheader("Detected Entities:")
            for entity in entities:
                score_percentage = entity['Score'] * 100
                st.write(f"**Entity**: {entity['Text']}, **Type**: {entity['Type']}, **Confidence Score**: {score_percentage:.2f}%")
        else:
            st.write("No entities detected.")
