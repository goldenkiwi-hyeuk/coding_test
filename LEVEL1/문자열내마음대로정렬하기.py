def solution(strings, n):
  check = []
  answer = []
  answer1 = []
  for i in strings:
    check.append(i[n])
  check = sorted(check)
  for i in check:
    for j in strings:
        if i == j[n]:
            answer1.append(j)
    answer1 = sorted(answer1)
    answer.extend(answer1)
    for i in answer1:
        strings.remove(i)
    answer1 = []
  return answer