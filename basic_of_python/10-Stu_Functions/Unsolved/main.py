# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(number):
    length= float(len(number))
    total=0.0
    for num in number:
        total+=num
    print(total/length)

# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
