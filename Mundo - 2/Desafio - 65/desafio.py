# IsacBM - 2K24
seq = int(input('Digite a sequência: '))
i = 0
print('0', end=(' -> '))

while i <= seq:
    anti = 0
    suss = 1
    
    soma = anti + suss
    
    print(soma, end=(' -> '))
    
    anti = suss
    suss = soma
    
    i += 1