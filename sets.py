# myset = {"apple", "banana", "cherry", "apple", 2, 0, False}
# #  unordered, unchangeable*, and unindexed.
# print(len(myset))

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# set1 = {"abc", 34, True, 40, "male"}
# print(type(set1))


# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)


# thisset = {"apple", "banana", "cherry", True}

# # for x in thisset:
# #     print(x)]


# print("banana" not in thisset)
# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = ["pineapple", "mango", "papaya"]

# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "cherry"}

# # thisset.remove("banana")
# # thisset.discard("banana")
# # thisset.pop()
# # thisset.clear()
# del thisset

# print(thisset)


# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# set3 = set1.union(set2, set3, set4)

# print(set3)


# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

# set1 = {"a", "b" , "c", "d"}
# set2 = {1, 2, 3, "d"}

# set1.update(set2)
# print(set1)

# Intersection
# Join set1 and set2, but keep only the duplicates:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# set4 = set1 & set2

# print(set3)
# print(set4)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)


# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)