peso = float(input('Qual seu peso atual (Kg) ?: '))
altura = float(input('Qual sua altura (M) ?: '))

imc = peso / (altura * altura)


linha_1 = f'Imc: {imc:.2f}!'
print(linha_1)
print(15*'-')

if imc < 18.5:
    print('Classificação:  MAGREZA!')
    print(15*'-')

elif imc < 24.9:
    print('Classificação: PESO NORMAL!')
    print(15*'-')

elif imc < 29.9:
    print('Classificação:  SOBREPESO!')
    print(15*'-')

elif imc < 34.9:
    print('Classificação:  OBESIDADE GRAU 1!')
    print(15*'-')

elif imc < 39.9:
    print('Classificação:  OBESIDADE GRAU 2!')
    print(15*'-')

elif imc > 40:
    print('Classificação:  OBESIDADE GRAU 3!')
print(15*'-')
