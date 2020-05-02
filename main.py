from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging


APP = Flask(__name__)
LOGGER = create_logger(app)
LOGGER.setLevel(logging.DEBUG)


@app.route("/")
def home():
    return "Welcome to Calculator API"

@app.route("/api/v0/multiply")
def multiply():
    param1 = request.args.get(key='param1', default=0, type=int)
    if (param1 == 0):
        return jsonify({"status": "error", "message": "Invalid parameter #1", "value": param1}), 500
    
    param2 = request.args.get(key='param2', default=0, type=int)
    if (param2 == 0):
        return jsonify({"status": "error", "message": "Invalid parameter #2", "value": param1}), 500

    result = int(param1) * int(param2)    
    return jsonify({"status": "success", "result": result}), 200

if __name__ == "__main__":
    LOGGER.info("START Flask")
    APP.debug = True
    APP.run(host='0.0.0.0', port=5001)
    LOGGER.info("SHUTDOWN Flask")
