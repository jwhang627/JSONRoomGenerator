import json, random, os, numpy, re, ast

max_num_rooms = 10
max_num_doors = 4


def generate_json_map(n_r):
    #print(n_r)
    rooms = ["{}".format(i + 1) for i in range(n_r)]
    
    items = ["item_1","item_2","item_3","item_4","item_5"]
    str_map = "{"
    for i in range(n_r):
        str_map += ("{}".format(i+1) + ":" + "{")
        str_map += "\"num_of_doors\":"
        num_doors = random.randint(1,max_num_doors)
        str_map += (str(num_doors) + ",")
        str_map += "\"doors\":"
        
        portals = numpy.random.choice(rooms,num_doors,False)
        
        if "{}".format(i + 1) in portals:
            while "{}".format(i + 1) in portals:
                portals = numpy.random.choice(rooms,num_doors,False)
            
        str_map += (re.sub("\s+",",",str(portals).strip()) + ",")
        
        #door = [str(j + 1) for j in range(num_doors)]
        
        #str_map += ","
        
        num_items = random.randint(0,5)
        
        str_map += ("\"num_of_items\":" + str(num_items) + "," + "\"items\":")
        
        if num_items > 0:
            str_map += (re.sub("\s+",",",str(numpy.random.choice(items,num_items)).strip()) + "},")
        else:
            str_map += "[null]},"
    
    str_map = str_map[:len(str_map)-1]

    str_map += "}"
    return str_map

def main():
    #print("is this working?")
    num_rooms = random.randint(5,max_num_rooms)
    #num_doors = random.randint(1,max_num_doors)
    str_map = generate_json_map(num_rooms)

    str_map = str_map.replace("\'","\"")
    
    #p = re.compile('(?<!\\\\)\'')
    #str_map = p.sub('\"',str_map)

    print(str_map)

    #json_object = json.loads(str_map)

    json_file = ast.literal_eval(json.dumps(str_map,skipkeys = True, allow_nan = True,indent = 4))

    with open("result.json","w+") as outfile:
        outfile.write(json_file)
        #json.dump(json_object, outfile)

main()
