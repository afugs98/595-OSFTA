import re
from Source.Component import UnprocessedComponent, DummyComponent, RootComponent


class AnalyzeEngine:

    def __init__(self):
        self.operators = ["AND", "OR", "or", "and"]
        self.root = None

    def createUnprocessedTree(self, dic):
        # defines the relations
        for id in dic:
            parent = dic[id]
            dep = parent.unprocessed_dep

            # no dependencies
            if dep is None: continue

            if id == 'main':
                parent = RootComponent(parent.id, -1)
                self.setRoot(parent)

            parts = re.findall(r'\w+|\S', dep)
            pstack = []
            cstack = []
            ostack = []
            comp_lim = 2
            for part in parts:
                if part == "(":
                    pstack.append("(")
                    comp_lim = 2
                elif part == ")":
                    if pstack:
                        if pstack.pop() != "(":
                            return -1 # mismatched parantheses error
                elif part in self.operators:
                    ostack.append(part)
                elif part in dic:
                    cstack.append(dic[part])
                    comp_lim -= 1
                    if comp_lim == 0:
                        comp1 = cstack.pop()
                        comp2 = cstack.pop()
                        operator = ostack.pop()
                        dummy = DummyComponent(id="D", fail_rate=-1, left=comp1, right=comp2, dep_rel=operator)
                        cstack.append(dummy)
                        comp_lim = 1
                else: 
                    return None
            
            while len(cstack) > 1:
                comp1 = cstack.pop()
                comp2 = cstack.pop()
                operator = ostack.pop()
                dummy = DummyComponent(id="D", fail_rate=-1, left=comp1, right=comp2, dep_rel=operator)
                cstack.append(dummy)
            
            #should be one component in cstack
            comp = cstack.pop()

            #if the final component is a dummy, set current to the dummy values
            if type(comp) is DummyComponent:
                parent.left = comp.left
                parent.right = comp.right
                parent.set_dep_rel(comp.get_dep_rel())
            else:
                parent.left = comp

            dic[id] = parent
        
        return self.getRoot()

    
    def getRoot(self):
        return self.root
    
    def setRoot(self, root):
        self.root = root
        return
