import time

def calc_prod():

    product = 1
    for i in range (1, 100000):
        product = product * i
    return product

start_time = time.time()

prod = calc_prod()

end_time = time.time()

print('calcuration digit is {}'.format(len(str(prod))))
print('calcuration time is {}'.format(end_time - start_time))
