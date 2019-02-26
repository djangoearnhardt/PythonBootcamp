# Python3 Bootcamp Section 6 Function Practice Exercises

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_events(a,b):
	if a % 2 == 0 and b % 2 == 0 and a > b:
		return b
	elif a % 2 == 0 and b % 2 == 0 and b > a:
		return a
	elif a % 2 != 0 or b % 2 != 0 and a > b:
		return a
	elif a % 2 != 0 or b % 2 != 0 and b > a:
		return b


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text = 'scarry ssama'):
	rex = (text.split(' '))
	if rex[0][0] == rex[1][0]:
		return True
	else:
		return False

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
	if n1 + n2 == 20:
		return True
	if n1 == 20 or n2 == 20:
		return True
	else:
		return False
# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name='macdonald'):
	gird = name.replace(name[0], name[0].upper())
	bird = gird.replace(gird[3], gird[3].upper(), 1)
	return bird

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text='I am home'):
	array = text.split()[::-1]
	for i in array:
		blu_ray = " ".join(array)
		return blu_ray	

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
	if n + 90 == 100 or 100 - n == 10:
		return True
	elif n + 190 == 200 or 200 - n == 110:
		return True
	else:
		return False

# LEVEL 2 PROBLEMS
# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True
	return False	
	
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text='Hello'):
	array = ''
	for i in text:
		array += i.lower()*3
	return array

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
	if a + b + c <= 21:
		return a + b + c
	elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
		return sum([a,b,c]) - 10
	elif sum([a,b,c]) > 21:
		return print('BUST')

# I had to watch the video for the Summer of 69 solution :/
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
	
	total = 0
	add = True

	for num in arr:
		while add:
			if num!= 6:
				total =+ num
				break
			else:
				add = False
		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	return total	
