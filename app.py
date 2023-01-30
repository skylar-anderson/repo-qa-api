from flask import Flask, request, render_template
from flask_cors import CORS
from bot import get_answer

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html', title='Primer Bot')

@app.route('/ask', methods=['GET'])
def ask():
    question = request.args.get('question')
    if question:
      return get_answer(question)
    else:
      return "please provide a question!"