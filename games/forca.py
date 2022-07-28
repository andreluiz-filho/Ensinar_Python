

palavra = "celular"
palavra_oculta = []


for i in range(len(palavra)):
	palavra_oculta.append("*")



while True:
	print()
	print("----------------------Jogo da Forca----------------------")
	print()
	print("", palavra_oculta)
	print()
	print("---------------------------------------------------------")

	tentativa = input("Escola a Letra: ")

	ind = 0
	for p in palavra:

		if tentativa == p:
			palavra_oculta[ind] = p

		ind += 1


	print()

	print("\x1b[2J\x1b[1;1H", end="")

