class GrumpyBookstoreOwner:
    def __init__(self, customers, grumpy, minutes) -> None:
        self.customers = customers
        self.grumpy = grumpy
        self.minutes = minutes

    def maxSatisfied(self):
        potentialGain = []
        diffArr = []

        for i in range(0, len(self.customers)-1):
            if self.grumpy[i] == 0:
                potentialGain.append(self.customers[i])
            else:
                potentialGain.append(0)
            # diffArr.append()
        

        print(potentialGain)
        print(diffArr)




customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
a = GrumpyBookstoreOwner(customers, grumpy, minutes)
a.maxSatisfied()