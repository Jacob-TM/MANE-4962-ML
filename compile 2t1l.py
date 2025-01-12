from random import random

l = open('lies.txt','r')
t = open('truths.txt','r')

lies = []
truths = []

for x in l:
    lies.append(x.strip().capitalize())
    
for x in t:
    truths.append(x.strip().capitalize())

a=len(truths)
b=len(lies)

while len(truths) >= 2 and len(lies) >= 1:
    x = round(random()*(len(truths)-1))
    print(f'1. {truths[x]}')
    truths.pop(x)
    x = round(random()*(len(truths)-1))
    print(f'2. {truths[x]}')
    truths.pop(x)
    z = round(random()*(len(lies)-1))
    print(f'3. {lies[x]}')
    lies.pop(x)
    print()