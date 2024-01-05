
# Aula 8 – Utilizando Módulos
import tudo
from tudo import algo

# biblioteca Math:
import math
math.ceil() # a redonda para cima
math.floor() # a redonda para baixo
math.trunc() # elimina numeros depois da virgula
math.pow() # potenciação
math.sqrt() # raiz quadrada
math.factorial()

# Aula 9 – Manipulando Texto
# Fatiamento:
frase = 'Curso em Video Python'
frase[9:13] # vai do 9 ao 12;
frase[9:21:2] # Pulando de 2 em 2;

# Análise:
len(frase) #Quantidade de Caracteres;
frase.count('o') #Contar uma quantidade de algo;
frase.count('o', 0,13) # Com fatiamento
frase.find('deo') #Indicar a posição encontrada
'curso' in frase

#Transformação:
frase.replace('Python', 'android') #Substituir
frase.upper() #Fica em Maiusculo
frase.lower() #Fica em Minusculo
frase.capitalize() #Só o primeiro fica em maiusculo
frase.title() #analisa a quantidade de palavras e deixa o inicio em maiusculo
frase.strip() # Remove espaços desnecessarios
frase.rstrip() #Lado direito
frase.lstrip() #Lado esquerdo

#Divisão:
frase.split()

#Junção
'-'.join(frase)

# Aula 10 – Condições (Parte 1)
if algo >= 7:
    print('2')
else:
    print('1')