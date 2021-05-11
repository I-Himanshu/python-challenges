print("""
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
""")
def mid(S):
  """Return Middle Letter of string or return empty string if no middle letter found"""
  S_len=len(S)
  if(S_len%2==0): #if length of string is even
    return ""
  else:           #if length of string is odd
    return S[S_len-2]
    
print(mid("abcdef"))
print(mid("abcde"))