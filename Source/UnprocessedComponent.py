#unused, for referenced

class UnprocessedComponent:
    def __init__ (self, id, fail_rate, unprocessed_dep, left=None, right=None, dep_rel=None, is_dummy=0, parent=None):
        self.id = id
        self.fail_rate = fail_rate
        # relationships: AND, OR, NOISY AND, NOISY OR
        self.unprocessed_dep = unprocessed_dep
        self.left = left
        self.right = right
        self.dep_rel = dep_rel
        self.is_dummy = is_dummy
        self.parent = parent

    

    