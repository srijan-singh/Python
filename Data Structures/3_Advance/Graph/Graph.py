class Graph(dict):

    def __init__ (self):
        self = dict()

    def add(self, given_node: str, neighbour: str) -> None:
        if self.has_node(given_node):
            self[given_node].append(neighbour)
        else:
            self[given_node] = [neighbour]

    def has_node(self, given_node:str) -> bool:
        for key in self:
            if key == given_node:
                return True
        return False        
    
    def show(self):
        print(self)


graph = Graph()

graph.add('a','b')
graph.show()
graph.add('a','c')
graph.show()
graph.add('b', 'd')
graph.show()

print(graph.has_node('b'))
