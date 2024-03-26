from Source.Component import Component
from Source.FaultTree import FaultTree

if __name__ == "__main__":
    subsystem1 = Component("subsystem 1", "02", "25%", ["AND", "OR"])
    subsystem2 = Component("subsystem 2", "03", "25%", ["AND", "OR"])
    system = Component("system", "01", "50%", ["AND", "OR"], [subsystem1, subsystem2])

    tree = FaultTree(system)
    tree.print_tree()
