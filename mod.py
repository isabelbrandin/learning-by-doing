def even_or_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

def evens(numbers):
    res = []
    for i in numbers:
        if i % 2 == 0:
            res.append(i)
    return res

a = [1, 2, 3, 6, 8, 9, 11]

print(evens(a))

# def is_even(n):
    #return n % 2 == 0

# def evens(numbers):
    #result = []
    #for n in numbers:
        #if is_even(n):
            #result.append(n)