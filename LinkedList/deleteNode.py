class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

class Solution:
    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next

node1 = Node(4)
node2 = Node(5)
node3 = Node(1)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Before deletion:")
traverseAndPrint(node1)
node = 5
expected = [4, 1, 9]

Solution().deleteNode(node2)
print("After deletion:")
traverseAndPrint(node1)
