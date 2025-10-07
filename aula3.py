
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