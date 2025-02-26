class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
    def print_tree(self, level=0):
        print(' ' * level + "|__" + self.data)
        if self.children:
            level += 1
            for child in self.children:
                child.print_tree(level)
    
def build_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    mobile = TreeNode("Mobile")
    camera = TreeNode("Camera")
    
    laptop.add_child(TreeNode("ASUS"))
    laptop.add_child(TreeNode("ACER"))
    laptop.add_child(TreeNode("Lenovo"))
    
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Apple"))
    mobile.add_child(TreeNode("Mi"))
    
    camera.add_child(TreeNode("Canon"))
    camera.add_child(TreeNode("Nikon"))
    camera.add_child(TreeNode("RED"))
    
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(camera)
    
    root.print_tree()

build_tree()
        