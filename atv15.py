area = float (input("Qual é a media em metros quadrados para ser pintados: "))
litrosNecessario = area/3

latas = round(litrosNecessario/18)
valorLatas = round(latas * 80)

print("Você precisara de", latas , "e ira  pagar: R$", valorLatas)
