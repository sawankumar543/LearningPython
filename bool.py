# print(3+2)
# print(3-2)
# print(3*2)
# print(10/2) # 5
# print(10%2) # 0
# print(5**2) #5*5
# print(5**3) #5*5*5

# print(15/2)
# print(15//2)
# #the floor division // rounds the result down to the nearest whole number


# x = 5
# x += 10 #15
# x -= 2  #13
# x *= 2  #26
# x /= 3
# x = 15
# x //= 7

# x = 12
# x = x & 7

# print(x)  

# 1 1 0 0  (12 ka binary)
# & 0 1 1 1  (7 ka binary)
# ----------
#   0 1 0 0  (result ka binary)

# x = 5

# x **= 3

# print(x)

# x = 5

# x ^= 3

# # print(x)
# x = 3
# print(x)

# print(x := 3)


# num = 6

# x = "WEEKEND!" if num > 5 else "Workday"

# print(x)

# num = 6

# x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

# print(x)


# x = 23
# y = 34

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# x = 5

# print(1 < x < 10)

# print(1 < x and x < 10)

# x = 5

# print(x > 0 and x < 10)
# print(x < 5 or x > 10)
# print(not(x > 3 and x < 10))


# is 
# is not

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z) true
# print(x is y) false
# print(x == y) true

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal


# x = [1, 2, 3]
# y = [1, 2, 3]
# z = y
# print(y is z)
# print(x == y)
# print(x is y)



# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object


# fruits = ["apple", "banana", "cherry"]

# print("banana" in fruits)


# fruits = ["apple", "banana", "cherry"]

# print("pineapple" not in fruits)


# text = "Hello World"

# print("H" in text)
# print("hello" in text)
# print("z" not in text)

# print((6 + 3) - (6 + 3))

# print(100 + 5 * 3)

# print(5 + 4 - 7 + 3)


# Python Lists


# myList = ["apple", "banana", "cherry", "cherry"]

# print(len(myList))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# list1 = ["abc", 34, True, 40, "male"]


# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# a = [4,1,2,4,3,4] # list
# d = (23,23,543) # tuple
# c = {1,3,2,3} # set
# e = {
#     "name": "sawan",
#     "age": 10
# } # dict

# a.remove()
# print(a)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])
# print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])
# print(len(thislist))

# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist = ["apple", "banana", "cherry"]

# thislist.insert(2, "watermelon")
# thislist.append("orange") # end me append karega

# tropical = ["mango", "pineapple", "papaya", "apple"]

# thislist.extend(tropical)
# thislist.remove("banana")
# thislist.pop()
# del thislist[0]
# thislist.clear()
# del thislist
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
# x = range(6, 12)
# for n in x:
#   print(n)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i],": ",i)


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1 # increment

# Looping Using List Comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# newlist = [x for x in fruits if "a" in x or "h" in x]

# for x in fruits:
#   if "a" in x or 'h' in x:
#     newlist.append(x)

# [print(x) for x in newlist]

# thislist.sort(reverse=True)
# print(thislist)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)

# The function will return a number that will be used to sort the list (the lowest number first):

# doubt
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# myfunc(100) → abs(100 - 50) = abs(50) → 50
# myfunc(50) → abs(50 - 50) = abs(0) → 0
# myfunc(65) → abs(65 - 50) = abs(15) → 15
# myfunc(82) → abs(82 - 50) = abs(32) → 32
# myfunc(23) → abs(23 - 50) = abs(-27) → 27

# असली नंबर (n) फ़ंक्शन का परिणाम (50 से दूरी) सॉर्टिंग का क्रम
# 50            0                        1st (सबसे छोटा)
# 65            15                       2nd
# 23             27                      3rd
# 82             32                      4th
# 100            50                      5th 


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# list1 = ["a", "b", "c"]

# list2 = list1
# list2[0] = "sawan"

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list1)
# print(list1)

l1 = [1,2,3,4]

# l1.append(22)
# l1.clear()
# print(l1.count(3))
# print(l1.index(4))
# l1.insert(2, "orange")
l1.pop()

print(l1)

# fruits = ['apple', 'banana', 'cherry']

# fruits.remove("banana")
# print(fruits)