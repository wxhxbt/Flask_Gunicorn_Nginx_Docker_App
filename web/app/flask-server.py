from flask import Flask, jsonify, request
from flasgger import Swagger
import os
import time

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/process', methods=['POST'])
def delete_space():
	text = request.form.get('text')
	result = text.replace(' ', '')
	return jsonify({"status":"ok", "result":result})

@app.route('/version', methods=['GET'])
def get_metadata():
	return jsonify({"ROUTE":os.environ['_CONDA_ROOT']})

# app.run(debug=True, host='0.0.0.0')
app.run(debug=True, threaded=True)