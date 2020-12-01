with open("input.txt") as f:
  numbers = [int(x) for x in f]

def special_pair(nums):
  pair = [(a, b) for a in nums for b in nums if a + b == 2020]
  return pair[0][0] * pair[0][1]

def special_triple(nums):
  triple = [(a, b, c) for a in nums for b in nums for c in nums if a + b + c == 2020]
  return triple[0][0] * triple[0][1] * triple[0][2]

print(special_pair(numbers))
print(special_triple(numbers))
