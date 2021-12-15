
import time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def total_lines(v,k):
    sum=v
    p=1
    while v>k**p:
        sum+=v//k**p
        p+=1
    return sum


def linear_search(n: int, k: int) -> int:
  # use linear search here
  for v in range(1,n+1):
      if total_lines(v,k)>=n:
          return v
  return 0 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  low=1
  high=n
  while (low<=high):
      mid=(low+high)//2
      if total_lines(mid,k)>=n and total_lines(mid-1,k)<n:
          return mid
      elif total_lines(mid,k)>=n:
          high=mid
      else:
          low=mid


  return 0 # placeholder

# main has been completed for you
# do NOT change anything below this line
def main():
  in_file = open("work.txt", "r")
  num_cases = int((in_file.readline()).strip())

  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str((finish - start)))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()