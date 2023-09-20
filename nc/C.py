import random

print("Hi")
print("Угадай загаданное число")
guesses_made = 0
number = random.randint(1, 20)
print('Отлично, {0}, я загадал число между 1 и 20. Сможешь угадать?')
while guesses_made < 3:
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess < number:
        print('Твое число меньше того, что я загадал.')
    if guess > number:
        print('Твое число больше загаданного мной.')
    if guess == number:
        break