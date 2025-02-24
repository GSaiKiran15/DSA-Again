class TreeNode:
    def __init__(self,value):
        self.parent = None
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def print_tree(self, level=0):
        print('  ' * level + '|-->' + self.value)
        if self.children:
            level += 1
            for child in self.children:
                child.print_tree(level)

def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.print_tree()
    return root

build_tree()


    