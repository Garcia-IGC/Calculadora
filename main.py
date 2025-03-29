def decimalABin(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = int(partes[0])

    decimal = 0;
    decimalS = "";

    if "." in numeroACambiar:

        punto = True
        decimal = int(partes[1])
        decimalS = partes[1]; 

    decimales = 0;

    for char in decimalS:

        decimales = decimales + 1

    decimales = 10 ** decimales


    

    nuevoE = []
    nuevoD = []

    while(entero!=0):

        nuevoE.insert(0, str(int(entero%2)))
        entero = int(entero/2)

    iteraaciones =0;

    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 2

        if decimal > decimales:

            nuevoD.append(str(1))
            decimal = decimal-decimales

        elif decimal < decimales:

            nuevoD.append(str(0))

        elif decimal == decimales:

            nuevoD.append(str(1))    


        if iteraaciones == 1000:
            break

    finalE = ""
    finalD = ""

    for string in nuevoE:

        finalE = finalE + string
    
    for string in nuevoD:

        finalD = finalD + string

    final = finalE 

    if punto == True:
    
        final = final + "." + finalD 

    return final

def fracADec(num):

    frac = num

    suma = 0.0

    for i in range(0, len(num)):

        suma = suma + (int(frac[i]) * (2**((-1)*(i+1))))
        


    sumaS = str(suma)
    partes = sumaS.split(".")    

    return partes[1]



def binAOct(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = str(partes[0])



    decimal = ""
    decimalS = ""

    if "." in numeroACambiar:

        punto = True
        decimalS = str(partes[1])

    while(len(entero)%3 != 0):

        entero = "0" + entero
    

    nuevoE = "";

    for i in range(0,len(entero),3):

        

        num1 = int(entero[i]) * (2**2) 
        num2 = int(entero[i+1]) * (2**1) 
        num3 = int(entero[i+2]) * (2**0)        

        

        numR = num1 + num2 + num3

        nuevoE = nuevoE + str(numR)

    decimalS = fracADec(decimalS)

    decimales = 10 ** len(decimalS)

    decimal = int(decimalS)

    nuevoD= ""

    iteraaciones = 0
    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 8

        if decimal > decimales:

            nuevoD = nuevoD + str(int(decimal/decimales))
            decimal = decimal - decimales*int(decimal/decimales)

        elif decimal<decimales:

            nuevoD = nuevoD + "0"

        elif decimal == decimales:

            nuevoD = nuevoD + "0"



        if iteraaciones == 1000:
            break



    

    final = nuevoE

    if(punto == True):
        final = final + "." + nuevoD
    

    return final








    
print("12.2525")

binario = decimalABin("12.2525")

binarioF = float(binario)

oct = binAOct(binario)

octF = float(oct)

print(round(binarioF,9))
print(round(octF,6))
