# ============================================================
# COMBINANDO IF, FOR e WHILE
# ============================================================

print("=" * 50)
print("Combinando Estruturas de Controle")
print("=" * 50)

# Você pode combinar IF, FOR e WHILE para criar lógicas complexas

def separar_pares_impares(numeros):
    """Separa números pares e ímpares usando FOR + IF"""
    print("\n→ Separando pares e ímpares:")
    
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            print(f"  {numero} é PAR")
        else:
            impares.append(numero)
            print(f"  {numero} é ÍMPAR")
    
    print(f"\nPares: {pares}")
    print(f"Ímpares: {impares}")

separar_pares_impares([1, 2, 3, 4, 5, 6, 7, 8])


def contar_positivos_negativos(numeros):
    """Conta quantos números são positivos e negativos"""
    print("\n→ Contando positivos e negativos:")
    
    positivos = 0
    negativos = 0
    zeros = 0
    
    for numero in numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    
    print(f"  Positivos: {positivos}")
    print(f"  Negativos: {negativos}")
    print(f"  Zeros: {zeros}")

contar_positivos_negativos([5, -3, 0, 8, -1, 0, 7])


def buscar_nome(lista_nomes, nome_procurado):
    """Busca um nome na lista usando WHILE + IF"""
    print(f"\n→ Buscando '{nome_procurado}' na lista:")
    
    indice = 0
    encontrado = False
    
    while indice < len(lista_nomes) and not encontrado:
        if lista_nomes[indice] == nome_procurado:
            encontrado = True
            print(f"  ✓ Encontrado na posição {indice}!")
        indice += 1
    
    if not encontrado:
        print(f"  ✗ Não encontrado")

nomes = ["Ana", "Bruno", "Carlos", "Diana"]
buscar_nome(nomes, "Carlos")
buscar_nome(nomes, "Eduardo")


def imprimir_ate_negativo(numeros):
    """Imprime números até encontrar um negativo usando WHILE + IF"""
    print(f"\n→ Imprimindo até encontrar negativo:")
    print(f"  Lista: {numeros}")
    
    indice = 0
    
    print("  Números: ", end="")
    while indice < len(numeros):
        if numeros[indice] < 0:
            print(f"\n  ✗ Parou no número negativo: {numeros[indice]}")
            break
        print(numeros[indice], end=" ")
        indice += 1

imprimir_ate_negativo([5, 10, 15, -3, 20, 25])


def listar_aprovados(alunos_notas):
    """Lista alunos aprovados (nota >= 7) usando FOR + IF"""
    print("\n→ Listando alunos aprovados:")
    
    for aluno, nota in alunos_notas.items():
        if nota >= 7:
            print(f"  ✓ {aluno}: {nota} - APROVADO")
        else:
            print(f"  ✗ {aluno}: {nota} - REPROVADO")

alunos = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carlos": 9.0,
    "Diana": 5.5
}
listar_aprovados(alunos)


print("\n" + "=" * 50)
print("RESUMO - COMBINAÇÕES:")
print("=" * 50)
print("""
Você pode combinar as estruturas:

FOR + IF:
    for numero in lista:
        if numero > 0:
            print("Positivo")

WHILE + IF:
    while contador < 10:
        if contador % 2 == 0:
            print(contador)
        contador += 1

FOR + IF + ELSE:
    for item in lista:
        if condição:
            # faz algo
        else:
            # faz outra coisa

💡 Dica: Comece simples e vá adicionando complexidade!
""")
print("=" * 50)

