"""
Write a function named add_dots that takes a string and adds "." in between each letter. Then, below the add_dots function, write another function named remove_dots that removes all dots from a string
"""
def add_dots(S):
  return ".".join(list(S))
  
def remove_dots(S):
  return "".join(S.split("."))

print(remove_dots(add_dots("Hello Doston")))