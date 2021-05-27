import math
import numpy as np

class Node:
    id = None
    up = None
    down = None
    left = None
    right = None
    previousNode = None

    def __init__(self, value):
        self.value = value

# region ID3
class item:
    def __init__(self, age, prescription, astigmatic, tearRate, diabetic, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.diabetic = diabetic
        self.needLense = needLense

    def getDataset():
        data = []
        labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
        data.append(item(0, 0, 0, 0, 1, labels[0]))
        data.append(item(0, 0, 0, 1, 1, labels[1]))
        data.append(item(0, 0, 1, 0, 1, labels[2]))
        data.append(item(0, 0, 1, 1, 1, labels[3]))
        data.append(item(0, 1, 0, 0, 1, labels[4]))
        data.append(item(0, 1, 0, 1, 1, labels[5]))
        data.append(item(0, 1, 1, 0, 1, labels[6]))
        data.append(item(0, 1, 1, 1, 1, labels[7]))
        data.append(item(1, 0, 0, 0, 1, labels[8]))
        data.append(item(1, 0, 0, 1, 1, labels[9]))
        data.append(item(1, 0, 1, 0, 1, labels[10]))
        data.append(item(1, 0, 1, 1, 0, labels[11]))
        data.append(item(1, 1, 0, 0, 0, labels[12]))
        data.append(item(1, 1, 0, 1, 0, labels[13]))
        data.append(item(1, 1, 1, 0, 0, labels[14]))
        data.append(item(1, 1, 1, 1, 0, labels[15]))
        data.append(item(1, 0, 0, 0, 0, labels[16]))
        data.append(item(1, 0, 0, 1, 0, labels[17]))
        data.append(item(1, 0, 1, 0, 0, labels[18]))
        data.append(item(1, 0, 1, 1, 0, labels[19]))
        data.append(item(1, 1, 0, 0, 0, labels[20]))
        return data


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1


class ID3:
    dataset = item.getDataset()

    def __init__(self, features):
        self.features = features
        self.buildtree('Root')

    def entropy(self, list):
        numberOFZeros = 0
        numberOFOnes = 0
        for i in range(0, len(list)):
            if list[i] == 0:
                numberOFZeros += 1
            elif list[i] == 1:
                numberOFOnes += 1
        length = numberOFOnes + numberOFZeros
        if length == 0:
            return 0
        elif numberOFZeros == 0 and numberOFOnes == 0:
            return 0
        elif numberOFZeros == 0 and numberOFOnes != 0:
            return -((numberOFOnes / length) * math.log2(numberOFOnes / length))
        elif numberOFZeros != 0 and numberOFOnes == 0:
            return -((numberOFZeros / length) * math.log2(numberOFZeros / length))
        else:
            return -(((numberOFZeros / length) * math.log2(numberOFZeros / length)) + (
                        (numberOFOnes / length) * math.log2(numberOFOnes / length)))

    def Get_Max_Gain(self):
        Max_Gain = -99999
        age = []
        prescription = []
        astigmatic = []
        tearRate = []
        diabetic = []
        needLenses = []
        maxColumn = 0
        for i in range(0, len(self.dataset)):
            age.append(self.dataset[i].age)
            prescription.append(self.dataset[i].prescription)
            astigmatic.append(self.dataset[i].astigmatic)
            tearRate.append(self.dataset[i].tearRate)
            diabetic.append(self.dataset[i].diabetic)
            needLenses.append(self.dataset[i].needLense)
        listOFColumns = [age, prescription, astigmatic, tearRate, diabetic, needLenses]
        for i in range(0, 5):
            if self.features[i].visited == -1:
                numberOfZeros = 0
                numberOfOnes = 0
                listOFOutputZeros = []
                listOFOutputOnes = []
                length = len(listOFColumns[i])
                for j in range(0, length):
                    if listOFColumns[i][j] == 0:
                        numberOfZeros += 1
                        listOFOutputZeros.append(listOFColumns[5][j])
                    elif listOFColumns[i][j] == 1:
                        numberOfOnes += 1
                        listOFOutputOnes.append(listOFColumns[5][j])
                gain = self.entropy(listOFColumns[5]) - (((numberOfZeros / length) * self.entropy(listOFOutputZeros)) +
                                                         ((numberOfOnes / length) * self.entropy(listOFOutputOnes)))
                if gain > Max_Gain:
                    Max_Gain = gain
                    maxColumn = i
        self.features[maxColumn].visited = 1
        return maxColumn

    startNode = None
    currentNode = None

    def buildtree(self, postion):

        maxGainColumn = self.Get_Max_Gain()
        node = Node(maxGainColumn)
        node.id = maxGainColumn
        if postion == 'Root':
            self.startNode = node
        elif postion == 'Left':
            self.currentNode.left = node
        elif postion == 'Right':
            self.currentNode.right = node

        self.currentNode = node
        datasetZeros = []
        datasetOnes = []
        tmpResultZeros = []
        tmpResultones = []

        if maxGainColumn == 0:
            for i in range(0, len(self.dataset)):
                if self.dataset[i].age == 0:
                    datasetZeros.append(self.dataset[i])
                    tmpResultZeros.append(self.dataset[i].needLense)
                elif self.dataset[i].age == 1:
                    datasetOnes.append(self.dataset[i])
                    tmpResultones.append(self.dataset[i].needLense)
        elif maxGainColumn == 1:
            for i in range(0, len(self.dataset)):
                if self.dataset[i].prescription == 0:
                    datasetZeros.append(self.dataset[i])
                    tmpResultZeros.append(self.dataset[i].needLense)
                elif self.dataset[i].prescription == 1:
                    datasetOnes.append(self.dataset[i])
                    tmpResultones.append(self.dataset[i].needLense)
        elif maxGainColumn == 2:
            for i in range(0, len(self.dataset)):
                if self.dataset[i].astigmatic == 0:
                    datasetZeros.append(self.dataset[i])
                    tmpResultZeros.append(self.dataset[i].needLense)
                elif self.dataset[i].astigmatic == 1:
                    datasetOnes.append(self.dataset[i])
                    tmpResultones.append(self.dataset[i].needLense)
        elif maxGainColumn == 3:
            for i in range(0, len(self.dataset)):
                if self.dataset[i].tearRate == 0:
                    datasetZeros.append(self.dataset[i])
                    tmpResultZeros.append(self.dataset[i].needLense)
                elif self.dataset[i].tearRate == 1:
                    datasetOnes.append(self.dataset[i])
                    tmpResultones.append(self.dataset[i].needLense)
        elif maxGainColumn == 4:
            for i in range(0, len(self.dataset)):
                if self.dataset[i].diabetic == 0:
                    datasetZeros.append(self.dataset[i])
                    tmpResultZeros.append(self.dataset[i].needLense)
                elif self.dataset[i].diabetic == 1:
                    datasetOnes.append(self.dataset[i])
                    tmpResultones.append(self.dataset[i].needLense)

        self.dataset.clear()

        tmpResult = np.unique(tmpResultZeros)
        if len(tmpResult) > 1:
            self.dataset = datasetZeros.copy()
            self.buildtree('Left')
        else:
            self.currentNode.left = tmpResult[0]

        tmpResult = np.unique(tmpResultones)
        if len(tmpResult) > 1:
            for i in range(0, len(datasetOnes)):
                self.dataset = datasetOnes.copy()
            self.buildtree('Right')
        else:
            self.currentNode.right = tmpResult[0]

    def classify(self, input):
        node = self.startNode
        while True:
            if node.id == 0:
                if input[0] == 1:
                    if node.right == 0 or node.right == 1:
                        return node.right
                    else:
                        node = node.right
                elif input[0] == 0:
                    if node.left == 0 or node.left == 1:
                        return node.left
                    else:
                        node = node.left
            elif node.id == 1:
                if input[1] == 1:
                    if node.right == 0 or node.right == 1:
                        return node.right
                    else:
                        node = node.right
                elif input[1] == 0:
                    if node.left == 0 or node.left == 1:
                        return node.left
                    else:
                        node = node.left
            elif node.id == 2:
                if input[2] == 1:
                    if node.right == 0 or node.right == 1:
                        return node.right
                    else:
                        node = node.right
                elif input[2] == 0:
                    if node.left == 0 or node.left == 1:
                        return node.left
                    else:
                        node = node.left
            elif node.id == 3:
                if input[3] == 1:
                    if node.right == 0 or node.right == 1:
                        return node.right
                    else:
                        node = node.right
                elif input[3] == 0:
                    if node.left == 0 or node.left == 1:
                        return node.left
                    else:
                        node = node.left
            elif node.id == 4:
                if input[4] == 1:
                    if node.right == 0 or node.right == 1:
                        return node.right
                    else:
                        node = node.right
                elif input[4] == 0:
                    if node.left == 0 or node.left == 1:
                        return node.left
                    else:
                        node = node.left


# endregion
# region ID3_Main_Fn
def ID3_Main():
    dataset = item.getDataset()
    features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate'),
                Feature('diabetic')]
    id3 = ID3(features)
    cls = id3.classify([0, 0, 1, 1, 1])
    print('testcase 1: ', cls)
    cls = id3.classify([1, 1, 0, 0, 0])
    print('testcase 2: ', cls)
    cls = id3.classify([1, 1, 1, 0, 0])
    print('testcase 3: ', cls)
    cls = id3.classify([1, 1, 0, 1, 0])
    print('testcase 4: ', cls)


# endregion
######################## MAIN ###########################33
if __name__ == '__main__':
    ID3_Main()