import random
m = random.randint(1,100)

print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if n.isalnum():
        if 0 < int(n) < 101:
            return True
        else:
            return False
    else:
        return False
print('Введите число от 1 до 100 ')
while True:
    num = input()
    if is_valid(num):
        n = int(num)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if n == m:
        print('Вы угадали, поздравляем!')
        break
    elif n < m:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif n > m:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')