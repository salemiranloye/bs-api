from flask import Flask, request, jsonify
from gpt import linkget_response, get_response
from validURL import is_valid_url, is_valid_link
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#user_input="In 2016, a story circulated that Pope Francis made an unprecedented and shocking endorsement of Donald Trump for president."
@app.route('/api',methods=["POST"])
def apis():
    user_input = request.get_json()["text"]
    print(user_input)

    if is_valid_link(user_input):
        if is_valid_url(user_input):
            reso = linkget_response(user_input)
           

            # Create a JSON response using jsonify
            response = jsonify({'reso': reso})

            # Return the JSON response
            print(response)
            return response

        else:
            return jsonify({'error': 'The URL is not valid or could not be reached.'}), 400
    else:
        reso = get_response(user_input)
        

            # Create a JSON response using jsonify
        response = jsonify({'reso': reso})
        print(response      )
            # Return the JSON response
        return response

if __name__ == '__main__':
    app.run()
