from flask import Flask, request, render_template_string

from templates import HTML_TEMPLATE
from qa_model import answer_question

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Render only the form initially
    return render_template_string(HTML_TEMPLATE)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    if question:
        new_question, similar_questions, similar_answers, answer_content = answer_question(question)
        return render_template_string(HTML_TEMPLATE, question=new_question, similar_questions=similar_questions, similar_answers=similar_answers, answer_content=answer_content)
    else:
        return render_template_string(HTML_TEMPLATE, question="")