# 1)Write a python program to find the longest word of txt file.

with open("text.txt") as file:
	word = file.read().split()
	long_word = len(max(word, key = len))
	print(long_word)

#2)Write a Python program to count the frequency of words in a txt file.

with open("text.txt") as file:
	a = file.read().split()
	b = {i: a.count(i) for i in a}
	print(b)

#3) Write a Python program to read a random line from a file.

import random
with open("text.txt", "r") as f:
	a = f.readlines()
	b = random.choice(a)
	print(b)

# 4)You have two list convert it in dictionary and add
# in (mydict.txt) and show result:
# for example: input :
# first = [‘Ani’, ‘Jessy’, ‘Ben’]
# second = [1,2,3]
# my_dict = {1 : “Ani” , 2: “Jessy”, 3: “Ben”}


lst1 = [1,2,3]
lst2 = ["Ani", "Jessy", "Ben"]
# dic = dict(zip(lst1,lst2))
with open("text.txt", "w+") as f:
	lst1 = [1,2,3]
	lst2 = ["Ani", "Jessy", "Ben"]
	dic = dict(zip(lst1,lst2))
	f.write(str(dic))
	print(dic)
	

#5) Write a Python program to convert Python object to JSON data.

import json
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data,type(j_data))


#6)Write a Python program to convert JSON data to Python object. 


import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print(type(python_obj), python_obj) 








