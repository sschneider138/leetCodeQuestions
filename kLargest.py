import heapq

class Solution:
    def __init__(self, inputArr, k) -> None:
        self.inputArr = inputArr
        self.k = k

    def kLargest(self):
        maxHeap = []
        for i in range(len(self.inputArr)):
            heapq.heappush(maxHeap, self.inputArr[i])

        while len(maxHeap) > self.k:
            heapq.heappop(maxHeap)
        return maxHeap[0]
    
    def arrMethod(self):
        self.inputArr.sort()
        return self.inputArr[-self.k]

myArr = [3,2,3,1,2,4,5,5,6]
a = Solution(myArr, 4)
print(a.kLargest())
print(a.arrMethod())
