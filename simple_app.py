import streamlit as st
import requests
import sqlite3

# Define the name of the SQLite database
DATABASE_NAME = "user_inputs.db"

def init_db():
    """Initialize the database and create table if not exists."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute(
            '''CREATE TABLE IF NOT EXISTS user_inputs (name TEXT)'''
        )
        conn.commit()

def insert_input_to_db(input_value):
    """Insert the provided input value into the database."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute(
            '''INSERT INTO user_inputs (name) VALUES (?)''', (input_value,)
        )
        conn.commit()

def fetch_data_from_api(input_value):
    # Make a request to the API with user input as a parameter
    response = requests.get(f"https://api.genderize.io?name={input_value}")
    
    # Process the response and extract the data
    if response.status_code == 200:
        data = response.json()
        output = f'''{input_value.capitalize()} is a {str(data['gender']).upper()}\n 
        Confidence: {data['probability']*100} %'''
        return output
    else:
        st.error("Error retrieving data from API")
        return None

def main():
    # Initialize the database and table
    init_db()
    st.title('"Predict Gender by Name"\n')
    st.header("A Simple Python based Web Application built using Streamlit created by Shashank Kashyap")
    st.subheader('Visit the link to know more about me -> https://imshashankashyap.github.io')
    
    # Get user input
    st.subheader("Enter any name to check its Gender")
    user_input = st.text_input()
    
    if user_input:  # Check if user_input is not empty
        # Store the user input in the database
        insert_input_to_db(user_input)
        
        # Fetch data from the API based on user input
        data = fetch_data_from_api(user_input)
        
        if data is not None:
            # Display the retrieved data
            st.write(data)

if __name__ == "__main__":
    main()
