from flask import Flask, request, jsonify, render_template
from gpt import get_response
app = Flask(__name__)
prompt = "President Obama shocked the country when he announced he would be running for a third term."
@app.route('/')
def index():
    return get_response(prompt)

@app.route('/hello')
def hello():
    
    return 'Hello, World'

if __name__ == '__main__':
    app.run()