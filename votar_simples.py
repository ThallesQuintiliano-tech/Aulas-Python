# Verificação de Voto - Exemplo Simples

# F-STRING (f""): Insere variáveis no texto usando {}
# Exemplo: print(f"Olá {nome}") em vez de print("Olá " + nome)

# Entrada do nome e idade pelo usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verificação simples
if idade >= 16:
    print(f"{nome}, você PODE VOTAR")
else:
    print(f"{nome}, você NÃO PODE VOTAR")
