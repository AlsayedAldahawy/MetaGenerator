from flask import Flask, render_template, request, redirect, url_for
import os
from src.gemini_model import ask_question
from src.scraping import scrape_website
from src.pages_reader import pages_reader
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# ---------------------- Front Routes -----------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/json')
def json_file():
    return render_template('index.html', data_type="json")

@app.route('/csv')
def csv_file():
    return render_template('index.html', data_type="csv")

@app.route('/links')
def multiple_links():
    return render_template('index.html', data_type="links")
#_____________________________________________________________#

# ---------------------- APIs -----------------------
@app.route('/file', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        message = "No file part"
        return render_template('index.html', message=message)
    file = request.files['file']
    if file.filename == '':
        message = "No selected file"
        return render_template('index.html', message=message)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        links_list = json.dumps(pages_reader(file_path))
        return redirect(url_for('results', links=links_list))

@app.route('/multiLinks', methods=['POST'])
def multi_links(): 
    links_list = request.form.get('links') 
    if links_list: 
        print("Received links:", links_list) 
    return redirect(url_for('results', links=links_list))

@app.route('/results', methods=['GET'])
def results():

    links = json.loads(request.args.get('links'))
    answers = []
    
    print("--------------API results links------------------\n", links)

    
    for link in links:
        scraped_data = scrape_website(link)
        answer = ask_question(scraped_data)
        answers.append(answer)
            

    return render_template('index.html', messages=answers, data_type="results")

if __name__ == '__main__':
    app.run(debug=True, port=7777)
