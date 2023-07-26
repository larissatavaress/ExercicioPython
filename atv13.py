peso = float(input("Digite o peso do peixe:"))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

print("Peso: %.2f kg. Excesso: %.2f kg. \nMulta: R$ %.2f" %(peso, excesso, multa))