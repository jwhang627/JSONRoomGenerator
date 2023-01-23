import json, random, os, numpy, re, ast, array

max_num_rooms = 10
max_num_doors = 3


# room_0000, room_0001, etc.

def generate_json_map(n_r):
    #print(n_r)
    #rooms = ["{0}".format(str(i + 1).zfill(2)) for i in range(n_r)]
    rooms = ["room_00%02d"%i for i in range(n_r)]
    
    #rooms = list(rooms)
    #rooms_string = json.dumps(rooms)
    #print(json.dumps(str(rooms).replace("\'","\"")))
    #print(rooms)
    #rooms = json.dumps(rooms)
    items = ["item_1","item_2","item_3","item_4","item_5"]
    str_map = "{"
    for i in range(n_r):
        #str_map += (str("{0}".format(str(i+1).zfill(2))) + ":" + "{")
        str_map += ("\"" + rooms[i] + "\"" + ":" + "{")
        str_map += "\"num_of_doors\":"
        num_doors = random.randint(1,max_num_doors)
        str_map += (str(num_doors) + ",")
        str_map += "\"doors\":"
        
        portals = numpy.random.choice(rooms,num_doors,False)
        
        '''
        if str("{0}".format(str(i + 1).zfill(2))) in portals:
            while str("{0}".format(str(i + 1).zfill(2))) in portals:
                portals = numpy.random.choice(rooms,num_doors,False)
        '''
        if ("room_00%02d"%i) in portals:
            while ("room_00%02d"%i) in portals:
                portals = numpy.random.choice(rooms,num_doors) 
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
    #print(str_map)
    return str_map

def main():
    #print("is this working?")
    num_rooms = random.randint(5,max_num_rooms)
    #num_doors = random.randint(1,max_num_doors)
    str_map = generate_json_map(num_rooms)
    #print(str_map)
    str_map = str_map.replace("\'","\"")
    
    #p = re.compile('(?<!\\\\)\'')
    #str_map = p.sub('\"',str_map)

    print(str_map)

    #json_object = json.loads(str_map)

    json_file = ast.literal_eval(json.dumps(str_map,indent = 4,sort_keys=False))
    #json_file = json.dumps(str_map,indent = 4,sort_keys=False)
    #j = json.loads(json_file)
    #j = json.dumps(str(j),indent = 4,sort_keys=False)
    #print(str(j))
    with open("result.json","w+") as outfile:
        #outfile.write(str(j))
        outfile.write(json_file)
        #json.dump(json_object, outfile)
    #with open("result.json","r+") as infile:
    #	j = json.load(infile)
        
main()
