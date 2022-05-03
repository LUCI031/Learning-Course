# https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python
# def solution(prices):
#     length = len(prices)
#     answer = [ i for i in range (length - 1, -1, -1)]
    
#     stack = [0]
#     for i in range (1, length, 1):
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
#     return answer

from collections import deque

def solution(prices):
    que = deque(prices)
    answer = []
    while True:
        curr = que.popleft()
        cnt = 0
        length = len(que)
        if length > 0:
            for i in range(length):
                if prices[i] >= curr:
                    cnt += 1
                else:
                    cnt += 1
                    break
            answer.append(cnt)
        else:
            answer.append(0)
            break
    return answer

print(solution([1,2,3,2,3]))