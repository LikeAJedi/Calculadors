
print('=====================================================Calculadora Fatorial===================================================================')

num = int(input('\nDigite um numero:'))

def factcalc(num):
    if num == 1:
        return 1
    else:
        return num * factcalc(num-1)

print('\nO resultado é:', factcalc(num))

