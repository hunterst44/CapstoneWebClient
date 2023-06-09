import socketClient
import NeuralNetwork
import numpy as np

## Receives data from 2 sensors and does NN training and logging on the data in real time.
## WARNING this will start with fresh (random) weights and biases and OVERWRITE current model at pathPreface/model

def main():

  # Get Data for training
    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/noMove", packetLimit=30, label=0, packetSize=5, numSensors=2)
    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/noMove_Test", packetLimit=3, label=0, packetSize=5, numSensors=2)

    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/upandDown", packetLimit=30, label=1, packetSize=5, numSensors=2)
    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/upandDown_Test", packetLimit=3, label=1, packetSize=5, numSensors=2)

    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/inandOut", packetLimit=30, label=2, packetSize=5, numSensors=2)
    socketClient.createTrainingData(pathPreface="data/trainGestures3Classes/inandOut_Test", packetLimit=3, label=2, packetSize=5, numSensors=2)

    #Train network on all data
    NeuralNetwork.train3Gestures("data/trainGestures3Classes/")

if __name__ == "__main__": main()