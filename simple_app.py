import streamlit as st
import requests

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
    st.title("A simple Web Application with API Integration using Streamlit")
    st.write("Welcome to this FREE API-powered web application created by Shashank Kashyap")
    st.write('Visit to know more about me: https://imshashankashyap.github.io')
    
    # Get user input
    user_input = st.text_input("Enter any name to check its Gender")
    
    if user_input:  # Check if user_input is not empty
        # Fetch data from the API based on user input
        data = fetch_data_from_api(user_input)
        
        if data is not None:
            # Display the retrieved data
            st.write(data)

if __name__ == "__main__":
    main()
