import sys
input=sys.stdin.readline

N = int(input())

for _ in range(N):
    clothe = []
    type1 = []
    dict = {}
    M = int(input())
    for _ in range(M):
        a,b = map(str,input().split())
        b.strip('\n')
        clothe.append(a)
        type1.append(b)
    for c,t in zip(clothe, type1):
        dict[t] = dict.get(t,0) + 1 
    answer = 1
    for t in dict:
        answer *= (dict[t] + 1)
    print(answer-1)