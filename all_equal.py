"""
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""
def all_equal(L):
  if len(set(L))<=1:
    return True
  else:
    return False
    
print(all_equal([1,2,3,4]))
print(all_equal([2,2,2,2]))