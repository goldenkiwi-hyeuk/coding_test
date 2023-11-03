def solution(nums):
  from itertools import combinations
  combi = list(combinations(nums, 3))
  sum_list = []
  answer = 0
  for i in combi:
    sum_list.append(sum(i))
  for i in sum_list:
    for j in range(2, int(i**(1/2))+2):
        if i%j == 0:
            break
        if j == int(i**(1/2))+1:
            answer += 1
return answer