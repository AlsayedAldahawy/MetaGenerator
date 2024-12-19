from src.scraping import scrape_website
from src.pages_reader import pages_reader
from src.answer_save import save_metadescription
import google.generativeai as genai
from dotenv import load_dotenv 
import os 


load_dotenv() 


# Load environment variables from .env file 

API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to interact with the Hugging Face API and ask a question
def ask_question(question):

    response = model.generate_content(question)

    # Check if the request was successful
    if response:
        return response.text
    else:
        return f"Error:"


def chat_answer(file_path):
    pages_list = pages_reader(file_path)
    answers_list = []
    i = 0
    for page in pages_list:
        i += 1
        scraped_data = scrape_website(page)
        question = f"provide meta description of this page based on its scraped data, make your answer ready to be used as meta description: {scraped_data}"
        answer = ask_question(question)
        answers_list.append(f'{i}: {answer}')
        

    return answers_list
