from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/sns', methods=['POST'])
def sns():
    message = json.loads(request.data)
    action = message.get('action')
    if action == "open_door":
        # Perform the hardware action here
        print("Opening the door")
    if action == "close_door":
        # Perform the hardware action here
        print("Closing the door")
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)