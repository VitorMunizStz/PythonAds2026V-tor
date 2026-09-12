nome = "Vitinho"
idade = 19
altura = 1.60
aprovado = True

print("Seja bem-vindo ao Vitinho parque!")

if nome == "Vitinho":
    print("Olá, Vitinho!")
else:
    print("Olá, visitante!")

#str significa string
print(
    f"{nome} tem {idade} anos, "
    f"{'é maior de idade' if idade >= 18 else 'é menor de idade'}, "
    f"mede {altura}m ({'é alto' if altura >= 1.70 else 'não é alto'}), e "
    f"{'está aprovado' if aprovado else 'não está aprovado'}"
)