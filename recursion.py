# Recursion: A technique where a function calls itself to solve a smaller version of the same problem.
# Base Case: The condition that stops the recursion and prevents infinite calls.
# Recursive Case: The part where the function calls itself with a smaller/simpler input.

# def conumdown(n):
#     # base case
#     if n ==0:
#         return
#     # recursive case
#     print(n)
#     conumdown(n-1)
# conumdown(10)

# Print sum of all number from 1 to n using recursion.

# def sumOfAllNum(n):
#     if n == 0:
#         return 0
#     return n + sumOfAllNum(n-1)
# print(sumOfAllNum(7))

#print factorial of a number using recursion.

# def fectorrialNuma(n):
#     if n==0:
#         return 1
#     return n*(fectorrialNuma(n-1))
# print(fectorrialNuma(5))

# print 1 to n using recursion 

# def print1ton(n):
#     if n==0:
#         return 0
#     print1ton(n-1)
#     print(n)
# print1ton(5)

# WAP to find nth fibonacci number using recursion.

# “The Fibonacci sequence is a sequence where each number is the sum of the previous two numbers. In recursion, we use two base cases for 0 and 1, and the recursive case calculates fib(n-1) + fib(n-2).”

# def fibonocci(n):
#     if n ==0:
#         return 0
#     if n ==1:
#         return 1
#     return fibonocci(n-1)+fibonocci(n-2)
# print(fibonocci(5))

# print sum of elements of a list using recursion.

# def sumOfList(a,i):
#     if i == len(a):
#         return 0
#     return a[i]+sumOfList(a,i+1)
# print(sumOfList([2,3,5,10,50,100],0))

# Check if a string is palindromic using recursion

# def isPalindrome(s, start, end):
#     if start>=end:
#         return True
#     if s[start]!=s[end]:
#         return False
#     return isPalindrome(s,start+1,end-1)
# s="madam"
# print(isPalindrome(s,0,len(s)-1))

# WAP to find nth power of a number using recursion.

# def power(num, n):
#     if n == 0:
#         return 1
#     return num * power(num, n - 1)
# print(power(2, 5))

# Find maximum of an array (list) using recursion.

# def findMax(a, i):
#     # Base case
#     if i == len(a) - 1:
#         return a[i]
#     # Recursive case
#     max_rest = findMax(a, i + 1)
#     return max(a[i], max_rest)
# a = [2, 8, 5, 10, 3]
# print(findMax(a, 0))

# Complete a recursive binary search function. Return the index if found,
# otherwise return -1.

# def binary_search(a, target, left, right):
# 	if left > right:
# 		return -1

# 	middle = (left + right) // 2

# 	if a[middle] == target:
# 		return middle
# 	if target < a[middle]:
# 		return binary_search(a, target, left, middle - 1)
# 	return binary_search(a, target, middle + 1, right)


# a = [2, 5, 8, 12, 16, 23]
# print(binary_search(a, 16, 0, len(a) - 1))
# print(binary_search(a, 10, 0, len(a) - 1))


# Count all the digits in a number using recursion.

# def count_digits(number):
# 	number = abs(number)
# 	if number < 10:
# 		return 1
# 	return 1 + count_digits(number // 10)


# print(count_digits(5072))


# Sum the digits of a number using recursion.

# def sum_digits(number):
# 	number = abs(number)
# 	if number < 10:
# 		return number
# 	return number % 10 + sum_digits(number // 10)


# print(sum_digits(5072))


# Generate all subsequences of a list.

# def subsequences(a, index=0):
# 	if index == len(a):
# 		return [[]]

# 	remaining = subsequences(a, index + 1)
# 	with_current = [[a[index]] + sequence for sequence in remaining]
# 	return with_current + remaining


# print(subsequences([1, 2, 3]))

# Backtracking

# print all the subsequences of a list 

# def subset(a,index,currentPath):
#   if index==len(a):
#     print(currentPath)
#     return
#   currentPath.append(a[index])
#   subset(a,index+1,currentPath)
#   currentPath.pop()
#   subset(a,index+1,currentPath)
# subset([1,2,3],0,[])

# Print all of the combinations of a list which sums to target, assume that every number is reusable. 

# ans=[]

# def cs(a,index,path,target,total):

#   if total==target:
#     ans.append(path.copy())
#     return
#   if total>target:
#     return
#   for i in range(index,len(a)):
#     path.append(a[i])
#     cs(a,i,path,target,total+a[i])
#     path.pop()
# cs([2,3,7,4],0,[],7,0)
# print(ans)

# Combination sum - each element can be used only once.

# def combination_sum_once(numbers, target):
# 	numbers.sort()
# 	answers = []

# 	def backtrack(index, path, total):
# 		if total == target:
# 			answers.append(path.copy())
# 			return

# 		if total > target:
# 			return

# 		for current_index in range(index, len(numbers)):
# 			if current_index > index and numbers[current_index] == numbers[current_index - 1]:
# 				continue
# 			if total + numbers[current_index] > target:
# 				break

# 			path.append(numbers[current_index])
# 			backtrack(current_index + 1, path, total + numbers[current_index])
# 			path.pop()

# 	backtrack(0, [], 0)
# 	return answers

# print(combination_sum_once([2, 3, 2, 7, 4], 7))

# N=6

# board = [["." for _ in range(N)] for _ in range(N)]

# result = []



# def isSafe(row,col):

#   # check for column:

#   for r in range(row):

#     if board[r][col]=="Q":

#       return False



#   # check for upper left diag:



#   r=row-1

#   c=col-1



#   while r>=0 and c>=0:

#     if board[r][c]=='Q':

#       return False

#     r-=1

#     c-=1

#   # check for upper right diag:

#   r=row-1

#   c=col+1

#   while r>=0 and c<N:

#     if board[r][c]=='Q':

#       return False

#     r-=1

#     c+=1



#   return True

  



# def nQueens(row):

#   if row==N:

#     currentAns= ["".join(rowNum) for rowNum in board]

#     result.append(currentAns)

#     return



#   for col in range(N):

#     if isSafe(row,col):

#       board[row][col]="Q"

#       nQueens(row+1)

#       board[row][col]="."



# nQueens(0)

# for ans in result:

#   print(ans)