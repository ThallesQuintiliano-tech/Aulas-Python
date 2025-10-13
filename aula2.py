idade = 18
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira
pode_entrar = idade >= 18 or tem_carteira
nao_menor = not (idade < 18)

print("Pode dirigir?", pode_dirigir)
print("Pode entrar?", pode_entrar)
print("Não é menor de idade?", nao_menor)


