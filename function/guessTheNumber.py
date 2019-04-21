# 数当てゲーム

import random

secret_number = random.randint(1, 20)

print('数当てゲーム チャンスは6回 1から20の整数を入力してください。')

for guesses_taken in range(1, 7):
    print('Please Input number.')
    guess = int(input())

    if guess < secret_number:
        print('小さいです。')
    elif guess > secret_number:
        print('大きいです。')
    else:
        break

if guess == secret_number:
    print('当たり！' + str(guesses_taken) + '回で当てました。')
else:
    print('残念。正解は' + str(guesses_taken) + 'でした。')
