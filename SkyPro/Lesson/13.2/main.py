class Employee:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


node1 = Employee({'id' : 1})
node2 = Employee({'id' : 2})
node1.next_node = node2
print(node1.next_node)