num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print('A soma é: {}. \nO produto é: {}.\nA divisão é: {:.3n}'.format(s,m,d))
print('Divisão inteira é: {}, e a potência é: {}'.format(di, e))
