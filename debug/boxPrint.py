
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be 1 char')
    if width <= 2:
        raise Exception('width over 2 length')
    if height <= 2:
        raise Exception('height over 2 length')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)

    print(symbol * width)

for sym, w, h in(('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('Raise error:' + str(err))

