import pool
import network
import numpy as np
import math

def getInputs(poolTable):
    inputs = np.zeros(32)
    for i in range(len(poolTable.balls)):
        ball = poolTable.balls[i]
        inputs[2*i] = ball.pos.x
        inputs[2*i+1] = ball.pos.y
    return inputs

MAX_SHOTS = 100
TIME_STEP = 0.01

brains = []
setup = network.NeuralNetworkInputs()
setup.numberOfInputs = 32
setup.numHiddenLayer = 8
setup.numberOfOutputs = 2
for i in range(10):
    brains.append(network.NeuralNetwork(setup))

for i in range(len(brains)):
    print("Training brain:", i)
    poolTable = pool.PoolTable()

    brain = brains[i]
    shots = 0
    while shots < MAX_SHOTS:
        poolTable.update(TIME_STEP)
        if (poolTable.hasFinished()):
            inputs = getInputs(poolTable)
            outputs = brain.evaluate(inputs)
            power = outputs[0] * 2
            angle = outputs[1] * math.pi * 2
            print("Taking shot",shots,"with", power, "power and", angle, "rad")
            poolTable.takeShot(power, angle)
            shots += 1
    
    pocketed = 0
    for ball in poolTable.balls:
        if ball.isPocketed:
            pocketed += 1
    
    print("Brain",i,"scored",pocketed)