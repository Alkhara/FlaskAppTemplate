# server.py
# A simple Web App for sending payments on the ethereum network

# Required imports
from flask import Flask, request, jsonify, send_file, render_template

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve():
	return render_template("index.html")


if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port=3636)