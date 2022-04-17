def fib(n, my_dict={}):
    if n in my_dict:   
        return my_dict[n]
    if n<=2: 
        return 1
    my_dict[n] = fib(n-1, my_dict) + fib(n-2, my_dict)
    return my_dict[n]

print(fib(46))

