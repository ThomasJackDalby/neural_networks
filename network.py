import numpy as np

def sigmoid(x, derivative=False):
  return x*(1-x) if derivative else 1/(1+np.exp(-x))

class NeuralNetworkInputs:

    def __init__(self):
        self.numberOfInputs = 1
        self.numHiddenLayer = 1
        self.numberOfOutputs = 1

class NeuralNetwork:

    def __init__(self, setup, dna=None):
        self.setup = setup

        if dna is not None:
            self.weights1 = dna[0:self.setup.numberOfInputs*self.setup.numHiddenLayer].reshape(self.setup.numberOfInputs,self.setup.numHiddenLayer)
            self.weights2 = dna[self.setup.numberOfInputs*self.setup.numHiddenLayer:len(dna)].reshape(self.setup.numHiddenLayer,self.setup.numberOfOutputs)
        else:
            self.weights1 = np.random.rand(self.setup.numberOfInputs,self.setup.numHiddenLayer)
            self.weights2 = np.random.rand(self.setup.numHiddenLayer,self.setup.numberOfOutputs)

    def evaluate(self, inputs):
        self.layer1 = sigmoid(np.dot(inputs, self.weights1))
        return sigmoid(np.dot(self.layer1, self.weights2))

    def getDNA(self):
        w1 = self.weights1.flatten()
        w2 = self.weights2.flatten()
        return np.concatenate((w1, w2))

    def breed(self, other):
        dna1 = self.getDNA()
        dna2 = other.getDNA()
        i = np.random.randint(1,dna1.shape[0]-1)
        l = dna1.shape[0]
        child1 = NeuralNetwork(self.setup, np.concatenate((dna1[0:i],dna2[i:l])))
        child2 = NeuralNetwork(self.setup, np.concatenate((dna2[0:i],dna1[i:l])))
        return [child1, child2]