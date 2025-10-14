import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="wide")


# Initialize the language model
@st.cache_resource
def load_model():
    return ChatOpenAI(model_name="gpt-4o")


# Create the chat prompt template for translation
@st.cache_data
def create_chat_template():
    return ChatPromptTemplate(
        [
            (
                "system",
                "You are a helpful assistant that translates {input_language} to {output_language}.",
            ),
            (
                "human",
                "{text}",
            ),
        ]
    )


def main():
    st.title("🌐 Language Translator")
    st.markdown("Translate text between different languages using AI")

    # Sidebar for language selection
    st.sidebar.header("Translation Settings")

    # Language options
    languages = [
        "English",
        "Spanish",
        "French",
        "German",
        "Italian",
        "Portuguese",
        "Russian",
        "Chinese",
        "Japanese",
        "Korean",
        "Arabic",
        "Hindi",
        "Dutch",
        "Swedish",
        "Norwegian",
        "Danish",
        "Finnish",
        "Polish",
        "Turkish",
        "Greek",
        "Hebrew",
        "Thai",
        "Vietnamese",
        "Indonesian",
    ]

    input_language = st.sidebar.selectbox(
        "Input Language:", languages, index=0  # Default to English
    )

    output_language = st.sidebar.selectbox(
        "Output Language:", languages, index=11  # Default to Hindi
    )

    # Main content area
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"📝 Input Text ({input_language})")
        text_to_translate = st.text_area(
            "Enter text to translate:",
            height=200,
            placeholder="Type your text here...",
            value="Hello, how are you?",
        )

    with col2:
        st.subheader(f"🔄 Translation ({output_language})")
        translation_placeholder = st.empty()

    # Translation button
    if st.button("🚀 Translate", type="primary", use_container_width=True):
        if text_to_translate.strip():
            with st.spinner("Translating..."):
                try:
                    # Load model and template
                    model = load_model()
                    chat_template = create_chat_template()

                    # Create the prompt with user input
                    prompt = chat_template.invoke(
                        {
                            "input_language": input_language,
                            "output_language": output_language,
                            "text": text_to_translate,
                        }
                    )

                    # Get the translation
                    response = model.invoke(prompt)

                    # Display the result
                    with col2:
                        translation_placeholder.text_area(
                            "Translation result:",
                            value=response.content,
                            height=200,
                            disabled=True,
                        )

                    # Show success message
                    st.success("Translation completed successfully!")

                    # Show formatted prompt in expander (for debugging)
                    with st.expander("🔍 View Formatted Prompt"):
                        st.code(str(prompt))

                except Exception as e:
                    st.error(f"Translation failed: {str(e)}")
        else:
            st.warning("Please enter some text to translate.")

    # Footer
    st.markdown("---")
    st.markdown(
        "**Note:** This translator uses OpenAI's GPT-4 model. "
        "Make sure you have set up your OpenAI API key in the environment variables."
    )


if __name__ == "__main__":
    main()
