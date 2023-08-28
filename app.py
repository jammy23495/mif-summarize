# app.py

from flask import Flask, request, json
from flask_cors import CORS
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
app = Flask(__name__)
CORS(app)


# For handling post request form we can get the form
# inputs value by using POST attribute.
# this values after submitting you will never see in the urls.
@app.route('/mif', methods=['POST'])
def handle_post():
	data = json.loads(request.data)
	text = data["text"]
	return summarizer(text, max_length=1000, min_length=30, do_sample=False)

if __name__ == '__main__':
	app.run()
