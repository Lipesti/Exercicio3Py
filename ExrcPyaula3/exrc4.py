#Exercicio 4 

valorPrestacao = float(input('Digite o valor da prestação R$: '))
multa = int(input('Informe a porcentagem da multa aplicada: '))
qntdDias = int(input('Informe os dias de atraso: '))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qntdDias)

print(f'O valor da prestação com a multa é de:\n {prestacao}')