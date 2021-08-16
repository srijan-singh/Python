# sets is a data structure where we can perform mathemeatical function like union and intersection
# it contains unique elements

my_set = {3, 3, 4, 5, 6}
print(my_set) #will print only one 3

# To check whether an element is present in a set
print(3 in my_set)

# To print number of element present in set
print(len(my_set))

# To remove the element in the set
print(my_set.pop())

# To remove all the element in the set
print(my_set.clear())

# mathematical operaions
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

print(set_1 & set_2)  # intersection " & " and gate
print(set_1 | set_2)  # union " | " or gate
print(set_1 ^ set_2)  # symmeric difference " ^ " xor gate
print(set_1 <= set_2) # is set_1 subset of set_2
print(set_1 >= set_2) # is set_1 superset of set_2