equipamentos = []

for i in range(3):
    equipamento = input("Insira o nome do equipamento: ")
    equipamentos.append(equipamento)

print("Lista de equipamentos:")
for equipamento in equipamentos:
    print("- " + equipamento)