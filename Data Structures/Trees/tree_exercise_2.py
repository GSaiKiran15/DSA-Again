class TreeNode:
    def __init__(self,value):
        self.parent = None
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def print_tree(self, level=0, l=None):
        print('  ' * level + '|__' + self.value)
        if self.children:
            level += 1
            if l == level:
                return
            for child in self.children:
                child.print_tree(level, l)

def build_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")
    
    india.add_child(gujarat)
    india.add_child(karnataka)
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka.add_child(TreeNode("Bangalore"))
    karnataka.add_child(TreeNode("Mysore"))
    

    usa = TreeNode("USA")
    nj = TreeNode("New Jersey")
    ca = TreeNode("California")
    usa.add_child(nj)
    usa.add_child(ca)
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))
    ca.add_child(TreeNode("San Francisco"))
    ca.add_child(TreeNode("Mountain View"))
    ca.add_child(TreeNode("Palo Alto"))

    root.add_child(india)
    root.add_child(usa)
    root.print_tree(l=0)
    return root

build_tree()


    