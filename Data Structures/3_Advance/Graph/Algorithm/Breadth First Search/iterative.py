# Breadth First Search is a searching algorithm which starts searching nodes 
# surrounding the elements; in general term we can say that it explores 
# neighbour nodes
 
from collections import deque

# for directed graph only
def bfs_ (graph : dict, src) -> None :

    q = deque()

    q.append(src)

    while len(q) > 0:

        node = q.popleft()

        print(node)

        for neighbour_node in graph[node]:

            q.append(neighbour_node)

    return

# for both directed and undirectd graph
def bfs (graph : dict, src, visited : set) -> None :

    q = deque()

    q.append(src)

    while len(q) > 0:

        node = q.popleft()

        print(node)

        for neighbour_node in graph[node]:

            if neighbour_node not in visited:

                q.append(neighbour_node)
            
        visited.add(node)

    return


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

    src = "f"  

    #bfs_(graph, src)

    src = 'i'
    visited = set()

    bfs(undirected_graph, src, visited)

