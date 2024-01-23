class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        newNode.data = data
        self.head.next = newNode

    def printList(self):
        returnList = []

        if self.head:
            currentNode = self.head
            while currentNode:
                returnList.append(currentNode.data)
                currentNode = currentNode.next
        return returnList
        
        
print("hi there")
a = LinkedList()
print(a.printList())