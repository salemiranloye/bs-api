from flask import Flask, request, jsonify
from gpt import linkget_response, get_response
from validURL import is_valid_url, is_valid_link
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def process_input():
    print("hello")
    data = request.get_json()
    print(data)
    user_input = data.get("text", "")

    if is_valid_link(user_input):
        if is_valid_url(user_input):
            response, percent = linkget_response(user_input)
            return jsonify({'response': response, 'percent': percent})
        else:
            return jsonify({'error': 'The URL is not valid or could not be reached.'}), 400
    else:
        response, percent = get_response(user_input)
        return jsonify({'response': response, 'percent': percent})

if __name__ == '__main__':
    app.run()
