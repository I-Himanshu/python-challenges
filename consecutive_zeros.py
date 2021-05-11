"""
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""
def consecutive_zeros(S):
  max_zero=0
  temp_zero=0
  for i in S:
    if (int(i)==0):
      temp_zero+=1
    else:
      temp_zero=0
    if temp_zero>max_zero:
        max_zero=temp_zero
  return max_zero
  
print(consecutive_zeros("1001101000110"))