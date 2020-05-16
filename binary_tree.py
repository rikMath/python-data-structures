class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class NodeAVL(Node):
    def __init__(self, data):
        super().__init__(data)
        self.height = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            insertNode(data)

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftChild:
                insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return getMin(self.root)

    def getMin(self, node):
        if not node.leftChild:
            return node.data
        else:
            getMin(node.leftChild)

    def getMaxValue(self):
        if self.root:
            return getMax(self.root)

    def getMax(self, node):
        if not node.rightChild:
            return node.data
        else:
            getMax(node.rightChild)

    def traverse(self, order='in'):
        if not self.root:
            if order == 'in':
                traverseInOrder(self.root)
            elif order == 'pre':
                traversePreOrder(self.root)
            else:
                traversePreOrder(self.root)

    def traverseInOrder(self, Node):
        if node.leftChild:
            traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            traverseInOrder(node.rightChild)

    def traversePreOrder(self, Node):
        if node.leftChild:
            traversePreOrder(node.leftChild)
        if node.rightChild:
            traversePreOrder(node.rightChild)
        print(node.data)

    def traversePostOrder(self, Node):
        print(node.data)
        if node.leftChild:
            traversePostOrder(node.leftChild)
        if node.rightChild:
            traversePostOrder(node.rightChild)

    def delete(self, data):
        if self.root:
            deleteNode(data, self.root)

    def deleteNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            deleteNode(data, node.leftChild)

class AVL:

    def __init__(self):
        self.root = None

    def calcHeight(self, node):

        if not node:
            return -1

        return node.height

    def calcBalance(self, node):

        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
