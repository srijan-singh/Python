# Dictionaries are data structures which have key and value pair
# aka Assocoative array and hashmap
# unordered

my_dict = {'pork':25.3, 'beef':33.8, "chicken":22.7}
print(my_dict)

x = dict([("ram", 1), ("krishna", 1600)])
print(x)

# where key is like index here it can be more than integers
another_dict = dict(aloo=16, pyaaz=80, gobhi=30)
print(another_dict)

# acessing value in dict

# to print the keys
print(another_dict.keys())

# to print the values
print(another_dict.values())

# to print the item
print(another_dict.items())

# to check the item
print("aloo" in another_dict) #True
print("panner" in another_dict) #False

# to iterate in dictionary

for i in another_dict:
    print(i, another_dict[i])