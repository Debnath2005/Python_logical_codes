# Given a positive number, check if it is a perfect square without using any
# built-in library function. A perfect square is a number that is the square of an integer. 
# Input: n = 25 Output: true Explanation: 25 is a perfect square since it can be written as 5×5.
# Input: n = 20 Output: false

def perfectSquare(n):
  for i in range(2,int(n/2)):
    if i*i==n:
      return True
  return False

n=int(input("Enter any number."))
result=perfectSquare(n)
if result==True:
  print(f"{n} is a perfect square")
else:
  print(f"{n} is not a perfect square")