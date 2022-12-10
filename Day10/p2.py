import os

path = os.getcwd() + "\in.txt"

inst = open(path).read().splitlines()

CRT = [[" " for c in range(40)] for r in range(6)]
print(CRT)
cur_crt_row_n = 0

X=1
cycle=0

m = {
    "noop":1,
    "addx":2
}

for item in inst:
    z = item.split(" ")
    ins = z[0]
    add = 0 if len(z)==1 else int(z[1])
    temp = m[ins]
    while temp:
        if cycle%40 in [X-1, X, X+1]:
            CRT[cur_crt_row_n][cycle%40] = "#"
        cycle+=1
        if cycle%40==0:
            cur_crt_row_n+=1
        temp-=1
    X+=add

print(CRT)
for r in CRT:
    for c in r:
        print(c, end="")
    print()