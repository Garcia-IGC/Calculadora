def decimalABin(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = int(partes[0])

    decimal = 0
    decimalS = ""

    if "." in numeroACambiar:

        punto = True
        decimal = int(partes[1])
        decimalS = partes[1]; 

    decimales = 0

    for char in decimalS:

        decimales = decimales + 1

    decimales = 10 ** decimales


    

    nuevoE = []
    nuevoD = []

    while(entero!=0):

        nuevoE.insert(0, str(int(entero%2)))
        entero = int(entero/2)

    iteraaciones =0

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


        if iteraaciones == 25:
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

def decimalAHex(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = int(partes[0])

    decimal = 0
    decimalS = ""

    if "." in numeroACambiar:

        punto = True
        decimal = int(partes[1])
        decimalS = partes[1]; 

    decimales = 0

    for char in decimalS:

        decimales = decimales + 1

    decimales = 10 ** decimales


    

    nuevoE = []
    nuevoD = []

    while(entero!=0):

        if(entero%16 >= 10):

            nuevoE.insert(0, str(chr(int(entero%16) + 55)))
            entero = int(entero/16)

        else:   
            nuevoE.insert(0, str(int(entero%16)))
            entero = int(entero/16)

    iteraaciones =0

    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 16

        if decimal > decimales:

            if decimal >= decimales*10:

                nuevoD.append(str(chr(int(decimal/decimales) + 55)))
                decimal = decimal - decimales*int(decimal/decimales)
            else:
                nuevoD.append(str(int(decimal/decimales)))
                decimal = decimal - decimales*int(decimal/decimales)
            

        elif decimal<decimales:

            nuevoD.append("0")

        elif decimal == decimales:

            nuevoD.append("1")



        if iteraaciones == 25:
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

def decimalAOct(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = int(partes[0])

    decimal = 0
    decimalS = ""

    if "." in numeroACambiar:

        punto = True
        decimal = int(partes[1])
        decimalS = partes[1]; 

    decimales = 0

    for char in decimalS:

        decimales = decimales + 1

    decimales = 10 ** decimales


    

    nuevoE = []
    nuevoD = []

    while(entero!=0):

        nuevoE.insert(0, str(int(entero%8)))
        entero = int(entero/8)

    iteraaciones =0

    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 8

        if decimal > decimales:

            nuevoD.append(str(int(decimal/decimales)))
            decimal = decimal - decimales*int(decimal/decimales)
            

        elif decimal<decimales:

            nuevoD.append("0")

        elif decimal == decimales:

            nuevoD.append("1")



        if iteraaciones == 25:
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

    suma = 0

    for i in range(0, len(num)):

        potencia = 2**(-i-1)
        print(potencia)
        suma = suma + (int(frac[i]) * (potencia))
        


    print(suma)
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
    

    nuevoE = ""

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

            nuevoD = nuevoD + "1"



        if iteraaciones == 100000:
            break



    

    final = nuevoE

    if(punto == True):
        final = final + "." + nuevoD
    

    return final

def binAHex(num):

    numeroACambiar = num

    punto = False

    partes = (numeroACambiar.split("."))

    entero = str(partes[0])



    decimal = ""
    decimalS = ""

    if "." in numeroACambiar:

        punto = True
        decimalS = str(partes[1])

    while(len(entero)%4 != 0):

        entero = "0" + entero
    

    nuevoE = ""

    for i in range(0,len(entero),4):

        

        
        num1 = int(entero[i]) * (2**3) 
        num2 = int(entero[i+1]) * (2**2) 
        num3 = int(entero[i+2]) * (2**1)        
        num4 = int(entero[i+3]) * (2**0)
        

        numR = num1 + num2 + num3 + num4

        if numR >= 10:

            carac = chr(numR + 55)
            nuevoE = nuevoE + str(carac)
        else:
            nuevoE = nuevoE + str(numR)

    decimalS = fracADec(decimalS)

    decimales = 10 ** len(decimalS)

    decimal = int(decimalS)

    nuevoD= ""

    iteraaciones = 0
    while(decimal != decimales and punto == True):

        iteraaciones = iteraaciones+1
        decimal = decimal * 16

        if decimal > decimales:

            if decimal >= decimales*10:

                nuevoD = nuevoD + str(chr(int(decimal/decimales) + 55))
                decimal = decimal - decimales*int(decimal/decimales)
            else:
                nuevoD = nuevoD + str(int(decimal/decimales))
                decimal = decimal - decimales*int(decimal/decimales)
            

        elif decimal<decimales:

            nuevoD = nuevoD + "0"

        elif decimal == decimales:

            nuevoD = nuevoD + "1"



        if iteraaciones == 100000:
            break



    

    final = nuevoE

    if(punto == True):
        final = final + "." + nuevoD
    

    return final

def binADec(num):

    numeroACambiar = num

    respuesta = 0

    partes = numeroACambiar.split(".")

    tamano = len(partes[0])

    for i in range (0, len(numeroACambiar)):
        if(numeroACambiar[i]!='.'):

            if i < tamano:

                potencia = 2 ** (tamano-1-i)

            else:

                potencia = 2 ** (tamano-i)

            respuesta = respuesta + int(numeroACambiar[i]) * potencia
                                    
    return str(respuesta)

def octADec(num):

    numeroACambiar = num

    respuesta = 0

    partes = numeroACambiar.split(".")

    tamano = len(partes[0])

    for i in range (0, len(numeroACambiar)):
        if(numeroACambiar[i]!='.'):

            if i < tamano:

                potencia = 8 ** (tamano-1-i)

            else:

                potencia = 8 ** (tamano-i)

            respuesta = respuesta + int(numeroACambiar[i]) * potencia
                                    
    return str(respuesta)

def hexADec(num):

    numeroACambiar = num

    respuesta = 0.0

    partes = numeroACambiar.split(".")

    tamano = len(partes[0])

    for i in range (0, len(numeroACambiar)):
        if(numeroACambiar[i]!='.'):

            aux = numeroACambiar[i]

            if i < tamano:

                potencia = 16 ** (tamano-1-i)

            else:

                potencia = 16 ** (tamano-i)

            if((numeroACambiar[i]) >= 'A'):

                if(numeroACambiar[i] == 'A'):
                    aux=10
                elif(numeroACambiar[i]=='B'):
                    aux=11
                elif(numeroACambiar[i]=='C'):
                    aux=12
                elif(numeroACambiar[i]=='D'):
                    aux=13
                elif(numeroACambiar[i]=='E'):
                    aux=14
                elif(numeroACambiar[i]=='F'):
                    aux=15

            aux = int(aux)
            respuesta = respuesta + aux * potencia
                                    
    return str(respuesta)