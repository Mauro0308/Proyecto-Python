#MATRIZ

n = [[0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0,0,0,0,
	 0,0,0,0,0,0,0,0,0]]

#Arreglos

clientes = []
cliente = []


fila = 0
columna = 0

#VARIABLES
cont = 0
ta1 = 0 #Tipo de asiento contador
ta2 = 0
ta3 = 0
buscar_rut = 0
op = ""
cant = ""
opc = ""
compra_id = 0
rut = ""
letra = ""
numero = ""
pack = ""
cont_pack_comun = 0
cont_pack_adicional = 0
cont_no_reclinable = 0
mta = 0
fila_n = 0
enumerador = 0
buscar = ""
#FUNCIONES

def ubicacionesavion():
		print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
		print("║   [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33] ║")
		print("║ F",n[0],"║")
		print("║ E",n[1],"║")
		print("║ D",n[2],"║")
		print("║ C",n[3],"║")
		print("║ B",n[4],"║")
		print("║ A",n[5],"║")
		print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝")


print("********************************")
print("BIENVENIDO A AEROLINEAS FLASH")
print("********************************")
print("")
print("Por favor Elija una opcion: ")
print("")
while opc != "s":
	print("1) Comprar pasajes")
	print("2) Mostrar ubicaciones disponibles")
	print("3) Ver listado de pasajeros")
	print("4) Buscar pasajero")
	print("5) Reasignar asiento")
	print("6) Mostrar ganancias totales")
	print("S) Salir")
	opc = input()

# Comprar pasajes ------------------------------------------------------------------------------------
	if opc == "1":
		print("Digite la cantidad de asientos que desea comprar: ")
		cant = input()
		while cant.isdigit() == False:
			print("opcion invalida, vuelva a ingresar nuevamente")
			cant = input()
		cantnu = int(cant)
		while cantnu > 3:
			print("opcion invalida")
			print("El maximo de asientos que se pueden comprar es de 3. ")
			print("")
			print("Por favor intente nuevamente.")
			cant = input()
			while cant.isdigit() == False:
				print("opcion invalida")
				cant = input()
			cantnu = int(cant)

		enumerador = 0

		while enumerador < cantnu:
			compra_id += 1
			print("Por favor ingrese su rut para el asiento Nª",enumerador+1)
			rut = input()
			while len(rut) != 8:
				print("opcion invalida")
				print("Debe ingresar un rut de 8 digitos")
				rut = input()
			while rut.isdigit() == False:
				print("opcion invalida")
				print("Por favor intente nuevamente.")
				rut = input()

			print("Ingrese su asiento",enumerador,"rut",rut)
			print("")
			print("1) Asiento comun: $60.000 mil pesos")
			print("2) Espacio adicional para las piernas: $80.000 mil pesos")
			print("3) Asiento NO reclinable: $50.000 mil pesos")
			pack = input()
			while pack.isdigit() == False:
				print("opcion invalida")
				print("Por favor intente nuevamente.")
				pack = input()
			pack_numero = int(pack)

			
			while mta == 0:

				if pack_numero == 1 or pack_numero == 2 or pack_numero == 3:

					if pack_numero == 1:
						pack_comun = 60000
						cont_pack_comun += 1
						enumerador += 1
						break
					elif pack_numero == 2:
						pack_adicional = 80000
						cont_pack_adicional +=1
						enumerador += 1
						break
					elif pack_numero == 3:
						pack_no_reclinable = 50000
						cont_no_reclinable +=1
						enumerador += 1
						break
					

				else:
					print("Debe ingresar un numero valido del 1 al 3")
					pack = input()
					while pack.isdigit() == False:
						print("opcion invalida")
						print("Por favor intente nuevamente.")
						pack = input()
					pack_numero = int(pack)

				

			print("Ingrese la ubicacion de su asiento",enumerador)

			ubicacionesavion()
			print("ingrese una letra")
			letra = input()
			letra = letra.upper()
			#Ingresando Letra Asiento -----------------------------------------------------------------------------
			while letra != "F" and letra != "E" and letra != "D" and letra != "C" and letra != "B" and letra != "A":
				print("opcion invalida")
				print("debe ingresar una letra valida de la imagen.")
				letra = input()
				letra = letra.upper()
			#Ingresando Numero Asiento -----------------------------------------------------------------------------
			print("Ingrese el numero de asiento")
			numero = input()
			while numero.isdigit()== False:
				print("opcion invalida")
				numero = input()
			while int(numero) < 1 or int(numero) > 33:
				print("opcion invalida")
				print("Debe ingresar un numero que sea mayor a 0 y menor a 33.")
				numero = input()
			numeroint = int(numero)
			if letra == "F":
				fila_n = 0
			if letra == "E":
				fila_n = 1
			if letra == "D":
				fila_n = 2
			if letra == "C":
				fila_n = 3
			if letra == "B":
				fila_n = 4
			if letra == "A":
				fila_n = 5

			while (n[fila_n][numeroint-1]) == 1: #al numero que escojio el usuario se le resta 1 para encanjar con la matriz
				print("Asiento ocupado")
				print("Presione cualquier tecla y elija otro asiento por favor")
				input()

				print("Ingrese la ubicacion de su asiento",enumerador)

				ubicacionesavion()
				print("Ingrese una letra")
				letra = input()
				letra = letra.upper()
				#Ingresando Letra Asiento -----------------------------------------------------------------------------
				while letra != "F" and letra != "E" and letra != "D" and letra != "C" and letra != "B" and letra != "A":
					print("opcion invalida")
					print("debe ingresar una letra valida de la imagen.")
					letra = input()
					letra = letra.upper()
				#Ingresando Numero Asiento -----------------------------------------------------------------------------
				print("Ingrese el numero de asiento")
				numero = input()
				while numero.isdigit()== False:
					print("opcion invalida")
					numero = input()
				while int(numero) < 1 or int(numero) > 33:
					print("opcion invalida")
					print("Debe ingresar un numero que sea mayor a -1 y menor a 33.")
					numero = input()
				numeroint = int(numero)
				if letra == "F":
					fila_n = 0
				if letra == "E":
					fila_n = 1
				if letra == "D":
					fila_n = 2
				if letra == "C":
					fila_n = 3
				if letra == "B":
					fila_n = 4
				if letra == "A":
					fila_n = 5

			if (n[fila_n][numeroint - 1]) == 0:
				print("Asiento comprado")
				n[fila_n][numeroint - 1] = 1

				cliente = [compra_id,rut,letra,numeroint]
				clientes.append(cliente)

# Mostrar avión ------------------------------------------------------------------------------------
	elif opc == "2":
		ubicacionesavion()
# Ver Clientes ------------------------------------------------------------------------------------
	elif opc == "3":
		while len(clientes) < 1:
			print ("Ingresar clientes primero")
			break

		for c in clientes:

			print ("Cliente numero:", c[0])
			print ("Rut:", c[1])
			print ("Letra:", c[2])
			print ("Número:", c[3])
			print("")

# Buscar Cliente ------------------------------------------------------------------------------------
	elif opc == "4":
		while len(clientes) < 1:
			print ("Ingresar clientes primero")
			break

		print ("Ingrese rut de pasajero a buscar:")
		buscar_rut = input()
		while len(buscar_rut) != 8:
			print("opcion invalida")
			print("Debe ingresar un rut de 8 digitos")
			buscar_rut = input()
		cont = 0
		for c in clientes:

			if int(buscar_rut) == int(c[1]):
				print ("Cliente numero:", c[0])
				print ("Rut:", c[1])
				print ("Letra:", c[2])
				print ("Número:", c[3])
				print("")
				cont = 1

		if cont == 0:
			print ("El pasajero ingresado no está en los registros.")
			print("")

# Reasignar ------------------------------------------------------------------------------------
	elif opc == "5":
		while len(clientes) < 1:
			print ("Ingresar clientes primero")
			break

		print ("Ingrese rut de pasajero para cambiar su asiento:")
		buscar_rut = input()
		while len(buscar_rut) != 8:
			print("opcion invalida")
			print("Debe ingresar un rut de 8 digitos")
			buscar_rut = input()

		cont = 0
		for c in clientes:
			# Reasignando valores a la variables
			if int(buscar_rut) == int(c[1]):
				compra_id = int(c[0])
				rut = c[1]
				letra = c[2]
				numero = c[3]
				cont = 1

		if cont == 0:
			print ("El pasajero ingresado no está en los registros.")
			print("")

		print("")
		print ("compra_id:", compra_id)
		print ("rut:", rut)
		print ("letra:", letra)
		print ("numero:", numero)
		print("")

		# Eliminar asiento asignado ------------------------------------------------------------------------------------
		numeroint = int(numero)
		if letra == "F":
			fila_n = 0
		if letra == "E":
			fila_n = 1
		if letra == "D":
			fila_n = 2
		if letra == "C":
			fila_n = 3
		if letra == "B":
			fila_n = 4
		if letra == "A":
			fila_n = 5
		n[fila_n][numeroint - 1] = 0 #Se borra el asiento

# se asigna el nuevo asiento--------------------------------------------------------------------------------------------

		ubicacionesavion()
		print("ingrese una letra")
		letra = input()
		letra = letra.upper()
		#Ingresando Letra Asiento -----------------------------------------------------------------------------
		while letra != "F" and letra != "E" and letra != "D" and letra != "C" and letra != "B" and letra != "A":
			print("opcion invalida")
			print("debe ingresar una letra valida de la imagen.")
			letra = input()
			letra = letra.upper()
		#Ingresando Numero Asiento -----------------------------------------------------------------------------
		print("Ingrese el numero de asiento")
		numero = input()
		while numero.isdigit()== False:
			print("opcion invalida")
			numero = input()
		while int(numero) < 1 or int(numero) > 33:
			print("opcion invalida")
			print("Debe ingresar un numero valido")
			numero = input()
		numeroint = int(numero)
		if letra == "F":
			fila_n = 0
		if letra == "E":
			fila_n = 1
		if letra == "D":
			fila_n = 2
		if letra == "C":
			fila_n = 3
		if letra == "B":
			fila_n = 4
		if letra == "A":
			fila_n = 5

		while (n[fila_n][numeroint-1]) == 1:
			print("Asiento ocupado")
			print("Presione cualquier tecla y elija otro asiento por favor")
			input()

			print("Ingrese la ubicacion de su asiento",enumerador)

			ubicacionesavion()
			print("Ingrese una letra")
			letra = input()
			letra = letra.upper()
			#Ingresando Letra Asiento -----------------------------------------------------------------------------
			while letra != "F" and letra != "E" and letra != "D" and letra != "C" and letra != "B" and letra != "A":
				print("opcion invalida")
				print("debe ingresar una letra valida de la imagen.")
				letra = input()
				letra = letra.upper()
			#Ingresando Numero Asiento -----------------------------------------------------------------------------
			print("Ingrese el numero de asiento")
			numero = input()
			while numero.isdigit()== False:
				print("opcion invalida")
				numero = input()
			while int(numero) < 1 or int(numero) > 33:
				print("opcion invalida")
				print("Debe ingresar un numero que sea mayor a -1 y menor a 33.")
				numero = input()
			numeroint = int(numero)
			if letra == "F":
				fila_n = 0
			if letra == "E":
				fila_n = 1
			if letra == "D":
				fila_n = 2
			if letra == "C":
				fila_n = 3
			if letra == "B":
				fila_n = 4
			if letra == "A":
				fila_n = 5

		if (n[fila_n][numeroint - 1]) == 0:
			print("Asiento comprado")
			n[fila_n][numeroint - 1] = 1

# Reasignar datos del cliente --------------------------------------------------------------------------------------------

		for c in clientes:
			# Reasignando valores a la variables
			if int(buscar_rut) == int(c[1]):
				c[2] = letra
				c[3] = numeroint

		print("Asiento reasignado!")

	elif opc == "6":
		if cont_pack_comun == 0:
			print("╔════════════════════════╗")
			print("  Asiento comun $60.000")
			print("╚════════════════════════╝")
			print(" cantidad vendidas: ", cont_pack_comun)
			print(" total de ganancias de asiento comun: $0 \n")
		else:
			print("╔════════════════════════════╗")
			print("  Espacio adicional $60.000")
			print("╚════════════════════════════╝")
			print("cantidad vendidas: ", cont_pack_comun)
			ganancia1 = cont_pack_comun*pack_comun
			print("total de ganancias de asiento comun: ","$",ganancia1,"\n")
		if cont_pack_adicional == 0:
			print("╔════════════════════════════╗")
			print("  Espacio adicional $80.000")
			print("╚════════════════════════════╝")
			print("cantidad vendidas: ", cont_pack_adicional)
			print(" total de ganancias de asiento comun: $0 \n")
		else:
			print("╔════════════════════════════╗")
			print("  Espacio adicional $80.000")
			print("╚════════════════════════════╝")
			print("cantidad vendidas: ", cont_pack_adicional)
			ganancia2 = cont_pack_adicional*pack_adicional
			print("total de ganancias de asiento comun: ","$",ganancia2,"\n")
		if cont_no_reclinable == 0:
			print("╔═══════════════════════╗")
			print("  No reclinable $50.000")
			print("╚═══════════════════════╝")
			print("cantidad vendidas: ", cont_no_reclinable)
			print(" total de ganancias de asiento comun: $0 \n")
		else:
			print("╔═══════════════════════╗")
			print("  No reclinable $50.000")
			print("╚═══════════════════════╝")
			print("cantidad vendidas: ", cont_no_reclinable)
			ganancia3 = cont_no_reclinable*pack_no_reclinable
			print("total de ganancias de asiento comun: ","$",ganancia3,"\n")

input()
