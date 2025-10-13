# ============================================================
# AULA 05 - Estruturas de Controle em Python (VERSÃO SIMPLES)
# ============================================================

print("=" * 50)
print("1. IF e ELSE - Tomando Decisões")
print("=" * 50)

# IF/ELSE: Executa código diferente dependendo da condição
def verificar_numero(numero):
    """Verifica se um número é positivo ou negativo"""
    if numero > 0:
        print(f"{numero} é POSITIVO")
    else:
        print(f"{numero} é NEGATIVO ou ZERO")

verificar_numero(5)
verificar_numero(-3)
verificar_numero(0)


def pode_votar(idade):
    """Verifica se pode votar (16+ anos)"""
    if idade >= 16:
        print(f"Com {idade} anos: PODE VOTAR ✓")
    else:
        print(f"Com {idade} anos: NÃO PODE VOTAR ✗")

print()
pode_votar(18)
pode_votar(14)


print("\n" + "=" * 50)
print("2. FOR - Repetindo com Lista/Range")
print("=" * 50)

# FOR: Percorre cada item de uma lista ou sequência
def imprimir_nomes():
    """Imprime cada nome da lista"""
    nomes = ["Ana", "Bruno", "Carlos"]
    
    for nome in nomes:
        print(f"Olá, {nome}!")

imprimir_nomes()


def contar_10():
    """Conta de 1 até 10"""
    print("\nContando de 1 a 10:")
    
    for numero in range(1, 11):
        print(numero, end=" ")
    print()

contar_10()


def somar_lista(numeros):
    """Soma todos os números da lista"""
    soma = 0
    
    for numero in numeros:
        soma += numero
    
    print(f"\nSoma de {numeros} = {soma}")

somar_lista([1, 2, 3, 4, 5])


print("\n" + "=" * 50)
print("3. WHILE - Repetindo com Condição")
print("=" * 50)

# WHILE: Repete enquanto a condição for verdadeira
def contar_ate_5():
    """Conta de 1 até 5 usando while"""
    contador = 1
    
    print("Contando com WHILE:")
    while contador <= 5:
        print(contador, end=" ")
        contador += 1
    print()

contar_ate_5()


def diminuir_de_10():
    """Diminui de 10 até 1"""
    numero = 10
    
    print("\nContagem regressiva:")
    while numero > 0:
        print(numero, end=" ")
        numero -= 1
    print("FIM!")

diminuir_de_10()


print("\n" + "=" * 50)
print("4. Combinando IF + FOR")
print("=" * 50)

def separar_pares_impares():
    """Separa números pares e ímpares"""
    numeros = [1, 2, 3, 4, 5, 6]
    
    print("Analisando números:")
    for numero in numeros:
        if numero % 2 == 0:
            print(f"{numero} é PAR")
        else:
            print(f"{numero} é ÍMPAR")

separar_pares_impares()


print("\n" + "=" * 50)
print("RESUMO RÁPIDO:")
print("=" * 50)
print("""
IF/ELSE:  Toma decisões
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

FOR:      Percorre listas/sequências
    for nome in ["Ana", "Bruno"]:
        print(nome)

WHILE:    Repete enquanto condição for True
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
""")
print("=" * 50)