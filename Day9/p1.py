import os
from tools import rolling_window

path = os.getcwd() + "\in.txt"

lines = open(path).read().splitlines()


head = [0, 0]
tail = [0, 0]

t_traverses  = {(0, 0)}

move={
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0 ,-1),
    "R": (0, 1)
}

for count, line in enumerate(lines, start=1):
    m, s = line.split(" ")
    s = int(s)
    #print(f"Head: {head} Tail: {tail}")
    #print(f"----{m} {s}----")

    for _ in range(s):
        head[0] += move[m][0]
        head[1] += move[m][1]

        del_x = head[0] - tail[0]
        del_y = head[1] - tail[1] 

        if abs(del_x) > 1 or abs(del_y) > 1:

            if del_x == 0:
                tail[1] += (1* int(del_y/abs(del_y)))
            elif del_y == 0:
                tail[0] += (1* int(del_x/abs(del_x)))
            else:
                tail[0] += (1* int(del_x/abs(del_x)))
                tail[1] += (1* int(del_y/abs(del_y)))
        
        t_traverses.add(tuple(tail))
    


print(len(t_traverses))