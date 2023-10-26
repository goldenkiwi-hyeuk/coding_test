def solution(a, b):
  mon_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
  if a > 1:
      while a!=1 :
          b += mon_list[a-2]
          a -= 1
  answer = day_list[((b-1)%7)]
  return answer