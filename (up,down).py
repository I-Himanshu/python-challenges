"""parameterfunction named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6)."""
def up_down(N):
  return (N-1,N+1)
  
print(up_down(2))