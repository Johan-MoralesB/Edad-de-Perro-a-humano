nombre = input("¿Cuál es el nombre de tu perro? ")
edad_perro = int(input(f"¿Cuántos años tiene {nombre}? "))

edad_humana = edad_perro * 7

print(f"{nombre} tiene {edad_perro} años, lo que equivale a {edad_humana} años humanos.")
input("Presiona Enter para salir...")