# Handwritten Digits Recognition Server (hwdr_server.py)
#
# Start with: FLASK_APP=hwdr_server.py flask run
#
# done by sy2002 at 8th of April 2018

import spnn

import numpy as np
import scipy.ndimage as ndi

from flask import Flask, request
from flask_cors import CORS
from nist_csv import *

app = Flask(__name__)
CORS(app)

#recommended: great success/size-ratio and success rate of 97.83% 
#the_network = "saved_nn/784-100-10-0.004-2nd-epoch-66.npz"

#for demo purposes: you need to run XYZ from the root of the project folder
#to make sure this file exists
the_network = "saved_nn/test-epoch-1.npz"

nn = spnn.SimplePerceptronNN(filename=the_network)

@app.route("/")
def hello():
    return """
    Handwritten Digits Recognition Server (hwdr_server.py)<br>
    done by sy2002 at 8th of April 2018<br>
    Use REST API to communicate.
    """

@app.route("/recognize")
def recognize():
    raw_input = eval("[" + request.args.get('imgdata') + "]")

    #the data comes in this form:
    #-1 = no pixel ("white"), +1 = maximum pixel strength ("black")
    #additionally, it needs to be 90 degrees rotated to the right and then mirrored along the y-axis
    adj_input = np.asfarray(raw_input).reshape(28, 28)
    adj_input = np.array(ndi.interpolation.rotate(adj_input, -90, cval=-1.0, reshape=False)).reshape(28, 28)
    adj_input = np.flip(adj_input, axis=1).reshape(784)
    adj_max   = max(adj_input)
    adj_min   = min(adj_input)
    adj_input = ((adj_input + abs(adj_min)) / (max(adj_input) - min(adj_input)) * 0.99) + 0.01

    ascii_art_debug_output(adj_input)

    nn_output = nn.query(adj_input)
    recognized_nr_str = str(nn_output.index(max(nn_output)))
    print("Recognized: ", recognized_nr_str)

    return recognized_nr_str
