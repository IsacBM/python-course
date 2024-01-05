# IsacBM - 2K23
import math
angulo = int(input('Digite o valor do ângulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem o Tangente de {:.2f}'.format(angulo, tang))
