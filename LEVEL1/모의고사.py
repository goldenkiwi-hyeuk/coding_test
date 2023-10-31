def solution(answers):
  num_1 = [1,2,3,4,5]
  num_2 = [2,1,2,3,2,4,2,5]
  num_3 = [3,3,1,1,2,2,4,4,5,5]
  collects = [0,0,0]
  result = []
  for i in range(len(answers)):
    if answers[i] == num_1[i%5]:
        collects[0] += 1
    if answers[i] == num_2[i%8]:
        collects[1] += 1
    if answers[i] == num_3[i%10]:
        collects[2] += 1
  for i, collect in enumerate(collects):
    if max(collects) == collect:
        result.append(i+1)
  return result