FROM python:3

MAINTAINER sy2002 "https://github.com/sy2002"

RUN mkdir -p /opt/HWD-Perceptron
RUN git clone https://github.com/sy2002/HWD-Perceptron.git /opt/HWD-Perceptron
WORKDIR /opt/HWD-Perceptron

# install python library
RUN pip install -r requirements.txt
WORKDIR /opt/HWD-Perceptron/server/training
RUN ./install_data.sh

# training the network
WORKDIR /opt/HWD-Perceptron/server
RUN rm -f saved_nn/test-epoch-1.npz
RUN python hwdt.py

# run process
WORKDIR /opt/HWD-Perceptron/server
CMD FLASK_APP=hwdr_server.py flask run --host=0.0.0.0
