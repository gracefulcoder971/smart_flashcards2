from flask import Flask, render_template, request, redirect, url_for
import os
import ingestion, extractor, flashcards, quiz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['document']
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        clean_text = ingestion.clean_file(filepath)
        concepts = extractor.extract_concepts(clean_text)
        flashcards_data = flashcards.generate_flashcards(concepts)
        quiz_data = quiz.generate_quiz(concepts)

        return render_template('dashboard.html',
                               flashcards=flashcards_data,
                               quiz=quiz_data)
    return redirect(url_for('home'))

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
