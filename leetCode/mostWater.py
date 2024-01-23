class MostWater:

    def __init__(self, heights):
        self.heights = heights
        self.maxVolume = 0

    def maxArea(self):
        table = [
            [0 for i in range(len(self.heights))] for j in range(len(self.heights))
        ]

        i = 0
        j = len(self.heights) - 1
        while i < j:
            if self.heights[i] < self.heights[j]:
                vol = self.heights[i] * (j - i)
                table[i][j] = vol
                if vol > self.maxVolume:
                    self.maxVolume = vol
                i += 1
            else:
                vol = self.heights[j] * (j - i)
                table[i][j] = vol
                if vol > self.maxVolume:
                    self.maxVolume = vol
                j -= 1

        print(table)
        print(self.maxVolume)



a = MostWater([1,8,6,2,5,4,8,3,7])
a.maxArea()