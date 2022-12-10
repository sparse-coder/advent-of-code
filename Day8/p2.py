import os

path = os.getcwd() + "\in.txt"

lines = open(path).read().splitlines()
lines = [list(map(int, line)) for line in lines]
scenic_scores = []

for r in range(len(lines)):
    if r==0 or r == len(lines)-1:
        pass
    else:
        for c in range(len(lines[r])):
            if c==0 or c==len(lines[r])-1:
                pass
            else:
                current = lines[r][c]
                le = lines[r][c-1::-1] # look left
                ri = lines[r][c+1:] #look right
                up = [lines[x][c] for x in range(r)] # stores from top to bottom
                down = [lines[x][c] for x in range(r+1, len(lines))]
                
                
                s_up = 0
                #while looking up we need to look from bottom to top
                for item in up[::-1]:
                    s_up+=1
                    if item >= current:
                        break

                s_down = 0
                for item in down:
                    s_down+=1
                    if item >= current:
                        break
                
                s_le = 0
                for item in le:
                    s_le+=1
                    if item >= current:
                        break
                          
                s_ri = 0
                for item in ri:
                    s_ri+=1
                    if item >= current:
                        break


                #print(f"\n{s_up=},{s_down=},{s_le=},{s_ri=}") 
                #scenic_scores.append((s_up*s_down*s_le*s_ri, f"{s_up=},{s_down=},{s_le=},{s_ri=}", (r,c)))    
                scenic_scores.append(s_up*s_down*s_le*s_ri)

print(max(scenic_scores))  
            

