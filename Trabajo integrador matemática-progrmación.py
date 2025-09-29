# Trabajo integrador que relaciona matemáticas y programación en Python

# Calculadora de Operaciones Bit a Bit:
# Desarrollen un programa que reciba dos números.
# Aplique operaciones bit a bit (AND, OR, XOR) mostrando el resultado tanto en formato decimal como binario.

print("Bienvenidos a la Calculadora de Operaciones Bit a Bit")
# Pedir números enteros (positivos y negativos)
while True:
    try:
        a = int(input("Ingrese el primer número entero: "))
        b = int(input("Ingrese el segundo número entero: "))
        break
    except ValueError:
        print("Error: debe ingresar solo números enteros.")
# Mostramos los números en binario (8 bits)
print(". . .")
print(f"{a} en binario (8 bits): {a & 0xFF:08b}")
print(f"{b} en binario (8 bits): {b & 0xFF:08b}")
encendido = True
while encendido:
    print("\nIndique la operación que quiere realizar: ")
    print("1- AND\n2- OR\n3- XOR\nOtro caracter- Salir ")
    menu = input("Opción: ")

    if menu == "1":
# AND
        operacion_and= a & b
        print(". . .")
        print(f"{a} & {b} en → decimal: {operacion_and}  → binario: {operacion_and:08b}")
        print()
        mas = input("¿Querés conocer más sobre AND? (S/N): ").upper()
        if mas == "S":
            print("**Explicación del AND:** El resultado es 1 solo si AMBOS bits son 1.")
            print("Ejemplo: 1 & 1 = 1, pero 1 & 0 = 0, 0 & 1 = 0, 0 & 0 = 0.")
        print()
        print(f"  {a & 0xFF:08b}  ({a})")
        print(f"& {b & 0xFF:08b}  ({b})")
        print("  --------")
        print(f"  {operacion_and & 0xFF:08b}  ({operacion_and})")
        print()
# OR      
    elif menu == "2":
        operacion_or = a | b
        print(". . .")
        print(f"{a} | {b} en → decimal: {operacion_or}  → binario: {operacion_or & 0xFF:08b}")
        print()
        mas = input("¿Querés conocer más sobre OR? (S/N): ").upper()
        if mas == "S":
            print("**Explicación del OR:** El resultado es 1 si ALGUNO de los bits es 1.")
            print("Ejemplo: 1 | 0 = 1, 0 | 1 = 1, 1 | 1 = 1, 0 | 0 = 0.")
            print()
            print(f"  {a & 0xFF:08b}  ({a})")
            print(f"| {b & 0xFF:08b}  ({b})")
            print("  --------")
            print(f"  {operacion_or & 0xFF:08b}  ({operacion_or})")
            print()
# XOR
    elif menu == "3":
        print(". . .")
        operacion_xor = a ^ b
        print(f"{a} ^ {b} = {operacion_xor}  → binario: {operacion_xor & 0xFF:08b}")
        print()
        mas = input("¿Querés conocer más sobre XOR? (S/N): ").upper()
        if mas == "S":
            print("**Explicación del XOR:** El resultado es 1 si los bits son DIFERENTES.")
            print("Ejemplo: 1 ^ 0 = 1, 0 ^ 1 = 1, pero 1 ^ 1 = 0, 0 ^ 0 = 0.")
        print()
        print(f"  {a & 0xFF:08b}  ({a})")
        print(f"^ {b & 0xFF:08b}  ({b})")
        print("  --------")
        print(f"  {operacion_xor & 0xFF:08b}  ({operacion_xor})")
        print()
    else:
        i=input("Carácter inválido, seguro que querés salir? S/N: ").upper()
        if i == "N":
            print("Volvemos al menu")
            continue
        elif i =="S":
            print("¡Gracias por jugar, saludos!")
            encendido = False






