def get_factorial(num):
    factorial = 1
    for i in range(1,num + 1):
       factorial = factorial*i
    return factorial

def sum_odd_numbers(num):
    counter = 0
    odd_sum = 1
    result = 0
    if num%2 == 1:
        odd_counter = (num-1)/2 + 1
    elif num%2 == 0:
        odd_counter = num/2
    while counter < int(odd_counter):
        counter += 1
        result += odd_sum
        odd_sum += 2
    return result

