def sum_even_numbers(numbers):
    # TODO: return the sum of all even numbers in `numbers`
    addition = 0

    for even_num in numbers:
        if even_num % 2 == 0:
            addition = addition + even_num

    return addition
print(sum_even_numbers([2,4,6,8]))