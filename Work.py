#  File: Work.py 

#  Description:  Using search algorithms to find the most efficient work strategy

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/20/2022

#  Date Last Modified: 2/20/2022

import sys, time

def num_cups(v: int, n: int, k: int) -> int:
    num_lines = v
    cups = 0
    while num_lines > 0:
        num_lines = v // k ** cups
        n -= num_lines
        
        if n <= 0:
            return cups
        cups += 1

    return -1

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    for v in range(1, n + 1):
        if num_cups(v, n, k) != -1:
            return v
    
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    hi = n
    lo = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if (num_cups(mid, n, k) != -1) and (num_cups(mid - 1, n, k) == -1):
            return mid
        elif num_cups(mid, n, k) == -1:
            lo = mid + 1
        elif num_cups(mid, n, k) != -1:
            hi = mid - 1

# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

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