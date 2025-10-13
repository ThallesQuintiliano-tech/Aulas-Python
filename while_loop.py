# ============================================================
# WHILE - Repetindo com Condição
# ============================================================

print("=" * 50)
print("WHILE - Loop Condicional")
print("=" * 50)

# WHILE: Repete enquanto a condição for verdadeira

def contar_ate_5():
    """Conta de 1 até 5 usando while"""
    contador = 1
    
    print("→ Contando de 1 a 5:")
    while contador <= 5:
        print(contador, end=" ")
        contador += 1
    print()

contar_ate_5()


def contagem_regressiva(numero):
    """Faz contagem regressiva"""
    print(f"\n→ Contagem regressiva de {numero}:")
    
    while numero > 0:
        print(numero, end=" ")
        numero -= 1
    print("🚀 FIM!")

contagem_regressiva(10)


def somar_ate_limite(limite):
    """Soma números até atingir um limite"""
    soma = 0
    numero = 1
    
    print(f"\n→ Somando números até passar de {limite}:")
    
    while soma < limite:
        print(f"  {soma} + {numero} = {soma + numero}")
        soma += numero
        numero += 1
    
    print(f"  Total final: {soma}")

somar_ate_limite(20)


def dobrar_ate_100(numero):
    """Dobra o número até passar de 100"""
    print(f"\n→ Dobrando {numero} até passar de 100:")
    
    while numero <= 100:
        print(f"  {numero}")
        numero *= 2
    
    print(f"  Passou de 100: {numero}")

dobrar_ate_100(5)


def contar_de_2_em_2():
    """Conta de 2 em 2 até 10"""
    contador = 0
    
    print("\n→ Contando de 2 em 2:")
    while contador <= 10:
        print(contador, end=" ")
        contador += 2
    print()

contar_de_2_em_2()


print("\n" + "=" * 50)
print("RESUMO - WHILE:")
print("=" * 50)
print("""
Sintaxe:
    while condição:
        # código a repetir
        # IMPORTANTE: alterar variável da condição!

Exemplo:
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

⚠️ CUIDADO: Sempre garanta que a condição vai 
            se tornar falsa para evitar loop infinito!

Use quando: Não sabe quantas repetições serão necessárias
""")
print("=" * 50)

