from flask import Flask, render_template, request
import os
from src.gemini_model import chat_answer
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
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
        message = f"File '{file.filename}' uploaded successfully."
        messages = chat_answer(f"./uploads/{file.filename}")
    return render_template('index.html', messages=messages)
        
if __name__ == '__main__':
    app.run(debug=True, port=7777)
