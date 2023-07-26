area = float(input("Qual é a medida em metros quadrados para ser pintado: "))
litrosNecessario = area/3

latas = round(litrosNecessario/18)
valorLatas = round(latas * 80)

galoes = round(litrosNecessario/3.6)
valorGaloes = round(litrosNecessario * 25)

semSobras = round(latas/3.6)
valorSemSobras = round((semSobras *25) + valorLatas)

print("Apenas latas pagará", valorLatas , "reias por", latas, "litros \n"
      "Apenas galões pagará", valorGaloes , "reias por", galoes, "litros \n"
      "Com os 2, pagará", valorSemSobras , "por", latas, "litros de lata e", semSobras , "litros de galão")