"""
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""
def is_anagram(s1,s2):
  s1=list(s1)
  s2=list(s2)
  s1.sort()
  s2.sort()
  return s1==s2

print(is_anagram("hey","yeh"))