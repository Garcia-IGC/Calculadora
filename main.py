def decimalABin(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = int(partes[0])

    decimal = 0;
    decimalS = "";

    if "." in numeroACambiar:

        decimal = int(partes[1])
        decimalS = partes[1]; 

    decimales = 0;

    for char in decimalS:

        decimales = decimales + 1

    decimales = 10 ** decimales


    print(entero)
    print(decimal)
    print(decimales)

    nuevoE = []
    nuevoD = []

    while(entero!=0):

        nuevoE.insert(0, int(entero%2))
        entero = int(entero/2)

    iteraaciones =0;

    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 2

        if decimal > decimales:

            nuevoD.append(1)
            decimal = decimal-decimales

        if decimal < decimales:

            nuevoD.append(0)

        if decimal == decimales:

            nuevoD.append(1)    


        if iteraaciones == 20:
            break



    print(nuevoE)
    print(nuevoD)


decimalABin("12")