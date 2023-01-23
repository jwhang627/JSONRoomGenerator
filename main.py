import json, random, os, numpy

max_num_rooms = 10
max_num_doors = 4


def generate_json_map(n_r):
    #print(n_r)
    rooms = [str(i + 1) for i in range(n_r)]
    items = ["item_1","item_2","item_3","item_4","item_5"]
    str_map = "{"
    for i in range(n_r):
        str_map += ("\"" + str(i+1) + "\"" + ":" + "{")
        str_map += "\"num_of_doors\":"
        num_doors = random.randint(1,max_num_doors)
        str_map += (str(num_doors) + ",")
        str_map += "\"doors\":"
        
        portals = numpy.random.choice(rooms,num_doors,False)
        
        if str(i + 1) in portals:
            while str(i + 1) in portals:
                portals = numpy.random.choice(rooms,num_doors,False)
            
        str_map += (str(portals) + ",")
        
        #door = [str(j + 1) for j in range(num_doors)]
        
        str_map += ","
        
        num_items = random.randint(0,5)
        
        str_map += ("\"num_of_items\":" + str(num_items) + "," + "\"items\":")
        
        if num_items > 0:
            str_map += (str(numpy.random.choice(items,num_items)) + "},")
        else:
            str_map += "[null]},"
    
    str_map += "}"
    return str_map


#def __init__():
    #print("what's going on?")
    #main()

def main():
    #print("is this working?")
    num_rooms = random.randint(5,max_num_rooms)
    #num_doors = random.randint(1,max_num_doors)
    str_map = generate_json_map(num_rooms)
    print(str_map)

main()
