"""
Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""

def online_count(status):
  onlineUsers=[]
  for name in status:
    if status.get(name)=="online":
      onlineUsers.append(name)
  return len(onlineUsers)

#Lets Test Our Code
print(online_count({
  "david":"online",
  "hemant":"offline",
  "skylord":"offline",
  "flora":"online",
  "problem":"offline"
}))