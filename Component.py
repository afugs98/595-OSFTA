class Component:
    tree_type = "Boolean"

    def __init__(self, name, id, fail_rate,  child_rels, children=[]) -> None:
        self.name = name
        self.id = id
        self.fail_rate = fail_rate
        # relationships: AND, OR, NOISY AND, NOISY OR
        self.child_rels = child_rels
        self.children = children
        
    @classmethod
    def set_tree_type(cls, tree_type):
        cls.tree_type = tree_type
    
    @classmethod
    def get_tree_type(cls):
        return cls.tree_type
    
    def add_children(self, node):
        self.children.append(node)
    
    def compute_fail(self):
        pass

    




    
