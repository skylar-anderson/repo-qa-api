from flask import Flask, request
from flask_cors import CORS
from bot import get_answer

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    question = request.args.get('question')
    if question:
      return get_answer(question)
    else:
      return "please provide a question!"