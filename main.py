def island(graph : dict, visited: set) -> int:
    count : int = 0
    queue : list = []

    for node in graph:
        source : str = node
        if source not in visited:
            count+=1
            queue.append(node)
        #visited.add(node)
        while len(queue)>0:
            current = queue.remove(0)      
            for neighbour in current:
                visited.add(neighbour)
    return count



graph = {
    'a' : ['b'],
    'b' : ['a'],
    'c' : ['d'],
    'd' : ['c','e','f','g'],
    'e' : ['d'],
    'f' : ['d'],
    'g' : ['d'],
    'h' : ['i'],
    'i' : ['h'],
    'j' : ['l'],
    'l' : ['j'],
    'x' : ['y'],
    'y' : ['x']
}

source = 'a'

Set = set()

print(island(graph, set))

#depth_first_search(graph, source)