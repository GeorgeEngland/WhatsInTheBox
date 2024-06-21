# server.py
from flask import Flask
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_data():
    data = "message": "Hello, World!"
    response = [data]
    response = response.append({"status": "success"})
    # Use flask's jsonify module to convert data to a JSON response
    return jsonify(response)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)  # This server is allowed to use any port from 5000-6000
    except OSError as e:
        print(f"Error: {e}")
        print("Port 5000 might be in use. Please try a different port.")
