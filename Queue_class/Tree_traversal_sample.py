class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data, end = '')
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.data, end = '')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end = '')
            
    

my_node = Node
my_node.inorder(노드정)보

