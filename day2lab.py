
# Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
def sum_to(n):
    result = 0
    for i in range(1,n+1):
        result+=i
    print(result)
    return result
sum_to(6)  # returns 21
sum_to(10) # returns 55







# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers.

def largest(list):
    print(max(list))
    return max(list)

largest([10, 4, 2, 231, 91, 54])  # returns 231
largest([1,2,3,4,0])  # returns 4






# Write a function named occurrences() that takes two string parameters and counts the number of occurrances of the second string inside the first string
def occurrences(string,substring):
    result = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            result += 1
    print(result)
    return result

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0



# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product.
def product(*args):
    result = 1
    for a in args:
        result *= a
    print(result)
    
product(4,3,2,5,10)
