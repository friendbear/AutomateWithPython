import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('starting program...')

def factorial(n):
    logging.debug('factorial({})start'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = {}, total = {}'.format(i, total))
    logging.debug('factorial({})end'.format(n))
    return total

print(factorial(5))

logging.debug('end program')
