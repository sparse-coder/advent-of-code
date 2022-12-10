import os

path = os.getcwd() + "\in.txt"

inst = open(path).read().splitlines()

stops = [20,60, 100,140,180,220]
signal_strengths=[]
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
        cycle+=1
        if cycle in stops:
            signal_strengths.append(X*(cycle))
        temp-=1
    X+=add

print(signal_strengths)
print(sum(signal_strengths))
