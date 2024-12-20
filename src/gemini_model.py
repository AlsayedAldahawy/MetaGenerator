from src.scraping import scrape_website
from src.pages_reader import pages_reader
from src.answer_save import save_metadescription
import google.generativeai as genai
from dotenv import load_dotenv 
import os 


# Load environment variables from .env file 
load_dotenv() 
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to interact with the Hugging Face API and ask a question
def ask_question(scraped_data):

    question = f"provide meta description of this page based on its scraped data, make your answer ready to be used as meta description: {scraped_data}"

    response = model.generate_content(question)

    # Check if the request was successful
    if response:
        return response.text
    else:
        return "Error getting response"

