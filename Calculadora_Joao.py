import math

def soma(n1, n2):
    r = n1 + n2
    return r

def subtração(n1, n2):
    r = n1 - n2
    return r

def multiplicação(n1, n2):
    r = n1* n2
    return r

def divisão(n1, n2):
    if n1 == 0 or n2 == 0:
        return "Erro: Divisão por zero!"
    else:
        return n1 / n2

def potencia(n1, n2):
    r = n1 ** n2
    return r

def porcentagem(valor, percentual):
    r = (valor * percentual) / 100
    return r

def raiz_quadrada(numero):
    if numero < 0:
        return None
    return math.sqrt(numero)

while True:
    print('-=-' * 16)
    print(f'Calculadora do João V1.0'.center(44))
    print('-=-' * 16)
    print(f'''[1] Operações Básicas
[2] Operações Avançadas
[3] Tabuada
[4] Sair''')
    print('-=-' * 16)

    opção = int(input(f'Escolha sua Opção: '))

    if opção not in [1, 2, 3, 4]:
        print('-=-' * 16)
        print("Opção inválida. Tente novamente!")
        continue

    if opção == 1:
        print(f'''[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão''')
        print('-=-' * 16)

        opc = int(input(f'Escolha sua Opção: '))

        if opc not in [1, 2, 3, 4]:
            print('-=-' * 16)
            print("Opção inválida. Tente novamente!")
            continue

        if opc == 1:
            n1 = float(input(f'Digite um número: '))
            n2 = float(input(f'Digite um número: '))
            print(f'{n1} + {n2} = {soma(n1, n2):.2f}')

        elif opc == 2:
            n1 = float(input(f'Digite um número: '))
            n2 = float(input(f'Digite um número: '))
            print(f'{n1} - {n2} = {subtração(n1, n2):.2f}')

        elif opc == 3:
            n1 = float(input(f'Digite um número: '))
            n2 = float(input(f'Digite um número: '))
            print(f'{n1} x {n2} = {multiplicação(n1, n2):.2f}')

        elif opc == 4:
            n1 = float(input(f'Digite um número: '))
            n2 = float(input(f'Digite um número: '))
            print(f'{n1} ÷ {n2} = {divisão(n1, n2):.2f}')

    if opção == 2:
        print(f'''[1] Potência
[2] Porcentagem
[3] Raiz Quadrada
''')
        print('-=-' * 16)

        opc = int(input(f'Escolha sua Opção: '))

        if opc not in [1, 2, 3]:
            print('-=-' * 16)
            print("Opção inválida. Tente novamente!")
            continue

        if opc == 1:
            n1 = float(input(f'Digite um número: '))
            n2 = float(input(f'Digite um número: '))
            print(f'{n1} elevado a {n2} = {potencia(n1, n2):.2f}')

        if opc == 2:
            print(f'''[1] Porcentagem normal
[2] Desconto de produto
[3] Reajuste Salarial''')
            print('-=-' * 16)

            opc = int(input(f'Escolha uma Opção:'))

            if opc not in [1, 2, 3]:
                print('-=-' * 16)
                print("Opção inválida. Tente novamente!")
                continue

            if opc == 1:
                valor = float(input(f'Digite um número: '))
                percentual = float(input(f'Qual o percentual desse número? '))
                print(f'{percentual}% de {valor} é = {porcentagem(valor, percentual):.2f}')

            if opc == 2:
                p = float(input(f'Qual o preço do produto: R$'))
                percentual = int(input(f'Quantos %: '))
                desconto = (p * percentual / 100)
                preço = p - desconto
                print(f'O produto que custava R${p}, com desconto de {percentual}% fica por R${preço:.2f}')

            if opc == 3:
                sal = float(input(f'Qual é o seu salário ? R$'))
                percentual = int(input(f'Quantos % vai subir? '))
                aumento = (sal * percentual / 100)
                novo_salario = sal + aumento
                print(f'O salário de R${sal:.2f}, com {percentual}% de aumento, será de R${novo_salario:.2f}')

        if opc == 3:
            numero = float(input("Digite um número para calcular a raiz quadrada: "))
            resultado = raiz_quadrada(numero)
            if resultado is None:
                print("Não é possível calcular a raiz quadrada de um número negativo.")
            else:
                print(f"A raiz quadrada de {numero} é {resultado:.1f}")

    if opção == 3:
            print('-=-' * 16)
            valor = int(input(f'Quer ver a tabuada de qual número?  '))
            for n in range(1, 11):
                print(f'{valor} x {n:.0f} = {valor * n}')

    if opção == 4:
            print('-=-' * 16)
            print(f'''Espero que tenha gostado da Calculadora!!!
            
Créditos: João Arevalo Acerbi''')
            break
