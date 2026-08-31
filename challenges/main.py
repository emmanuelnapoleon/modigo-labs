def multiplication_table(number, limit):
    # TODO: use a for loop to build a list of number * 1 through number * limit
    product = []

    for count in range(1,limit+1):
        product.append(number*count)
    return product

print(multiplication_table(1,4))