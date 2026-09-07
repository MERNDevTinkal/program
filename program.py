# Solution: print numbers from 0 to 100
# start = 0
# while start <= 100:
#     print(start)
#     start = start + 1

# Solution: print odd numbers between 1 and 1000
# number = 1

# while number <= 1000:
#     if number % 2 != 0:
#         print(number)
#     number = number + 1

# Solution: print numbers from 100 down to 1
# num = 100

# while num >= 1 :
#     print (num)
#     num = num -1

# Solution: print multiplication table of 68 from 1 to 10
# counter = 1
# while counter <= 10:
#     table = counter * 68
#     print(table)
#     counter = counter + 1

# Solution: sum all even numbers from 1 to 100000
# number = 1
# total =0

# while number <= 100000:
#     if number % 2 == 0:
#         total = total + number
#     number = number + 1
#     print(total)

# Solution: compute the sum of numbers from 1 to 9999
# total = 0
# for i in range (1,10000):
#     total = total + i
# print(total)

# Solution: print numbers from 1000 down to 1
# for i in range(1000,0,-1):
#     print(i)

# Solution: print a star for each number from 1 to N
# input= int(input("please enter a number"))
# for intput in range(1,input+1):
#     print(f"*")

# Solution: print multiplication table for the entered number
# table_to_print = int(input("please enter the table print number"))

# startFrom = 1
# end = 10

# for i in range(startFrom,end+1):
#     table= (i*table_to_print)
#     print(table)

# Solution: print numbers divisible by 8 from 50 to 500
# for i in range (50,501):
#     if (i % 8) == 0:
#         print(i)

# Solution: count numbers from 1 to 1000 that are divisible by both 3 and 5
# count = 0

# for i in range (1,1001):
#     if (i % 3 and 5) == 0:
#         count= count + 1
#         print(count)

# Solution: nested loops printing pairs (i, j)
# for i in range (1,5):
#     for j in range (1,4):
#      print(i, j)

# Solution: print a square of stars of size N
# userInput = int(input("Please enter number or row and col to print"))
# for i in range(userInput):
#     for j in range(userInput):
#         print("*",end="")
#     print() 
# 
# Solution: print a grid where each row repeats the row number
# userInput = int(input("Please enter number or row and col to print"))
# for i in range(1,userInput+1):
#     for j in range(1,userInput+1):
#         print(i,end="")
#     print()   

# Solution: print a grid where each row repeats the column number
# userInput = int(input("Please enter number or row and col to print"))
# for i in range(1,userInput+1):
#     for j in range(1,userInput+1):
#         print(j,end="")
#     print()    

# Solution: print multiplication tables for numbers 1 to N
# userInput=int(input("Please enter a number"))
# startFrom=1
# printTo=11

# for i in range(1,userInput+1):
#     for j in range(startFrom,printTo):
#         table=i*j
#         print(table)

# Solution: print a numeric triangle pattern (mountain shape)
# mountainTOPrint=int(input("please enter mountain number"))
# for i in range(1,mountainTOPrint+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Solution: print an increasing triangle of stars
# userInput=int(input("please enter number to print star"))
# for i in range(1,userInput+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# Solution: print a decreasing triangle of stars
# userInput=int(input("please enter number to print star"))
# for i in range(userInput+1,1,-1):
#     for j in range(i,1,-1):
#         print("*",end="")
#     print()

# Solution: print descending numbers from N to 1 in each row
# userInput = int(input("Please enter number"))
# for i in range(1,userInput+1):
#     for j in range(userInput,userInput-i,-1):
#         print(j,end="")
#     print()


# n1=int(input("Please enter first number : "))
# n2=int(input("Please enter second number : "))

# for i in range(1,n1+1):
#     for j in range(1,n2+1):
#         print(i,j)
#     print()

# factcheckstart=1
# fectcheckend=1000

# for i in range(factcheckstart,fectcheckend+1):
#     for j in range(factcheckstart,i+1):
#         if(i%j) == 0:
#             print(i,j)
#     print()


# for i in range(1,8):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(8,1,-1):
#     for j in range(i-1,1,-1):
#         print("*",end="")
#     print()

# Solution: print each element of a fixed list by index
# numbers=[1,32,3,4,5,36,7,8,9,140]

# for i in range(0,10):
#     print(numbers[i])

# Solution: iterate over array elements directly and print each value
# arr=[3,43,5,43,23,54,2,1]

# for i in arr:
#     print(i)

# Solution: demonstrate looping through array indices (buggy print of array each time)
# array=[23,324,2,1,43,5,334,23,23,548,]
# for i in range(len(array)):
#     print(array[i])

# Solution: replace values at odd indices with -1
# numbers=[32,43,54,65,76,5434,23,65,34,4,543,43,]
# for i in range(0,len(numbers)):
#     if i % 2 != 0:
#         numbers[i]=-1
# print(numbers)

# Solution: read 10 numbers from input and compute their total sum
# arr=[]
# sum=0
# for i in range(0,10):
#     arrData=int(input("please enter array data to append"))
#     arr.append(arrData)
#     sum=sum+arrData
# print(arr)    
# print(sum)

# Solution: find maximum value in a list read from input
# arr=list(map(int, input().split()))
# maxium=arr[0]
# for i in range(len(arr)):
#     if arr[i]>maxium:
#         maxium=arr[i]
# print(arr)
# print(maxium)

# Solution: reverse an array by appending values from the end to a new list
# array=[4,54,78,45,12,56,0,5,47,8]
# newarray=[]
# for i in range(len(array)-1,-1,-1):
#     newarray.append(array[i])
# print(newarray)    

# Solution: count how many times a number appears in the input list
# arraylist=list(map(int,input().split()))
# numberx=int(input("please enter number to find"))
# howManyTimes=0

# for i in range(0,len(arraylist)):
#     if numberx == arraylist[i]:
#         howManyTimes=howManyTimes+1
# print(arraylist)
# print(numberx)
# print(howManyTimes)

# Solution: print frequency of each element in the list
# arraylist=list(map(int,input().split()))

# for i in range(0,len(arraylist)):
#     currentEle=arraylist[i]
#     howManyTimes=0
#     for j in range(len(arraylist)):
#         if currentEle == arraylist[j]:
#             howManyTimes=howManyTimes+1
#     print(currentEle,howManyTimes)

# Solution: search for the last occurrence of an element in the list
# arraylist=list(map(int,input("please enter array").split()))
# searchElement=int(input("please enter enement to search in arraylist"))

# for i in range(len(arraylist)-1,-1,-1):
#     if searchElement == arraylist[i]:
#      print(i)
#      break

# Solution: rotate an array right by one position
# arrayList =[8,4,5,6,7,8,9,10]
# lastEle=arrayList[len(arrayList)-1]
# for i in range(len(arrayList)-1,0,-1):
#     arrayList[i]=arrayList[i-1]
# arrayList[0]=lastEle
# print(arrayList)

# Solution: find the smallest element in an array
# array=[23,3,-1,232,23,23,0,2,3,4,5,5,3,0]

# smallestEle=array[0]

# for i in range(len(array)):
#     if array[i]<=smallestEle:
#         smallestEle=array[i]
# print(smallestEle)

# Solution: selection sort an array in ascending order
# Find smallest
#       ↓
# Put it at correct position
#       ↓
# Find next smallest
#       ↓
# Put it at correct position
#       ↓
# Repeat
# array=[3,5,0,1,21,43,6,84,5,3,5,4,6,7]

# for i in range(len(array)):
#     minEle=i
#     for j in range(i+1,len(array)):
#         if array[j]<array[minEle]:
#             minEle=j
#     array[i],array[minEle]=array[minEle],array[i]
# print(array)

# Solution: bubble sort an array in ascending order
# array=[32,4,2,2,1,2,3,0,7,5,70,5,0,1]
# for i in range(len(array)):
#     for j in range(len(array)-i-1):
#         if array[j]>array[j+1]:
#             array[j],array[j+1]=array[j+1],array[j]
# print(array)

# Solution: merge two sorted arrays into one sorted result
# a = [1, 3, 5, 7]
# b = [2, 4, 6, 8]

# i = 0
# j = 0
# result = []

# while i < len(a) and j < len(b):

#     if a[i] <= b[j]:
#         result.append(a[i])
#         i += 1
#     else:
#         result.append(b[j])
#         j += 1

# # Add remaining elements from a
# while i < len(a):
#     result.append(a[i])
#     i += 1

# # Add remaining elements from b
# while j < len(b):
#     result.append(b[j])
#     j += 1

# print(result)

# Solution: brute-force check for a pair that sums to 100 in a sorted list
# sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# sum=100
# isSumFound=False
# for i in range(len(sorted_list)):
#     for j in range(i+1,len(sorted_list)):
#         if sorted_list[i]+sorted_list[j] == sum:
#             isSumFound=True
#             print(sorted_list[i],sorted_list[j])
#             break
#     if isSumFound==True:
#         break
#     print(isSumFound)

# Solution: two-pointer search on a sorted array to find two numbers that sum to 100
# sortedarray=[20,30,40,50,60,70,80,90]
# sumtoFind=100
# left=0
# reight=len(sortedarray)-1

# current=0

# while left < reight:
#     current = sortedarray[left] + sortedarray[reight]
#     if current == sumtoFind:
#         print("sumtofind founded")
#         print(sumtoFind,current)
#         print(sortedarray[left], sortedarray[reight])
#         break
#     if current > sumtoFind:
#         reight=reight-1
#     else:
#         left=left+1

# Solution: merge two sorted arrays with two pointers (merge step in merge sort)
# firstArray=[1,2,3,4,5,6,7,8,9]
# secondArray=[10,11,12,13,14,15,16,17,18,19]

# finalArray=[]
# i=0
# j=0

# while i < len(firstArray) and j < len(secondArray):
#     if firstArray[i]<=secondArray[j]:
#         finalArray.append(firstArray[i])
#         i+=1
#     else:
#         finalArray.append(secondArray[j])
#         j+=1
# while i < len(firstArray):
#     finalArray.append(firstArray[i])
#     i+=1

# while j < len(secondArray):
#     finalArray.append(secondArray[j])
#     j+=1
# print(finalArray)

# Solution: optimized two-pointer sum check in a sorted list for target 100
# sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# sumNumber=100

# left=0
# right=len(sorted_list)-1

# while left < right:
#     curent = sorted_list[left]+sorted_list[right]
#     if curent == sumNumber:
#         print(curent,sumNumber,sorted_list[left],sorted_list[right])
#         break
#     if curent > sumNumber:
#         right-=1
#     else:
#         left+=1

# # Check if list given by users is palindromic or not?

# a = [1,1,2,3,2,1,1]

# isPlaindrom=True
# left=0
# right=len(a)-1

# while left < right:
#     if a[left]==a[right]:
#         isPlaindrom=True
#         left+=1
#         right-=1
#     else:
#         isPlaindrom=False
#         break
# print(isPlaindrom)

# reverse a list using 2 pointers.

# a = [1,1,2,3,2,1,6]

# left=0
# right=len(a)-1

# while left<right:
#     a[left],a[right]=a[right],a[left]
#     left+=1
#     right-=1
# print(a)

# Find all the pairs which sums to a target.

# a = [1,2,3,4,5,6,8]

# target=int(input("Please enter taget numbers to find tahir pair all pair"))

# left=0
# right=len(a)-1
# current=0

# while left<right:
#     current=a[left]+a[right]
#     if current == target:
#         print(f"pair found target : {target} current : {current} element : {a[left]} and {a[right]}")
#         left+=1
#         right-=1
#     if current > target:
#         right-=1
#     if current < target:
#         left+=1 

# Count the number of pairs in  a sorted list which sums to target.

# a = [1,2,3,4,5,6,8]

# target=int(input("Please enter taget numbers to find tahir pair all pair"))

# left=0
# right=len(a)-1
# current=0
# count=0

# while left<right:
#     current=a[left]+a[right]
#     if current == target:
#         print(f"pair found target : {target} current : {current} element : {a[left]} and {a[right]}")
#         count+=1
#         left+=1
#         right-=1
#     if current > target:
#         right-=1
#     if current < target:
#         left+=1 
# print("count",count)


# remove duplicates from an sorted arrray/list

# arrayList=[1,1,1,2,2,3,3,4,5,5,6,7,8,9,9]

# slow=0

# for fast in range(1,len(arrayList)):
#     if arrayList[slow]!=arrayList[fast]:
#         slow+=1
#         arrayList[slow]=arrayList[fast]
# print(arrayList[:slow+1])

# Move all zeros in a list at the end without changing the order of elements

# a = [0, 1, 0, 3, 12]

# slow=0

# for fast in range(len(a)):
#     if a[fast] != 0:
#         a[slow],a[fast]=a[fast],a[slow]
#         slow+=1
# print(a)

#  sliding window - find maximum sub of subArray of size k
# arrayList=[1,2,3,4,5,6,7,8,9]
# size=3

# WindowSum=0

# for i in range(size):
#     WindowSum += arrayList[i]
#     ans=WindowSum
# for i in range(size,len(arrayList)):
#     newWindownSum = WindowSum + arrayList[i] - arrayList[i-size]
#     WindowSum = newWindownSum
#     ans= max(ans,WindowSum)
# print(ans)

# Find maximum avg subarray value of size k

# sortedArray=[10,11,21,22,31,32,40,43,52,65,66]
# size=3

# maxsum=0
# maxAvarage=0

# for i in range(size):
#     maxsum = maxsum + sortedArray[i]
# maxAvarage = maxsum/size
# ans=maxAvarage

# for i in range(size,len(sortedArray)):
#     maxsum= maxsum + sortedArray[i] - sortedArray[i-size]
#     maxAvarage= maxsum / size
#     ans=max(ans,maxAvarage)

# print(ans)

# Find the length of Smallest Subarray with Sum>=Target

# sortedArray = [10,11,21,22,31,32,40,43,52,65,66,70]
# target = 70

# left = 0
# windowSum = 0
# minLength = len(sortedArray) + 1

# for right in range(len(sortedArray)):

#     windowSum = windowSum + sortedArray[right]

#     while windowSum >= target:

#         currentLength = right - left + 1

#         minLength = min(minLength, currentLength)

#         windowSum = windowSum - sortedArray[left]

#         left = left + 1

# print(minLength)

# Given an array of non-negative integers representing an elevation map, where width of each bar is 1, calculate how much water can be trapped after raining. 🌧️ TRAPPING RAIN WATER

# height = [4, 2, 0, 3, 2, 5]


# right=len(height)-1
# left=0
# leftMax=0
# rightMax=0
# water=0

# while left < right:
#     if height[left] < height[right]:

#         if height[left] >= leftMax:
#             leftMax = height[left]
#         else :
#             water = water + leftMax - height[left]
#         left+=1
#     else:
#         if height[right] >= rightMax:
#             rightMax = height[right]
#         else:
#             water = water + rightMax - height[right]
#         right -=1
# print(water)

# # 🪣 CONTAINER WITH MOST WATER
# # Given an array of non-negative integers where each integer represents the height of a vertical line and the distance between adjacent lines is 1, find two lines that can form a container with the maximum possible area.

# height = [2, 7, 8, 9, 3, 1, 16, 4]

# left=0
# right=len(height)-1
# maxArea=0

# while left < right:
#     area = min(height[left], height[right]) * (right-left)
#     maxArea = max(maxArea,area)
#     if height[left] <= height[right]:
#         left+=1
#     else:
#         right-=1
# print(maxArea)

# Reverse a string

# name="Tinkal kumar"
# newName=""

# for i in range(len(name)-1,-1,-1):
#     newName+=name[i]
# print(newName)

# check if a string is palindrome 

# s = "madam"

# left = 0
# right = len(s) - 1

# isPalindrome = True

# while left < right:

#     if s[left] != s[right]:
#         isPalindrome = False
#         break

#     left += 1
#     right -= 1

# print(isPalindrome)

# count number of vowels in a string

# name = "Tinkal kumar"
# count=0

# for i in name.lower():
#     if i in "aeiou":
#         count+=1
# print(count)

# Problem: Longest Substring Without Repeating Characters

# Question keh raha hai:

# Ek string di hui hai. Humein sabse lambi continuous substring find karni hai jisme koi character repeat na ho.

# stringName="abcabcbbnewdlqwertrewq"

# left=0
# right=0
# maxContiousWindowSize=0
# window=set()

# for right in range(len(stringName)):
#     while stringName[right] in window:
#         window.remove(stringName[left])
#         left+=1
#     window.add(stringName[right])
#     currentWindowSize = right - left +1
#     maxContiousWindowSize= max(maxContiousWindowSize,currentWindowSize)
# print(maxContiousWindowSize)

# Prefix Sum

# given array a, print prefix sum array

# a=[2,1,3,4,4,9]

# for i in range(1,len(a)):
#     a[i]+= a[i-1]
# print(a)

# find pivot element Given an array a, find the index where: sum of elements on LEFT == sum of elements on RIGHT

# a=[1,7,3,6,5,6]

# totalsum=sum(a)
# leftsum=0
# count=0

# for i in range(len(a)):
#     rightsum=totalsum-leftsum-a[i]
#     if leftsum==rightsum:
#         print("pivot element found at index",i)
#         count+=1
#     leftsum+=a[i]
# print("total pivot element found",count)

# Given an integer list, find the frequency of every element.
# freq = {
#     number: how_many_times_seen
# }

# a = [2, 1, 2, 3, 1, 2, 4, 3]
# freq={}

# for i in range(len(a)):
#     if a[i] in freq:
#         freq[a[i]] +=1
#     else:
#         freq[a[i]] =1
# print(freq)

# Find the maximum sum of a subarray in a integer list -- Kadane's Algorithm.

# a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# currentsum=a[0]
# maxsum=a[0]

# for i in range(1,len(a)):
#     currentsum=max(a[i],currentsum+a[i])
#     maxsum=max(maxsum,currentsum)
# print(maxsum)

# def tinkal(role):
#     print("Hello Tinkal",role)
# tinkal("Developer")
# tinkal("User")

# Create a function which prints multiplication table of the number which is getting passed in the function as Parameter

# def print_multiplication_table(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")
# print_multiplication_table(5)

# Create a function which returns the avg of a list passed as a parameter.

# def getAverage(a):
#     return sum(a)/len(a)
# result =getAverage([1,2,3,4,5])
# print(result)

# create a function to find max in a list

# def findMax(a):
#     maxValue=a[0]
#     for i in range(1,len(a)):
#         if a[i]>maxValue:
#             maxValue=a[i]
#     return maxValue
# print(findMax([1,2,3,4,5,6,7,8,9,10]))

# create Bubble sort function and return the sorted list from it.
# def bubbleSort(a):
#     for i in range (len(a)):
#         for j in range(0,len(a)-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# bubbleSortResult=bubbleSort([5,4,3,2,1])
# print(bubbleSortResult)

# 2D array
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=" ")
#     print()

# 2D integer list -> find sum of all elements

# a=[[1, 2, 3], [4, 5,6,1,3,5, 6], [7, 8,5, 9]]
# totalSum=0
# for row in a:
#     for ele in row:
#         totalSum+=ele
# print(totalSum)

# create a function which returns maximum element of a 2d list passes as an argument.

# def findMaxelementintwoDList(a):
#     maxValue=a[0][0]
#     for row in a:
#         for ele in row:
#             if ele > maxValue:
#                 maxValue=ele
#     return maxValue
# print(findMaxelementintwoDList([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# print sum of every row
# a=[[1, 2, 3], [4, 5,6,1,3,5, 6], [7, 8,5, 9]]

# totalSum=0
# for i in range(len(a)):
#     rowSum=0
#     for j in range(len(a[i])):
#         rowSum+=a[i][j]
#         totalSum+=a[i][j]
#     print(rowSum)

# print(f"Total Sum: {totalSum}")

# print sum of every column of a 2d list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# total = 0
# for j in range(len(matrix[0])):
#     colSum = 0
#     for i in range(len(matrix)):
#         colSum += matrix[i][j]
#     print(colSum)

# create a function which returns the number of even numbers in a 2d list.
# def countEvenNumbersIn2DList(a):
#     count = 0
#     for row in a:
#         for ele in row:
#             if ele % 2 == 0:
#                 count += 1
#     return count

# print(countEvenNumbersIn2DList([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# find the main diagonal sum of a square matrix
# def mainDiagonalSum(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         total += matrix[i][i]
#     return total
# result = mainDiagonalSum([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(result)

# find the secondary diagonal sum of a square matrix

# def secondaryDiagonalSum(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         total += matrix[i][len(matrix) - 1 - i]
#     return total
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(secondaryDiagonalSum(matrix))

# Create a function which returns the sum of primary diagonal + secondary diagonal of a square matrix.
# def diagonalSum(matrix):

#     total = 0

#     for i in range(len(matrix)):

#         # Primary diagonal
#         total += matrix[i][i]

#         # Secondary diagonal
#         total += matrix[i][len(matrix) - 1 - i]

#     return total


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(diagonalSum(matrix))

# Print all the boundary elements of a 2D list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# rows = len(matrix)
# cols = len(matrix[0])
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print(matrix[i][j])

# Rotate a matrix by 90 deg clockwise
# def rotateClockwise(a):

#     # TRANSPOSE
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             a[i][j], a[j][i] = a[j][i], a[i][j]

#     # REVERSE EACH ROW WHILE PRINTING
#     for i in range(len(a)):
#         for j in range(len(a[0]) - 1, -1, -1):
#             print(a[i][j], end=" ")
#         print()
# rotateClockwise([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# Print Anticlockwise rotation of a 2d list.

# def rotateAnticlockwise(a):
#     # Step 1: Transpose
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             a[i][j], a[j][i] = a[j][i], a[i][j]
#     # Step 2: Print rows from bottom to top
#     for i in range(len(a) - 1, -1, -1):
#         for j in range(len(a[0])):
#             print(a[i][j], end=" ")
#         print()
# rotateAnticlockwise([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# Print spiral traversal of a matrix.

# a = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# direction = "right"

# topBoundary = 0
# bottomBoundary = len(a) - 1

# leftBoundary = 0
# rightBoundary = len(a[0]) - 1


# while leftBoundary <= rightBoundary and topBoundary <= bottomBoundary:

#     if direction == "right":

#         for i in range(leftBoundary, rightBoundary + 1):
#             print(a[topBoundary][i], end=" ")

#         direction = "down"
#         topBoundary += 1

#     elif direction == "down":

#         for i in range(topBoundary, bottomBoundary + 1):
#             print(a[i][rightBoundary], end=" ")

#         direction = "left"
#         rightBoundary -= 1

#     elif direction == "left":

#         for i in range(rightBoundary, leftBoundary - 1, -1):
#             print(a[bottomBoundary][i], end=" ")

#         direction = "up"
#         bottomBoundary -= 1

#     else:

#         for i in range(bottomBoundary, topBoundary - 1, -1):
#             print(a[i][leftBoundary], end=" ")

#         direction = "right"
#         leftBoundary += 1

# Binary Search

# /    normal division → can give float
# //  floor division → gives integer

# def binarySearch(a,target):
#     left=0
#     right=len(a)-1
#     isFound=False

#     while left <= right:
#         mid = (left + right) // 2
#         if a[mid] == target:
#             isFound = True
#             print("Target found at index", mid, "Value:", a[mid])
#             break
#         elif a[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# binarySearch([1,2,3,4,5,6,7,8,9,99],99)

# Find the first occurence of target in a sort list.

# def firstOccurence(a,target):
#     left=0
#     right=len(a)-1
#     firstOccuranceIndex=-1
#     isFound=False
#     while left <= right:
#         mid=(left + right ) // 2
#         if a[mid] == target:
#             isFound=True
#             firstOccuranceIndex=mid
#             break
#         elif a[mid] < target:
#             left=mid+1
#         else:
#             right=mid-1
#     print(isFound,firstOccuranceIndex)

# firstOccurence([1,2,3,4,5,6,7,8,9,99],99)

# return the last occurence of target in a sorted list


# def lastOccurence(a,target):
#     left=0
#     right=len(a)-1
#     lastOccuranceIndex=-1
#     isFound=False
#     while left <= right:
#         mid=(left + right ) // 2
#         if a[mid] == target:
#             isFound=True
#             lastOccuranceIndex=mid
#             left=mid+1
            
#         elif a[mid] < target:
#             left=mid+1
#         else:
#             right=mid-1
#     print(isFound,lastOccuranceIndex)

# lastOccurence([1,2,3,4,5,6,7,8,9,99,99,99],99)

# create a function which returns the first and last ocurrence of a target in a list format 

# def firstAndLastOccurrence(a, target):

#     # First occurrence
#     left = 0
#     right = len(a) - 1
#     first = -1

#     while left <= right:

#         mid = (left + right) // 2

#         if a[mid] == target:
#             first = mid
#             right = mid - 1

#         elif a[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     # Last occurrence
#     left = 0
#     right = len(a) - 1
#     last = -1

#     while left <= right:

#         mid = (left + right) // 2

#         if a[mid] == target:
#             last = mid
#             left = mid + 1

#         elif a[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return [first, last]


# a = [1, 2, 3, 4, 7, 7, 7, 8]

# print(firstAndLastOccurrence(a, 7))

# create a function which returns the index where a target should be inserted in a sorted list.

# def searchInsert(a, target):
#     left = 0
#     right = len(a) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if a[mid] == target:
#             return mid

#         elif a[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return left
# print(searchInsert([1, 3, 5, 6], 5))
# # 2

# print(searchInsert([1, 3, 5, 6], 4))
# # 2

# print(searchInsert([1, 3, 5, 6], 7))
# # 4

# print(searchInsert([1, 3, 5, 6], 0))
# # 0

# Find Lower Bound - Find the first index where a[i] >=t

# def lowerBound(a, target):

#     left = 0
#     right = len(a) - 1
#     answer = -1

#     while left <= right:

#         mid = (left + right) // 2

#         if a[mid] >= target:
#             answer = mid
#             right = mid - 1
#         else:
#             left = mid + 1

#     return answer

# Upper bound (first index where a[i]>target)

# def upperBound(a, target):
#     left = 0
#     right = len(a) - 1
#     answer = len(a)

#     while left <= right:
#         mid = (left + right) // 2

#         if a[mid] > target:
#             answer = mid
#             right = mid - 1
#         else:
#             left = mid + 1

#     return answer

# find the minimum element in the rotated sorted list 

# def findMin(a):
#     left = 0
#     right = len(a) - 1

#     while left < right:
#         mid = (left + right) // 2

#         if a[mid] > a[right]:
#             left = mid + 1
#         else:
#             right = mid

#     return a[left]

#  a = [4, 5, 6, 7, 0, 1, 2]
# print(findMin(a))

# Given a sorted list and target, return the indices of two numbers whose num is target.

# def twoSum(a, target):

#     left = 0
#     right = len(a) - 1

#     while left < right:

#         currentSum = a[left] + a[right]

#         if currentSum == target:
#             return [left, right]

#         elif currentSum < target:
#             left += 1

#         else:
#             right -= 1

#     return [-1, -1]


# a = [1, 2, 3, 4, 6]
# target = 10

# print(twoSum(a, target))

# rotate a 2D list by 90 deg clockwise. 

# def rotate90(a):

#     n = len(a)

#     # Step 1: Transpose
#     for i in range(n):
#         for j in range(i + 1, n):

#             temp = a[i][j]
#             a[i][j] = a[j][i]
#             a[j][i] = temp

#     # Step 2: Reverse every row
#     for i in range(n):

#         left = 0
#         right = n - 1

#         while left < right:

#             temp = a[i][left]
#             a[i][left] = a[i][right]
#             a[i][right] = temp

#             left += 1
#             right -= 1

#     return a


# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(rotate90(a))

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# def maxProfit(prices):

#     minPrice = prices[0]
#     maxProfit = 0

#     for i in range(1, len(prices)):

#         if prices[i] < minPrice:
#             minPrice = prices[i]

#         profit = prices[i] - minPrice

#         if profit > maxProfit:
#             maxProfit = profit

#     return maxProfit


# prices = [7, 1, 5, 3, 6, 4]

# print(maxProfit(prices))

# Check if a two strings given as a parameters of a function is valid anagram or not

# if freq[ele] < 0

# Ye second string ko process karte waqt hai.

# Humne pehle s1 ke characters count kiye:

# s1 = "aab"

# freq = {
#     a: 2,
#     b: 1
# }

# Ab s2 maan lo:

# s2 = "aaa"

# Hum har character ka count minus 1 karte hain:

# freq[ele] -= 1

# 1. freq.get(ele, 0) kya karta hai?

# Ye dictionary se ele ki current value nikalta hai
# freq = {"a": 2, "b": 1}

# Agar:

# freq.get("a", 0)

# toh result:

# 2

# Kyunki "a" already hai.

# Agar:

# freq.get("c", 0)

# toh result:

# 0

# Kyunki "c" dictionary mein nahi hai.

# So:

# freq.get(ele, 0)

# ka matlab:

# ele hai toh uski value do, nahi hai toh 0 do.

# def isValidAnagram(s1, s2):

#     if len(s1) != len(s2):
#         return False

#     freq = {}

#     # s1 ke characters ka count
#     for ele in s1:
#         freq[ele] = freq.get(ele, 0) + 1

#     # s2 ke characters ko count se minus karo
#     for ele in s2:

#         if ele not in freq:
#             return False

#         freq[ele] -= 1

#         if freq[ele] < 0:
#             return False

#     return True


# print(isValidAnagram("cat", "act"))
# print(isValidAnagram("apple", "plea"))

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# def mergeIntervals(intervals):

#     result = []

#     result.append(intervals[0])

#     for i in range(1, len(intervals)):

#         current = intervals[i]
#         last = result[-1]

#         if current[0] <= last[1]:
#             last[1] = max(last[1], current[1])

#         else:
#             result.append(current)

#     return result


# intervals = [[1,3], [2,6], [8,10], [15,18]]

# for non sorted intervals, you should sort them first based on the start time before merging. Here's the complete code with sorting included:

# def mergeIntervals(intervals):

#     intervals.sort()

#     result = []
#     result.append(intervals[0])

#     for i in range(1, len(intervals)):

#         current = intervals[i]
#         last = result[-1]

#         if current[0] <= last[1]:
#             last[1] = max(last[1], current[1])
#         else:
#             result.append(current)

#     return result

# print(mergeIntervals(intervals))

# Given a string as a parameter of a function, return the length of longest substring which contains non repeating characters.
# def lengthOfLongestSubstring(s):
#     charSet = set()
#     left = 0
#     maxLength = 0

#     for right in range(len(s)):
#         while s[right] in charSet:
#             charSet.remove(s[left])
#             left += 1
#         charSet.add(s[right])
#         maxLength = max(maxLength, right - left + 1)

#     return maxLength

# print(lengthOfLongestSubstring("abcabcbb"))  
# print(lengthOfLongestSubstring("bbbbb"))     
# print(lengthOfLongestSubstring("pwwkew"))   

