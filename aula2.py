
idade = 16
tem_carteira = True


pode_dirigir = idade >= 18 and tem_carteira
pode_entrar = idade >= 18 or tem_carteira
nao_menor = not (idade < 18)

print("Pode dirigir?", pode_dirigir)
print("Pode entrar?", pode_entrar)
print("Não é menor de idade?", nao_menor)


# Título: Verificador de Permissão de Viagem
# Descrição:
# Crie um programa em Python que determine se uma pessoa pode viajar com base em duas condições:

# Ter idade maior ou igual a 18 anos (idade) ou possuir autorização dos pais (tem_autorizacao).
# Use operadores lógicos para verificar se a pessoa pode viajar.
# Exiba uma mensagem informando se a viagem é permitida ou não.
# Teste o programa com diferentes valores para idade e tem_autorizacao (ex.: idade = 16, tem_autorizacao = True).

# Resultado 

