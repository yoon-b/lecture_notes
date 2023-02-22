class TreeNode:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insertNode(self, value):
        if value < self.value:  # self.value: root's value
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insertNode(value)
        
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insertNode(value)
        
    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.value)
        if self.right:
            self.right.inorderTraversal()
    
    def preorderTraversal(self):
        print(self.value)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()
    
    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.value)
    
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
