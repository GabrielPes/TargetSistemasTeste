"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência."""

print('O valor faz parte da sequência de Fibonacci?')

while True:
    try:
        valor = int(input('Valor: '))
    except:
        print('Digite um número inteiro')
    else:
        break

n1 = 0
n2 = 1
lista_sequencia = [n1, n2]
while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    lista_sequencia.append(n3)
    if n3 == valor:
        print(f'{valor} faz parte da sequencia Fibonacci')
        break
    elif n3 > valor:
        print(f'{valor} NÃO faz parte da sequência Finonacci')
        break

while True:
    try:
        seq = int(input(' \nMostrar sequência gerada, até o valor informado? \n[0] Sim\n[1] Não\n'))
    except:
        print('Digite uma opção válida')
    else:
        if seq == 0:
            print(lista_sequencia)
            break
        elif seq == 1:
            break
        else:
            print('Digite uma opção válida')
            continue
