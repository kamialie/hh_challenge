#open the file and calculate measurement of the map and values for shape calculation
f = open('input_2.txt').readlines()
map_list = []
total = 0
vacancy_count = 0
for line in f:
    line = line.rstrip()
    total += len(line)
    vacancy_count += line.count('o')
    map_list.append(line)
width_map = len(f)
length_map = total//width_map

#create possible shapes
s = total//vacancy_count
p = 0
possibilities = []
for j in range(1, s+1):
    if s %j == 0:
        p += 1
        if s//j <= length_map and j <= width_map:
            possibilities.append((s//j, j))

#prepare list for saving shapes
keys = ['startx', 'starty', 'answer','shape']
values = [0, 0, '', 0,0,0]
list_of_shapes = []
for o in range(vacancy_count+1):
    list_of_shapes.append(dict(zip(keys,values)))

#reserve map
reserve_map = [[ '' for i in range(length_map)] for j in range(width_map)]

#reserve_map checking function
def check(sy, sx, width, length):
    s = ''
    for y in range(sy, sy+width):
        for x in range(sx, sx+length):
            s += reserve_map[y][x]
    if s.count('8') != 0:
        return False
    else:
        return True

#actual calculation
startx = 0
starty = 0
answer = ''
i = 0
if total%vacancy_count ==0:
    while i < vacancy_count:
        #get initial values to create a shape
        startx = list_of_shapes[i]['startx']
        starty = list_of_shapes[i]['starty']
        startpos = list_of_shapes[i]['shape']
        for n in range(startpos, len(possibilities)):
            length = possibilities[n][0]
            width = possibilities[n][1]
            #check if shape fits the map and create it
            if startx+length <= length_map and starty+width <= width_map:
                #reserve_map checking
                rcheck = check(starty, startx, width, length)
                if rcheck:
                    for y in range(starty,starty+width):
                        answer += map_list[y][startx : startx+length] + '\n'
                        #if shape goes through all requirements, save it and update inital values and reserve_map
                    if answer.count('o') == 1:
                        list_of_shapes[i]['answer'] = answer
                        answer = ''
                        list_of_shapes[i]['shape'] = n
                        for y in range(starty, starty+width):
                            for x in range(startx, startx+length):
                                reserve_map[y][x] = "8"
                        for line in reserve_map:
                            if '' in line:
                                xxx = line.index('')
                                yyy = reserve_map.index(line)
                                list_of_shapes[i+1]['startx'] = xxx
                                list_of_shapes[i+1]['starty'] = yyy
                                break
                        i += 1
                        break
                    #check the next shape
                    else:
                        answer = ''
                        continue
                #check the next shape
                else:
                    answer = ''
                    continue
            #check the next shape
            else:
                continue
        #go back to previous form to try another shape if its not the first form    
        else:
            if i == 0:
                break
            else:
                list_of_shapes[i]['shape'] = 0
                #update reserve_map
                i = i - 1
                for y in range(list_of_shapes[i]['starty'], list_of_shapes[i]['starty'] + possibilities[list_of_shapes[i]['shape']][1]):
                    for x in range(list_of_shapes[i]['startx'], list_of_shapes[i]['startx'] + possibilities[list_of_shapes[i]['shape']][0]):
                        reserve_map[y][x] = ''
                list_of_shapes[i]['shape'] += 1
                
#print results
if i == vacancy_count:
    for item in list_of_shapes:
        print(item['answer'])

