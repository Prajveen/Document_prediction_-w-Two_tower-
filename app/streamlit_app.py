# streamlit_app.py

import streamlit as st
from model.Inference import *  # Import FastAPI function

# Streamlit app logic
def main():
    st.title("Two-tower Document prediction")

    # Add Streamlit components
    query = st.text_input("Enter your query:")
    if st.button("Predict"):
        documents = predict_passages(query)
        st.write("Relevant documents:", documents)

if __name__ == "__main__":
    main()
