# List comprehension is a short hand method offered by python

# to print the range of number
under_10 = [x for x in range(10)]
print("in range 10: ", under_10)

# to print the square of number
sq_num = [x**2 for x in under_10]
print("square: ", sq_num)

# using if condition or logic
odd_num = [x for x in range(10) if x%2 != 0]
print("odd number: ",odd_num)

# get multiples of 10
mul_of_10 = [x*10 for x in under_10]
print("multiple of 10: ", mul_of_10)

# **get all numeric data from the string**
random_string = "I'm 21 , my girl is 19 and soon we are going to be buy an house together worth 100000"
num = [x for x in random_string.split(" ") if x.isnumeric()]
print(num)

