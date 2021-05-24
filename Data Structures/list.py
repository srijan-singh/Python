# Declairing the list a data structure which is mutable
# Here we can save all primitive data types
my_list = [1, "two", 3.6234, True]
#Printing the list
print(my_list)

# To copy the list
new_list = my_list.copy()
#Printing the list
print(my_list)

#To add element in list
my_list.append("Srijanverse")
my_list.insert(2, 45667)
#Printing the updated list 
print(my_list)

#To remove the element in list 
my_list.remove("Srijanverse")
my_list.pop(1)
#Printing the updated list 
print(my_list)

#To reverse the list
my_list.reverse()
#Printing the updated list 
print(my_list)

#To sort the list
my_list.sort()
#Printing the updated list 
print(my_list)

#To print a particular element from index

# First element
print(my_list[0])
# Last element
print(my_list[-1])
# To print individual
print(my_list[3])
# To print ranging form
print(my_list[:2])
print(my_list[2:])

# To print the minimum elemnt
print(min(my_list))

# To print the maximum elelment
print(max(my_list))

# To print the sum of elements in the list
print(sum(my_list)) 

# To print the list in sorted order
print(sorted(my_list))

# To print the number of count in list
print(my_list.count(1))

# To print the index of the element
print(my_list.index(1))

# To assign value to variables
a, b, c, d = my_list
print(a, b, c, d)

#To clear the elements of list
my_list.clear()
#Printing the updated list 
print(my_list)

