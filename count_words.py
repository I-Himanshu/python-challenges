"""
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens,
"""
def count(S):
  return len(S.split("-"))

print(count("i-have-4-words"))