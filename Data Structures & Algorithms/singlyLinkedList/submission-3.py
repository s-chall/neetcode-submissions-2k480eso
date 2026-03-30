class LinkedList:
    
    def __init__(self):
        self.storage = []
    
    def get(self, index: int) -> int:
        if index >= len(self.storage) or index < 0:
            return -1
        else:
            return self.storage[index]

    def insertHead(self, val: int) -> None:
        new_storage = [0] * (len(self.storage)+1)
        new_storage[0] = val
        for i in range(len(self.storage)):
            new_storage[i+1] = self.storage[i]
        self.storage = new_storage

    def insertTail(self, val: int) -> None:
        new_storage = [0] * (len(self.storage)+1)
        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]
        new_storage[len(self.storage)] = val
        self.storage = new_storage

    def remove(self, index: int) -> bool:
        if index >= len(self.storage) or index < 0:
            return False
        else:
            new_storage = [0] * (len(self.storage)-1)
            n = 0
            for i in range(len(self.storage)):
                if i == index:
                    pass
                else:
                    new_storage[n] = self.storage[i]
                    n += 1
            self.storage = new_storage
            return True

    def getValues(self) -> list[int]:
        return self.storage

