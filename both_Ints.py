"""
Write a function named both_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise
"""
def both_ints(i1,i2):
  return (type(i1)==int and type(i2)==int);
  
print(both_ints(1,"2"))