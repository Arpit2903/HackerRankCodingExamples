from itertools import product

inp1 = list(map(int,input().split(' ')))
inp2 = list(map(int,input().split(' ')))

for i in product(inp1,inp2):
    print(i,end=' ')