numeroACambiar = "192.912381298"

punto = False

partes = (numeroACambiar.split("."))

entero = int(partes[0])

decimal = 0;

if "." in numeroACambiar:

    decimal = int(partes[1])

print(entero)
print(decimal)