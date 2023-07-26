arquivo = float(input("Tamanho do arquivoem MB: "))
velocidadeSegundos = float(input("Velocidade da sua internet em Mbps: "))

download = (arquivo / velocidadeSegundos)/60

print("Irá baixar o arquivo em", download, "minutos")