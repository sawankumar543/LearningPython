# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict = {
#     "brand":2,
#     "model":3,
#     "model":3,
#     "year":5,
#     "year":3
# }
# print(thisdict)
# print(type(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for index, (key, value) in enumerate(thisdict.items()):
#     print(index, key, value)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict["year"] = 2018
thisdict.update({"model": "red"})

print(thisdict)