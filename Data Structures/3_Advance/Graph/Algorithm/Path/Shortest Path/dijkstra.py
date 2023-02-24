from collections import deque

def dijkstra(graph : dict, start, end) -> list :

    path = []

    visited = set()

    q = deque()

    q.append(start)

    while len(q) > 0:

        node = q.popleft()

        if(node == end):
            return path

        visited.add(node)
    
        path.append([node, graph[node]])

        node_path = graph[node]

        sorted_path = sorted(node_path.items(), key=lambda x:x[1])

        for elm in sorted_path:

            neighbour_node = elm[0]

            if neighbour_node not in visited:
                q.append(neighbour_node)
        
    return path


if __name__ == "__main__":

    graph = {
        's' : {'a' : 7, 'b' : 2, 'c' : 3},
        'a' : {'s' : 7, 'b' : 3, 'd' : 4},
        'b' : {'s' : 2, 'a' : 3, 'e' : 1},
        'c' : {},
        'd' : {'a' : 4, 'b' : 4},
        'e' : {'b' : 1}
    }

    start = 's'
    end = 'e'

    print(dijkstra(graph, start, end))