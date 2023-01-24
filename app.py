from flask import Flask, request
from flask_cors import CORS
from langchain_bot_simple import get_answer

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    question = request.args.get('question')
    print('question:')
    print(question)
    if question:
      return get_answer(question)
    else:
      return "please provide a question!"

# app.run()