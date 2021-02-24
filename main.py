import random

print('Guess the Random No. between 1 - 20')

guessNo = int(input('Guess: '))
randNo = random.randint(1,20)
print(randNo)
for x in range(5):
    if guessNo != randNo:
        print('Wrong!')
        if guessNo > randNo:
            print('Hint :',guessNo,'> ?')
        else:
            print('Hint :',guessNo,'< ?')
        guessNo = int(input('Guess: '))
        if x == 4:
            print('Wrong!')
            print('You Lose!')
        if guessNo == randNo:
            print('Correct!')
            print('You Win!')
