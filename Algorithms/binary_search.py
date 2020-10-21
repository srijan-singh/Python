def binary_search(my_list, high, low, mid, x):
    # If element is present
    if x == my_list[mid]:
        print("Element number:", mid+1, "\nFound at index:", mid)
    # If element is less than middle element
    elif x > my_list[mid]:
        binary_search(my_list, high, mid, (high+mid)//2, x)
    # If element is larger than middle element
    elif x < my_list[mid]:
        binary_search(my_list, mid, low, (low+mid)//2, x)
    # If element is not present in the element
    else:
        print("Element is not present in the list!")


# Creating a list
my_list = [12, 23, 7, 8, 4, 256, 89, 2, 45]
# Sorting the list
my_list.sort()
print(my_list)
# Declairing high, low and mid
high = len(my_list) + 1
low = 0
mid = (high + low)//2
# Element to be found
x = 11
print(x)

binary_search(my_list, high, low, mid, x)

