import re
from Component import UnprocessedComponent, DummyComponent, RootComponent
from FaultTree import FaultTree

class AnalyzeEngine:

    def __init__(self):
        self.operators = ["AND", "OR", "or", "and"]
        self.root = None

    def convert_to_component(self, dic):
        # defines the relations
        for id in dic:
            parent = dic[id]
            dep = parent.unprocessed_dep

            # no dependencies
            if dep is None: continue

            if id == 'main':
                parent = RootComponent(parent.id, -1)
                self.root = parent
          

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
                   
                    # comp1 = cstack.pop()
                    # comp2 = cstack.pop()
                    # operator = ostack.pop()
                    # dummyid = "D"
                    # dummy = UnprocessedComponent(dummyid, -1, None, comp1, comp2, operator, 1)
                    # cstack.append(dummy)
                elif part in self.operators:
                    ostack.append(part)
                elif part in dic:
                    # dic[part].parent = parent
                    cstack.append(dic[part])
                    comp_lim -= 1
                    if comp_lim <= 0:
                        comp1 = cstack.pop()
                        comp2 = cstack.pop()
                        operator = ostack.pop()
                        print(operator)
                        dummy = DummyComponent("D", -1, left=comp1, right=comp2, dep_rel=operator)
                        cstack.append(dummy)
                        comp_lim = 1
                else: 
                    return -1
            
            #should be one component in cstack
            comp = cstack.pop()

            #if the final component is a dummy, set current to the dummy values
            if type(comp) is DummyComponent:
                parent.left = comp.left
                parent.right = comp.right
            else:
                parent.left = comp

            dic[id] = parent
        
        return dic

    def create_tree(self, dic):
        subs = []  
        for id in dic:
            if not dic[id].parent:
                subs.append(dic[id])
        
        root = FaultTree(subs)
        
        return root