# Receber um numero
# Receber um operador
# Receber um outro número
# Mostrar o resultado
resultado = 0.0
while resultado >= 0 or resultado <=0:
    print('-------Calculadora Python --------')
    numero1 = float(input('Insira o primeiro número: '))
    operador = input('Insira o Operador: ')
    numero2 = float(input('Insira o segundo número: '))
    if operador == '+':
        resultado = numero1 + numero2
        print(f'O resultado da soma é: {resultado}')
    elif operador == '-':
        resultado = numero1 - numero2
        print(f'O resultado da subtração é: {resultado}')
    elif operador == '*':
        resultado = numero1 * numero2
        print(f'O resultado da multiplicação é: {resultado}')
    elif operador == '/':
        resultado = numero1/numero2
        print(f'O resultado da divisão é: {resultado}')
    else:
        print('Você inseriu um operador inválido !')
    print('----------------------------')
        
        