# mytuple = ("apple",)
# fruits = ['apple']
# A tuple is a collection which is ordered and unchangeable.

# print(len(mytuple))
# print(type(mytuple))

# print(len(fruits))
# print(type(fruits))

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)


# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-2])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
# print(thistuple[:5])
# print(thistuple[4:])
# print(thistuple[-4:-1])


# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("kiwi")
# x = tuple(y)

# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# fruits = ("apple", "banana", "cherry", "strawberry", "jamun")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)



# thistuple = ("apple", "banana", "cherry")
# for x in range(len(thistuple)):
#   print(thistuple[x])

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)


# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = ("apple", "banana", "cherry ","apple")
x = thistuple.count('a')
y = thistuple.index("apple")
print(y)