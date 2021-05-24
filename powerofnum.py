def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result

def display(base, exponent):
    result = power(base, exponent)
    print(base, " to the power ",exponent," is ",result, "\n")

if __name__ == "__main__":
    base = int(input("Input base: "))
    exponent = int(input("Input Power: "))
    display(base, exponent)