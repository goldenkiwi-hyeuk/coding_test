def solution(nums):
  if len(set(nums)) > int(len(nums)/2):
      return int(len(nums)/2)
  else:
      return len(set(nums))