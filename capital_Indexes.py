print("""
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]
""")
def capital_indexes(s):
  """Take A String And Return Indexes of all capital letters as list"""
  indexes=[]
  for index, letter in enumerate(list(s)):
    if letter.isupper():
      indexes.append(index)
  return indexes
  
print("Result: \n")
print(capital_indexes("tHis String iS fOr testing purpose only"))