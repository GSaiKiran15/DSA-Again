class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def print_tree(self, level=0):
        print('  ' * level + "|__" + str(self.data))
        if self.children:
            level += 1
            for child in self.children:
                child.print_tree(level)
    
    def bfs(self, root):
        queue = [root]
        output = [float(root.data)]
        while queue:
            root = queue.pop(0)        
            print(root.data)
            sum = 0
            for i in root.children:
                queue.append(i)
                sum += i.data
            if root.children:
                output.append((sum / len(root.children)))
        print(output)

def build_tree():
    root = TreeNode(1)
    
    laptop = TreeNode(2)
    mobile = TreeNode(3)
    camera = TreeNode(4)
    
    laptop.add_child(TreeNode(5))
    laptop.add_child(TreeNode(6))
    laptop.add_child(TreeNode(7))
    
    mobile.add_child(TreeNode(8))
    mobile.add_child(TreeNode(9))
    mobile.add_child(TreeNode(10))
    
    camera.add_child(TreeNode(11))
    camera.add_child(TreeNode(12))
    camera.add_child(TreeNode(13))
    
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(camera)
    
    root.print_tree()
    root.bfs(root)
    
    

build_tree()