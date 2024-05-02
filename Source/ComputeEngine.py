from Source.Component import UnprocessedComponent, DummyComponent, RootComponent
from Source.FaultTree import FaultTree

class ComputeEngine:
    def __init__(self, root, type="Boolean"):
        self.root = root
        self.type = type

    def and_gate(self, prob1, prob2):
        probability = prob1 * prob2
        return probability

    def or_gate(self, prob1, prob2):
        probability = (1 - prob1) * (1 - prob2)
        return 1 - probability

    def calculate_gate(self, gate_type, prob1, prob2):
        # if leakage is not None:
            # result = self.noisy_or_gate(leakage, *args)
        if self.type == "Boolean":
            if gate_type == "AND":
                result = self.and_gate(float(prob1), float(prob2))
            else:
                result = self.or_gate(float(prob1), float(prob2))       
           
        return result
    
    def evaluate(self, root):
        if not root.left and not root.right:
            return
        else:
            if root.left:
                self.evaluate(root.left)
            if root.right:
                self.evaluate(root.right)

        # Now, calculate and set the current node's probability based on its children
        if root.right and root.left:
            probability = self.calculate_gate(root.get_dep_rel(), root.left.get_probability(), root.right.get_probability())
        elif root.right:
            probability = root.right.get_probability()
        elif root.left:
            probability = root.left.get_probability()

        root.set_probability(probability)



