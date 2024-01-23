# leet code 1514. Path with Maximum Probability

import collections
import heapq

class Solution:
    def maxProb(self, n, edges, succProb, start, end) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            source, destination = edges[i]
            adj[source].append([destination, succProb[i]])
            adj[destination].append([source, succProb[i]])

        priorityQ = [(-1, start)]
        visited = set()

        while priorityQ:
            prob, currentNode = heapq.heappop(priorityQ)
            visited.add(currentNode)

            if currentNode == end:
                return prob * -1
            for neighbor, edgeProb in adj[currentNode]:
                if neighbor not in visited:
                    heapq.heappush(priorityQ, (prob * edgeProb, neighbor))
