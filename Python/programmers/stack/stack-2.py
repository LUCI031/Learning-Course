def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

# def solution(priorities, location):
#     cnt = 1
#     loc = priorities[location]
#     f_loc = priorities[0]
#     if loc >= max(priorities) and priorities.count(loc)==1:
#         return 1
#     elif loc >= max(priorities):
#         for i in priorities[:location+1]:
#             if i == loc:
#                 cnt +=1
#         return cnt
#     else:
#         num = priorities[location]
#         priorities.remove(priorities[location])
#         priorities.append(num)
#         for i in priorities[:-1]:
#             if i >= priorities[-1]:
#                 cnt +=1
#         return cnt


# print(solution([2,1,3,2],2))
# print(solution([1, 1, 9, 1, 1, 1],0))
print(solution([2, 3, 3, 2, 9, 3, 3] , 3))
# print(solution([1,2,3] , 0))
# print(solution([1, 1, 1, 1, 1, 1] , 3))