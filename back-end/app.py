from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/covid')
def tracker():
    data = dict(
        total=1500,
        active=300,
        recovered=1000,
        deaths=50,
        ncases=150
    )
    return jsonify(data)

