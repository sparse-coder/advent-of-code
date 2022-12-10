import os

path = os.getcwd() + "\in.txt"

lines = open(path).read().splitlines()
lines = [list(map(int, line)) for line in lines] 
visible = 0

for r in range(len(lines)):
    if r==0 or r == len(lines)-1:
        visible+=len(lines[r])
    else:
        for c in range(len(lines[r])):
            if c==0 or c==len(lines[r])-1:
                visible+=1
            else:
                current = int(lines[r][c])
                le = lines[r][c-1::-1]# look left
                ri = lines[r][c+1:] #look right
                up = [lines[x][c] for x in range(r)]
                down = [lines[x][c] for x in range(r+1, len(lines))]
                
                if all([x<current for x in le]) or \
                    all([x<current for x in ri]) or \
                        all([x<current for x in up]) or\
                            all([x<current for x in down]):
                    visible+=1
                

print(visible)

