# ============================================================
# IF e ELSE - Tomando Decisões
# ============================================================

print("=" * 50)
print("IF e ELSE - Estrutura Condicional")
print("=" * 50)

# IF/ELSE: Executa código diferente dependendo da condição

def verificar_numero(numero):
    """Verifica se um número é positivo ou negativo"""
    if numero > 0:
        print(f"{numero} é POSITIVO")
    else:
        print(f"{numero} é NEGATIVO ou ZERO")

print("\n→ Testando números:")
verificar_numero(5)
verificar_numero(-3)
verificar_numero(0)


def pode_votar(idade):
    """Verifica se pode votar (16+ anos)"""
    if idade >= 16:
        print(f"Com {idade} anos: PODE VOTAR ✓")
    else:
        print(f"Com {idade} anos: NÃO PODE VOTAR ✗")

print("\n→ Verificando idade para votar:")
pode_votar(18)
pode_votar(14)


def verificar_nota(nota):
    """Classifica a nota do aluno"""
    if nota >= 7:
        print(f"Nota {nota}: APROVADO ✓")
    else:
        print(f"Nota {nota}: REPROVADO ✗")

print("\n→ Verificando notas:")
verificar_nota(8.5)
verificar_nota(5.0)


def desconto_produto(preco, tem_cupom):
    """Aplica desconto se tiver cupom"""
    if tem_cupom:
        preco_final = preco * 0.9  # 10% de desconto
        print(f"Preço: R${preco:.2f} → Com desconto: R${preco_final:.2f}")
    else:
        print(f"Preço: R${preco:.2f} (sem desconto)")

print("\n→ Calculando preços:")
desconto_produto(100, True)
desconto_produto(100, False)


print("\n" + "=" * 50)
print("RESUMO - IF/ELSE:")
print("=" * 50)
print("""
Sintaxe:
    if condição:
        # código se verdadeiro
    else:
        # código se falso

Exemplo:
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

Use quando: Precisa tomar decisões no código
""")
print("=" * 50)

