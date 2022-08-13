numero = 6 
numero_ingresado = int(input("Adivina el numero: "))
while numero_ingresado != numero:
    if numero_ingresado < numero:
        print("Incorrecto, ingrese un numero mas alto")
    elif numero_ingresado > numero:
        print("Incorrecto, ingrese un numero mas bajo")
    numero_ingresado = int(input("Adivina el numero: "))
print("Adivinaste!")