# Título: Verificador de Permissão de Viagem
# Descrição:
# Crie um programa em Python que determine se uma pessoa pode viajar com base em duas condições:

# Ter idade maior ou igual a 18 anos (idade) ou possuir autorização dos pais (tem_autorizacao).
# Use operadores lógicos para verificar se a pessoa pode viajar.
# Exiba uma mensagem informando se a viagem é permitida ou não.
# Teste o programa com diferentes valores para idade e tem_autorizacao (ex.: idade = 16, tem_autorizacao = True).

# Resultado 

idade = 16
tem_autorizacao = True


pode_viajar = (idade >= 18) or tem_autorizacao


print(f"Idade: {idade} anos, Autorização: {tem_autorizacao}")
print("Viagem PERMITIDA!" * pode_viajar + "Viagem NEGADA!" * (not pode_viajar))


# Como testar diferentes cenários:
# Menor sem autorização: idade = 16, tem_autorizacao = False
# Menor com autorização: idade = 16, tem_autorizacao = True
# Maior sem autorização: idade = 14, tem_autorizacao = False
# Maior com autorização: idade = 14, tem_autorizacao = True