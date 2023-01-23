import json, random, numpy, array
from collections import defaultdict

# reference: https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/

max_num_rooms = 10
max_num_doors = 2

def generate_map(n_r):
    rooms = ["room_00%02d"%i for i in range(n_r)]
    m = []
    
    for i in range(n_r):
        num_doors = random.randint(1,max_num_doors)
        doors = numpy.random.choice(rooms,num_doors,False)
        
        while "room_00%02d"%i in doors:
            doors = numpy.random.choice(rooms,num_doors,False)
        
        for j in range(num_doors):
            m.append(["room_00%02d"%i,str(doors[j])])
    
    graph = defaultdict(list)
    
    for e in m:
        a, b = e[0],e[1]
        graph[a].append(b)
        graph[b].append(a)
    
    for k in range(n_r):
        ls = []
        for c in graph["room_00%02d"%k]:
            if c not in ls:
                ls.append(c)
            graph["room_00%02d"%k] = ls
    
    return graph

if __name__ == "__main__":
    items = ["item_1","item_2","item_3","item_4","item_5"]
    graph = defaultdict(list)
    num_rooms = random.randint(5,max_num_rooms)
    _map = generate_map(num_rooms)
    #print(_map)
    for i in range(num_rooms):
        info = {"doors":[],"num_of_items":-1,"items":[]}
        print("room_00%02d"%i + " : " + str(_map["room_00%02d"%i]))
        num_items = random.randint(0,5)
        list_items = []
        if num_items > 0:
            list_items = numpy.random.choice(items,num_items,False)
        else:
            list_items = [None]
        info["doors"] = _map["room_00%02d"%i]
        info["num_of_items"] = num_items
        info["items"] = list(list_items)
        graph["room_00%02d"%i] = info
    
    #print(graph)
    json_object = json.dumps(graph, indent = 4)
    #print(json_object)
    
    with open("result.json","w+") as outfile:
        outfile.write(json_object)