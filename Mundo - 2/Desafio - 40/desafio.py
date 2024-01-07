# IsacBM - 2K23
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print('Você foi aprovado!')
elif media >= 5.0 and media <= 6.9:
    print('Você está de recuperação!')
else:
    print('Você foi Reprovado. :(')
