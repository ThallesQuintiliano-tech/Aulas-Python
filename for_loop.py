# ============================================================
# FOR - Repetindo com Listas e Sequências
# ============================================================

print("=" * 50)
print("FOR - Loop de Repetição")
print("=" * 50)

# FOR: Percorre cada item de uma lista ou sequência

def imprimir_nomes():
    """Imprime cada nome da lista"""
    nomes = ["Ana", "Bruno", "Carlos", "Diana"]
    
    print("→ Imprimindo nomes:")
    for nome in nomes:
        print(f"  Olá, {nome}!")

imprimir_nomes()


def contar_ate_10():
    """Conta de 1 até 10"""
    print("\n→ Contando de 1 a 10:")
    
    for numero in range(1, 11):
        print(numero, end=" ")
    print()

contar_ate_10()


def somar_lista(numeros):
    """Soma todos os números da lista"""
    soma = 0
    
    for numero in numeros:
        soma += numero
    
    print(f"\n→ Soma de {numeros} = {soma}")

somar_lista([1, 2, 3, 4, 5])
somar_lista([10, 20, 30])


def tabuada(numero):
    """Imprime a tabuada de um número"""
    print(f"\n→ Tabuada do {numero}:")
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"  {numero} x {i} = {resultado}")

tabuada(5)


def contar_frutas(frutas):
    """Conta quantas frutas existem"""
    total = 0
    
    print("\n→ Contando frutas:")
    for fruta in frutas:
        total += 1
        print(f"  {total}. {fruta}")
    
    print(f"\nTotal: {total} frutas")

contar_frutas(["Maçã", "Banana", "Laranja", "Uva"])


print("\n" + "=" * 50)
print("RESUMO - FOR:")
print("=" * 50)
print("""
Sintaxe:
    for item in sequência:
        # código a repetir

Exemplos:
    # Com lista
    for nome in ["Ana", "Bruno"]:
        print(nome)
    
    # Com range
    for i in range(5):
        print(i)  # 0, 1, 2, 3, 4

Use quando: Tem uma coleção para percorrer
""")
print("=" * 50)

