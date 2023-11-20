def solution(n):
  even_num = 2
  answer = 0
  while even_num <= n:
    answer += even_num
    even_num += 2
  return answer