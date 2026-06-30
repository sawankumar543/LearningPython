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


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict["year"] = 2018
# thisdict.update({"model": "red"})
# thisdict.pop("model")
# thisdict.popitem()
# thisdict.clear()
# del thisdict

# print(thisdict)
# for x in thisdict:
#     print(x,":",thisdict[x])

# for x in thisdict.values():
#   print(x)
# print("-------------next-----------")
# for x in thisdict.keys():
#   print(x)
# print("-------------next-----------")
# for y, x in thisdict.items():
#   print(y,x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "zaid":{
#     "age":18,
#     "collage":"technoindiau"
#   }
# }

# mydict= thisdict.copy()
# mydict2 = dict(thisdict)
# mydict3 = thisdict;
# print(mydict)
# print(thisdict["zaid"]["age"])


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004,
#     "qualities":{
#       "IQ":220,
#       "skill":"eating"
#     }
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007,
#     "qualities":{
#       "IQ":520,
#       "skill":"drinking"
#     }
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011,
#     "qualities":{
#       "IQ":320,
#       "skill":"food"
#     }
#   }
# }
# for x in myfamily:
#   for y in x:
#      print(y)

# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

# print(myfamily["child1"])

# for x in myfamily:
#     print(x,": qualities : IQ",myfamily[x]["qualities"]["IQ"])


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004,
#     "qualities":{
#       "IQ":220,
#       "skill":"eating"
#     }
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007,
#     "qualities":{
#       "IQ":520,
#       "skill":"drinking"
#     }
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011,
#     "qualities":{
#       "IQ":320,
#       "skill":"food"
#     }
#   }
# }


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()

# print(car)


# x = ('key1', 'key2', 'key3')

# y = ('1', '2', '3')

# thisdict = {}

# i=0
# for a in y:
#  thisdict[x[i]] = a
#  i+=1
 
# print(thisdict)

#mydict[x]=y

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model")
# print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


x = car.items()
print(x)