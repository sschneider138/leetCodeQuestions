import heapq

class test:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

        self.heap1 = []
        self.heap2 = []
        self.returnedArr = []

        for num in self.arr1:
            heapq.heappush(self.heap1, num)
        for num in self.arr2:
            heapq.heappush(self.heap2, num)

    def mergeTwoArray(self):
        while self.heap1 and self.heap2:
            if self.heap1[0] < self.heap2[0]:
                self.returnedArr.append(heapq.heappop(self.heap1))
            else:
                self.returnedArr.append(heapq.heappop(self.heap2))
        if self.heap1 and not self.heap2:
            while self.heap1:
                self.returnedArr.append(heapq.heappop(self.heap1))
        if self.heap2 and not self.heap1:
            while self.heap2:
                self.returnedArr.append(heapq.heappop(self.heap2))
        return self.returnedArr

list1 = [1,2,4, 1]
list2 = [1,3,4]
a = test(list1, list2)
print(a.mergeTwoArray())

        