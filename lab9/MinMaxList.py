class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=False / True):
        if not self.listData:
            self.listData.append(item)
        elif item >= max(self.listData):
            self.listData.append(item)
        else:
            for i in range(len(self.listData)):
                if item >= self.listData[i]:
                    pass
                else:
                    print(f"Item {item} inserted at location {i}")
                    self.listData.insert(i, item)
                    break
        if printResult:
            self.printList()

    def getMin(self):
        listMin = min(self.listData)
        self.listData.remove(listMin)
        return listMin

    def getMax(self):
        listMax = max(self.listData)
        self.listData.remove(listMax)
        return listMax

    def printList(self):
        print(self.listData)
