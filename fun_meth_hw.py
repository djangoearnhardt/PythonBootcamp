# Python3 Bootcamp Section 6 Functions and Methods HW

# Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
	return (rad ** 3) * (4/3) * math.pi

# Write a function that checks whether a number is in a given range (inclusive of high and low)
# One with printed results

def ran_check(num,low,high):
	if low < num < high:
		return print(num, 'is in the range between' ,low, 'and', high)

# One with Boolean

def ran_check(num,low,high):
	if low < num < high:
		return True

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s='Hello Mr. Rogers, how are you this fine Tuesday?'):
	count_up=0
	count_down=0
	for i in s:
		if i.isupper():
			count_up += 1
		elif i.islower():
			count_down += 1
		else:
			pass
	print('Original String:',s)
	print('No. of Upper case characters:',count_up)
	print('No. of Lower case characters:',count_down)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l=[1,1,1,1,2,2,2,4,4,4]):
	x = []
	for a in l:
		if a not in x:
			x.append(a)
	return x

# Write a Python function to multiply all the numbers in a list.

def multiply(numbers=[1,2,3,-4]):
	i = numbers[0]
	for num in numbers:
		i *= num
	return i

# Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(s='helleh'):
	return s == s[::-1]

# Write a Python function to check whether a string is pangram or not.
# I had to watch the video for this solution

import string
def ispangram(str1='The quick brown fox jumps over the lazy dog', alphabet=string.ascii_lowercase):
	alphaset = set(alphabet)
	return alphaset <= set(str1.lower())
