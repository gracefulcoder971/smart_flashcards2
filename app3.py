from flask import Flask, render_template, request, redirect, url_for
import os
import ingestion, extractor, flashcards, quiz


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["document"]
    if file:
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        clean_text = ingestion.clean_file(filepath)
        concepts = extractor.extract_concepts(clean_text)
        cards = flashcards.generate(concepts)

        return render_template("dashboard.html", cards=cards)
    return redirect(url_for("home"))

@app.route("/quiz")
def quiz_page():
    questions = quiz.generate_quiz()
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
