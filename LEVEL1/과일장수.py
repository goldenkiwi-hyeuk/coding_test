def solution(k, m, score):
  score = sorted(score, reverse = True)
  box = []
  answer = 0
  for i in score:
      box.append(i)
      if len(box) == m:
        answer = answer + min(box)*m
        box = []
  return answer