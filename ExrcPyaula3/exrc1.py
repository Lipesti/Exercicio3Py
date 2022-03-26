#Exercicio 1 
#Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os
#valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão:
#volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print('Calculando o volume de uma piramide.')

h = float(input('Digite a altura da Piramide: '))
Bmenor = float(input('Digite a base menor da Piramide: '))
Bmaior = float(input('Digite a base maior da Piramide: '))

volume = h/3*(Bmaior**2 + Bmenor**2 +(Bmaior**2 * Bmenor**2)**0.5)

print(f'O volume da Piramide é: {volume:.2f} ')