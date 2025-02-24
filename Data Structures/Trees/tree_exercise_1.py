class TreeNode:
    def __init__(self,name, role):
        self.parent = None
        self.name = name
        self.role = role
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def print_tree(self, level=0, detail=None):
        if detail == "name":
            print('  ' * level + '|-->' + self.name)
        elif detail == "role":
            print('  ' * level + '|-->' + self.role)
        elif detail == "both":
            print('  ' * level + '|-->' + self.name + "(" + self.role + ")")
        else:
            print("Please provide the detail you want name, role or both")
        if self.children:
            level += 1
            for child in self.children:
                child.print_tree(level, detail)

def build_tree():
    root = TreeNode("Nipul", "CEO")

    laptop = TreeNode("Chinmay", "CTO")
    vishwa = TreeNode("Vishwa", "Infrastructure head")
    laptop.add_child(vishwa)
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))
    laptop.add_child(TreeNode("Aamir", "Application Head"))

    cellphone = TreeNode("Gels", "HR Head")
    cellphone.add_child(TreeNode("Peter", "Recruitment Manager"))
    cellphone.add_child(TreeNode("Waqas", "Policy Manager"))


    root.add_child(laptop)
    root.add_child(cellphone)
    root.print_tree(detail="both")
    return root

build_tree()


    