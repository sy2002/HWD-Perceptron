Python Server for HWD-Perceptron
==========================================

Files and folders
-----------------

The following table is sorted by importance.

|Name                      |Description
|--------------------------|-------------------------------------------------------
|spnn.py                   |Simple Perceptron Neural Network: This is the main workhorse of the whole project. A Python class called `SimplePerceptronNN`, that implements a freely configurable Perceptron based Neural Network; you can specify the amount of nodes for each layer. Besides the obligatory training and querying features, the class also features saving and loading of networks including metadata.
|hwdr_server.py            |Flask based REST API server: It uses loads a previously trained network, receives requests via REST and outputs the recognized digit.
|hwdt.py                   |Training tool: Uses CSV based training data and runs multiple epochs to train handwritten digits recognition networks. Each epoch is saved as a separate file and metadata is added, so that later, after possibly long running training sessions, the best network version can be selected.
|nist_csv.py               |Helper functions: Load and parse CSV files in our [special format](training#background-information). Additionally an elegant ASCII art printing function is included.
|load_test.py              |Test program that checks loads a neural network and tests, if it performs according to the metadata stored within the file. This tool is a good test for the whole Python and training stack because it actually tests, if everything works as expcted.
|test_cp.py                |Tinkering tool: You can copy/paste the web browser console output of the [client](../client/nn.html) and test, if the recognition works as expected. See also the [tinkering section](../README.md#running-the-classification-manually-as-python-script) in the main README.md.
|training                  |Folder that stores training data. There is a [README.md](training) there worth reading.
|saved_nn                  |Folder that contains networks, that I experimented with. Have a look at the [training results](hwdt.py#L10) to learn more about them and to choose, which one you might want to test. The folder also contains by default all networks that you generate with `hwdt.py`.
|first_perceptron_test.py  |This was the development testbed I used while developing `SimplePerceptronNN (spnn.py)`. It trains a network with 4 input nodes, 2 hidden layers with 3 nodes each and 2 output nodes to output a certain value pair given certain inputs.
|second_perceptron_test.py |After `first_perceptron_test.py` worked, I used this more advanced development testbed to check, if deeper networks are working (I used [4, 8, 5, 4, 2]) and if this "low node count but deep" network could learn a bit more [complex excercise](second_perceptron_test.py#L16). I also used this to get a first idea about learning times and CPU power requirements.
|second_perceptron_test.txt|Results achieved with `second_perceptron_test.py`.
