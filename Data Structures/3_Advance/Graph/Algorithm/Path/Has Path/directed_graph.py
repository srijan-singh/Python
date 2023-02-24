# Has Path is implementation of DFS and BFS and it can be optimized for cyclic graphs
# by keeping track of visited nodes 

from collections import deque

def hasPathDFS(graph:dict, src, dst, visited = None) -> bool:

    if visited == None:
        visited = set()

    if(src == dst):
        return True

    visited.add(src)

    for neighbour_node in graph[src]:
        
        if neighbour_node not in visited:
            if (hasPathDFS(graph, neighbour_node, dst, visited)):
                return True
    
    return False

def hasPathBFS(graph:dict, src, dst) -> bool :

    q = deque()
    q.append(src)

    visited = set()

    while len(q) > 0:

        node = q.popleft()

        if node == dst:
            return True

        visited.add(node)

        for neighbour_node in graph[node]:
            if neighbour_node not in visited:
                q.append(neighbour_node)
            
    return False


if __name__ == "__main__":

    graph = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : [],
        'i' : ['g', 'k'],
        'j' : ['i'],
        'k' : []
    }

    undirected_graph = {
        'i' : ['j', 'k'],
        'j' : ['i'],
        'k' : ['i', 'm', 'l'],
        'm' : ['k'],
        'l' : ['k'],
        'o' : ['n'],
        'n' : ['o']
    } 

    src = 'i'
    dst = 'l'

    print(hasPathDFS(undirected_graph, src, dst))
    print(hasPathBFS(undirected_graph, src, dst))

