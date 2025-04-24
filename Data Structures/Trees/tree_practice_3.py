class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
    def print_tree(self):
        print(self.data)
        if self.children:
            
            for i in self.children:
                self.print_tree(i)
        