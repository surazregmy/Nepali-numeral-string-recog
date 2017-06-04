from __future__ import division
import numpy
import scipy.special
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/traindata/')
UPLOAD_FOLDER2 = join(dirname(realpath(__file__)),'templates/images/')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages/')

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # number of input nodes
        self.input_nodes = inputnodes
        # number of hidden nodes
        self.hidden_nodes = hiddennodes
        # number of output nodes
        self.output_nodes = outputnodes
        # learning rate
        self.lr = learningrate


        self.weight_input_hidden = numpy.genfromtxt(UPLOAD_FOLDER+'input_to_hidden.csv',delimiter=',')

        self.weight_hidden_output = numpy.genfromtxt(UPLOAD_FOLDER+'hidden_to_output.csv',delimiter=',')

        # sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

    def predict(self, inputs_list):
        # convert input list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # inputs to hidden layer
        hidden_inputs = numpy.dot(self.weight_input_hidden, inputs)

        # outputs from the hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # inputs to output layer
        final_inputs = numpy.dot(self.weight_hidden_output, hidden_outputs)

        # outputs from the output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

def recognize_single(rec_csv):

    input_nodes = 1024
    hidden_nodes = 300
    output_nodes = 10
    learning_rate = 0.3

    neural = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    print("Single data")
    test_data = open(UPLOAD_FOLDERC+rec_csv, 'r')
    test_list = test_data.readlines()
    test_data.close()


    for record in test_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[0:]) / 255 * 0.99) + 0.01
        outputs = neural.predict(inputs)
        label = numpy.argmax(outputs)
    print(label)
    return  label






