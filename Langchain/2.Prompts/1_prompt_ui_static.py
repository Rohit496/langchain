from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

st.title("Langchain Prompt UI")
st.write("This is a simple UI to test Langchain prompts.")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

user_input = st.text_area("Enter your prompt here:", height=200)

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating response..."):
            response = llm.invoke(user_input)  # Call the model with user input
        st.subheader("Response:")
        st.write(response)
        st.write(response.content)  # Display the content of the response
    else:
        st.error("Please enter a prompt.")
