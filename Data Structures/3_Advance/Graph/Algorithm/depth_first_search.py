def depth_first_search(graph : dict, source : str) -> None:
    stack = [source]

    while(len(stack) > 0):
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)


graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

source = 'a'

depth_first_search(graph, source)