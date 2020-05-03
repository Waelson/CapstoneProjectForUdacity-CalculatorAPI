""" Single page """
import socket
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger


APP = Flask(__name__)
LOGGER = create_logger(APP)
LOGGER.setLevel(logging.DEBUG)

@APP.route("/")
def1 home():
    """ Return the home page / Green=#006400 / Blue=#1E90FF """
    return "<html><body style='background-color:#1E90FF; color: white;'><h3>Welcome to Calculator API</h3><br/><h1>HOST: {}</h1></body></html>".format(socket.gethostname())

@APP.route("/api/v0/multiply")
def multiply():
    """ Return multiplication of param1 and param2 """    
    param1 = request.args.get(key='param1', default=0, type=int)
    if param1 == 0:
        return jsonify({'status': 'error', 'message': 'Invalid parameter 1', 'value': param1}), 500
    param2 = request.args.get(key='param2', default=0, type=int)
    if param2 == 0:
        return jsonify({'status': 'error', 'message': 'Invalid parameter 2', 'value': param2}), 500
    result = int(param1)*int(param2)    
    return jsonify({'status': 'success', 'result': result}), 200

if __name__ == "__main__":
    LOGGER.info("START Flask")
    APP.debug = True
    APP.run(host='0.0.0.0', port=5001)
    LOGGER.info("SHUTDOWN Flask")
