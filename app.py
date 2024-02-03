# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/beautify', methods=['POST'])
def beautify():
    try:
        txt = request.form['json_input'] 
        tab_space = int(request.form['tab_space'])
        to_json = json.loads(txt)
        beautified_result = json.dumps(to_json, indent=tab_space)
        return jsonify({'result': beautified_result, 'error': None})
    except json.JSONDecodeError as e:
        return jsonify({'result': None, 'error': f"Error: {e}"})

if __name__ == '__main__':
    app.run(debug=True)