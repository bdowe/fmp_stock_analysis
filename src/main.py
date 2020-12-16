from flask import Flask, request, jsonify
from stats import *

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'msg': 'Hello, World!'})

@app.route('/get-stats/<ticker>', methods=['GET'])
def stats(ticker):
    df = get_stats(ticker)
    return df.to_json(orient='records')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
