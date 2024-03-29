import socketClient
import NeuralNetwork
import numpy as np

## Receives data from 2 sensors and does NN training and logging on the data in real time.

#Input parameters
packetSize = 1
numSensors = 2
numClasses = 16


#Paths
basePath = "data/Orientation01/"

class0 = "baseStationaryC00"   #Class 0 is the reference orientation with no movement

class1 = "baseCW90X_01C001"         #sensor 1 reference orientation 90 CW on X axis; sensor 2 stationay     Sensor points straight up
class2 = "baseCW90X_02C02"         #sensor 2 reference orientation 90 CW on X axis; sensor 1 stationay     Sensor points straight up
class3 = "baseCW90X_01baseCW90X_02C03"         #sensor 1 & 2 reference orientation 90 CW on X axis         Sensor points straight up

class4 = "baseCCW90X_01C04"         #sensor 1 reference orientation 90 CCW on X axis; sensor 2 stationay   Sensor points straight down
class5 = "baseCCW90X_02C05"         #sensor 2 reference orientation 90 CCW on X axis; sensor 1 stationay   Sensor points straight down
class6 = "baseCCW90X_01baseCCW90X_02C06"         #sensor 1 & 2 reference orientation 90 CCW on X axis       Sensor points straight down

class7 = "baseCW90Y_01C07"         #sensor 1 reference orientation 90 CW on Y axis; sensor 2 stationay     Sensor rotates to right (looking from ESP32)
class8 = "baseCW90Y_02C08"         #sensor 2 reference orientation 90 CW on Y axis; sensor 1 stationay     Sensor rotates to right (looking from ESP32)
class9 = "baseCW90Y_01baseCW90Y_02C09"         #sensor 1 & 2 reference orientation 90 CW on Y axis         Sensor rotates to right (looking from ESP32)

class10 = "baseCCW90Y_01C10"         #sensor 1 reference orientation 90 CCW on Y axis; sensor 2 stationay  Sensor rotates to left (looking from ESP32)
class11 = "baseCCW90Y_02C11"         #sensor 2 reference orientation 90 CCW on Y axis; sensor 1 stationay  Sensor rotates to left (looking from ESP32)
class12 = "baseCCW90Y_01baseCCW90Y_02C12"         #sensor 1 & 2 reference orientation 90 CCW on Y axis      Sensor rotates to left (looking from ESP32)

class13 = "baseCCW45Y_01C13"         #sensor 1 reference orientation 90 CCW on Y axis; sensor 2 stationay  Sensor rotates to left (looking from ESP32)
class14 = "baseCCW45Y_02C14"         #sensor 2 reference orientation 90 CCW on Y axis; sensor 1 stationay  Sensor rotates to left (looking from ESP32)
class15 = "baseCCW45Y_01baseCCW45Y_02C15"         #sensor 1 & 2 reference orientation 90 CCW on Y axis      Sensor rotates to left (looking from ESP32)

pathList = [basePath + class0, basePath + class1, basePath + class2, basePath + class3, basePath + class4, basePath + class5, basePath + class6, basePath + class7, basePath + class8, basePath + class9, basePath + class10, basePath + class11, basePath + class12, basePath + class13, basePath + class14, basePath + class15]

#pathList = [basePath + class0]

def main():


  # Get Data for training
  # #No movement
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class0, packetLimit=30, label=0, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class0 + "_test", packetLimit=3, label=0, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class1, packetLimit=30, label=1, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class1 + "_test", packetLimit=3, label=1, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class2, packetLimit=30, label=2, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class2 + "_test", packetLimit=3, label=2, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class3, packetLimit=30, label=3, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class3 + "_test", packetLimit=3, label=3, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class4, packetLimit=30, label=4, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class4 + "_test", packetLimit=3, label=4, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class5, packetLimit=30, label=5, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class5 + "_test", packetLimit=3, label=5, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class6, packetLimit=30, label=6, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class6 + "_test", packetLimit=3, label=6, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class7, packetLimit=30, label=7, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class7 + "_test", packetLimit=3, label=7, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class8, packetLimit=30, label=8, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class8 + "_test", packetLimit=3, label=8, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class9, packetLimit=30, label=9, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class9 + "_test", packetLimit=3, label=9, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class10, packetLimit=30, label=10, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class10 + "_test", packetLimit=3, label=10, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class11, packetLimit=30, label=11, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class11 + "_test", packetLimit=3, label=11, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class12, packetLimit=30, label=12, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class12 + "_test", packetLimit=3, label=12, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class13, packetLimit=30, label=13, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class13 + "_test", packetLimit=3, label=13, packetSize=packetSize, numSensors = numSensors)

  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class14, packetLimit=30, label=14, packetSize=packetSize, numSensors = numSensors)
  # socketClient.createTrainingData(pathPreface=basePath, labelPath=class14 + "_test", packetLimit=3, label=14, packetSize=packetSize, numSensors = numSensors)

  socketClient.createTrainingData(pathPreface=basePath, labelPath=class15, packetLimit=30, label=15, packetSize=packetSize, numSensors = numSensors)
  socketClient.createTrainingData(pathPreface=basePath, labelPath=class15 + "_test", packetLimit=3, label=15, packetSize=packetSize, numSensors = numSensors)

  # for i in range(len(pathList)):
  #   #dataArr = np.load(pathList[i] + ".npy", allow_pickle=False)
  #   #print(f'data in file {pathList[i]} shape: {dataArr.shape}')
  #   #print(f'data at basePath: {dataArr}')

  #   truthArr = np.load(pathList[i] + "_truth.npy",allow_pickle=False)
  #   print(f'truth data in {pathList[i]} shape: {truthArr.shape}')
  #   print(f'truth data at basePath: {truthArr}')

  print()
  print()
  print(f'data acquired begin training')

  dataArr = np.load(pathList[0] + ".npy", allow_pickle=False)
  print(f'data in file {pathList[0]} shape: {dataArr.shape}')
  #print(f'data at basePath: {dataArr}')

  tmpArr = np.loadtxt(pathList[0] + ".csv",dtype=float, delimiter=',', ndmin=2)
  print(f'data from csv ({pathList[0] + ".csv"}) shape: {tmpArr.shape}')
  print(f'data from csv: {tmpArr}')

  #np.save(pathList[12] + ".npy", tmpArr, allow_pickle=False)

  #Train network with test data
  NeuralNetwork.trainOrientation(basePath, pathList, packetSize, numSensors, numClasses)

if __name__ == "__main__": main()