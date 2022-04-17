class BST:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
