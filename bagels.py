import random

NUM_DIGITS = 3 
MAX_GUESSES = 100

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Ты угадал!'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    print('''Начинается дедуктивная логическая игра.
Автор: Ай Свейгарт al@inventwithpython.com
Я имею в виду {}-значное число без повторяющихся цифр.
Попробуйте угадать, что это такое. Вот несколько подсказок:
    Когда я говорю:    Это означает:
    Pico               Одна цифра верна, но находится в неправильном положении.
    Fermi              Одна цифра верна и находится в правильном положении.
    Bagels             Ни одна цифра не является правильной.
Например, если секретное число было 248, а ваше предположение - 843, ключом к
разгадке будет Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('Я придумал номер.')
        print('У вас есть {} попыток, чтобы угадать его.'.format(MAX_GUESSES))

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('У тебя закончились попытки.')
                print('Ответ был {}.'.format(secretNum))
        
        print('Хочешь сыграть ещё раз? (Yes или No)')
        if not input('> ').lower().startswith('y'):
            break
    print('Спасибо за игру!')


if __name__ == '__main__':
    main()