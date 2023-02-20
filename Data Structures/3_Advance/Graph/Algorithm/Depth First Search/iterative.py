# Depth First Search is a searching algorithm which explores,
# all nodes unidirectioally until no nodes left
# It uses stack as a fundamental data structure

# directed graph
def dfs_(graph:dict, src) -> None :

    stack = []

    stack.append(src)

    while len(stack) > 0:

        node = stack.pop()

        print(node)

        for neighbour_node in graph[node]:
            stack.append(neighbour_node)

    return

# for both directed and undirected graph
def dfs (graph:dict, src, visited:set) -> None :

    stack = []

    stack.append(src)

    while len(stack) > 0:

        node = stack.pop()

        print(node)

        for neighbour_node in graph[node]:

            if neighbour_node not in visited:

                stack.append(neighbour_node)

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

    #dfs_(graph, src)

    src = 'i'
    visited = set()

    dfs(undirected_graph, src, visited)
