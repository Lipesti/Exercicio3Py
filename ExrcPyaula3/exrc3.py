# Exercicio 3

print('Convertendo idade em dias ')
anos = int(input('Digite a quantidade de anos de vida'))
dias = int(input('Digite a quantidade de dias de vida'))
meses = int(input('Digite a quantidade de meses de vida'))

dias = dias + anos*365 + meses*30

print('Parabéns você já viveu',dias,'dias')