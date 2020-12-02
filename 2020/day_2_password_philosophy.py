with open("input.txt") as f:
  passwords = [x for x in f]

def info_extract(line):
  """
  Extract usable information from a given password line
  """
  boundary, letter, candidate = line.split()
  lower_limit, upper_limit = boundary.split("-")
 
  return int(lower_limit), int(upper_limit), letter[0], candidate
  
def is_valid_positional(lower_position, upper_position, letter, candidate):
  """
  Check whether letter occurs once only in either the lower_position or upper_position 
  of candidate
  """
  relevant_substring = candidate[lower_position-1] + candidate[upper_position-1]

  return relevant_substring.count(letter) == 1

def is_valid_frequency(lower, upper, letter, candidate):
  """
  Check whether letter occurs lower-upper number of times within candidate
  """
  return candidate.count(letter) in range(lower, upper+1)


def valid_count(passwords, validator):
  """
  Count how many passwords adhere to the password philosophy of the chosen validator
  """
  valid_number = 0
  for line in passwords:
    if validator(*info_extract(line)):
      valid_number += 1
  
  return valid_number

print(valid_count(passwords, is_valid_frequency), "passwords have the required letter frequency")
print(valid_count(passwords, is_valid_positional), "passwords have once instance only of the required letter in a position ")