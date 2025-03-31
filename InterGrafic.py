import funciones
import tkinter as tk
from tkinter import ttk


def ventana_principal():

    def convertir():

        numero_entrada = numero_inicial.get()
        base_cambiable = base_entrada.get()
        
        if(base_cambiable == "10") :

            resultadobin = funciones.decimalABin(numero_entrada)
           
            resultadodec = numero_entrada
            
            resultado_oct = funciones.decimalAOct(numero_entrada)
            
            resultado_hex = funciones.decimalAHex(numero_entrada)
            
            binario_salida.config(state="normal")
            binario_salida.delete(0,tk.END)
            binario_salida.insert(0,resultadobin)
            binario_salida.config(state="readonly")

            decimal_salida.config(state="normal")
            decimal_salida.delete(0,tk.END)
            decimal_salida.insert(0,resultadodec)
            decimal_salida.config(state="readonly")

            octal_salida.config(state="normal")
            octal_salida.delete(0,tk.END)
            octal_salida.insert(0,resultado_oct)
            octal_salida.config(state="readonly")

            hex_salida.config(state="normal")
            hex_salida.delete(0,tk.END)
            hex_salida.insert(0,resultado_hex)
            hex_salida.config(state="readonly")

        elif(base_cambiable =="2") :

            resultadobin = numero_entrada
            ####pasar numero a binario
            numero_cambiado = funciones.binADec(numero_entrada)

            resultadodec = numero_cambiado


            resultado_oct = funciones.decimalAOct(numero_cambiado)


            resultado_hex = funciones.decimalAHex(numero_cambiado)

            binario_salida.config(state="normal")
            binario_salida.delete(0,tk.END)
            binario_salida.insert(0,resultadobin)
            binario_salida.config(state="readonly")

            decimal_salida.config(state="normal")
            decimal_salida.delete(0,tk.END)
            decimal_salida.insert(0,resultadodec)
            decimal_salida.config(state="readonly")

            octal_salida.config(state="normal")
            octal_salida.delete(0,tk.END)
            octal_salida.insert(0,resultado_oct)
            octal_salida.config(state="readonly")

            hex_salida.config(state="normal")
            hex_salida.delete(0,tk.END)
            hex_salida.insert(0,resultado_hex)
            hex_salida.config(state="readonly")

        elif (base_cambiable == "8"):
            
            resultado_oct = numero_entrada

            numero_cambiado = funciones.octADec(numero_entrada)

            resultadodec = numero_cambiado

            resultado_hex = funciones.decimalAHex(numero_cambiado)

            resultadobin = funciones.decimalABin(numero_cambiado)

            binario_salida.config(state="normal")
            binario_salida.delete(0,tk.END)
            binario_salida.insert(0,resultadobin)
            binario_salida.config(state="readonly")

            decimal_salida.config(state="normal")
            decimal_salida.delete(0,tk.END)
            decimal_salida.insert(0,resultadodec)
            decimal_salida.config(state="readonly")

            octal_salida.config(state="normal")
            octal_salida.delete(0,tk.END)
            octal_salida.insert(0,resultado_oct)
            octal_salida.config(state="readonly")

            hex_salida.config(state="normal")
            hex_salida.delete(0,tk.END)
            hex_salida.insert(0,resultado_hex)
            hex_salida.config(state="readonly")
        elif (base_cambiable == "16") :

            resultado_hex = numero_entrada

            numero_cambiado = funciones.hexADec(numero_entrada)

            resultadodec = numero_cambiado
            
            resultadobin = funciones.decimalABin(numero_cambiado)

            resultado_oct = funciones.decimalAOct(numero_cambiado)

            binario_salida.config(state="normal")
            binario_salida.delete(0,tk.END)
            binario_salida.insert(0,resultadobin)
            binario_salida.config(state="readonly")

            decimal_salida.config(state="normal")
            decimal_salida.delete(0,tk.END)
            decimal_salida.insert(0,resultadodec)
            decimal_salida.config(state="readonly")

            octal_salida.config(state="normal")
            octal_salida.delete(0,tk.END)
            octal_salida.insert(0,resultado_oct)
            octal_salida.config(state="readonly")

            hex_salida.config(state="normal")
            hex_salida.delete(0,tk.END)
            hex_salida.insert(0,resultado_hex)
            hex_salida.config(state="readonly")


            



        
        
        
        
    ventana = tk.Tk()
    ventana.title("Calculadora") 
    ventana.geometry("500x700")  

    #frames

    cuadro_entradas = tk.Frame(ventana)
    cuadro_desplegable = tk.Frame(ventana)
    cuadro_binario = tk.Frame(ventana)
    cuadro_decimal = tk.Frame(ventana)
    cuadro_octal = tk.Frame(ventana)
    cuadro_hex = tk.Frame(ventana)

    #titulo
    titulo = tk.Label(ventana,text="Conversor de Bases",font=("Times New Roman",20))
    titulo.pack(pady=20)

    #numero de entrada
    texto_entrada = tk.Label(cuadro_entradas, text= "Numero a convertir: ", font="Arial 12 bold")
    texto_entrada.pack(side=tk.LEFT, padx= 10, pady = 10)
    numero_inicial = tk.Entry(cuadro_entradas,font="Arial 12 bold")
    numero_inicial.pack(side=tk.RIGHT, padx=10,pady=10)
    cuadro_entradas.pack()

    #desplegables
    base_entrada = tk.StringVar()
    texto_desplegable = tk.Label(cuadro_desplegable,text= "Base de entrada: ",font=("Times New Roman",18))
    desplegable_entradas = ttk.Combobox(cuadro_desplegable,
    font = "Arial 12",
    width=2,
    values = ["2","8","10","16"],
    state="readonly",
    textvariable=base_entrada)
    desplegable_entradas.pack(side=tk.RIGHT,pady=5)
    texto_desplegable.pack(side=tk.LEFT,padx = 10,pady = 10)
    desplegable_entradas.set("2")
    cuadro_desplegable.pack()

    #boton
    boton = tk.Button(ventana,text="Transformar",padx=40,pady=10,bd=3,command=convertir)
    boton.pack()

    #cambios de base

    #binario
    texto_binario = tk.Label(cuadro_binario, text="Binario: ", font=("Times New Roman",12))
    texto_binario.pack(side=tk.LEFT)
    binario_salida =tk.Entry(cuadro_binario,text="",font="Arial 12",width=40)
    binario_salida.pack(side=tk.RIGHT,padx=10,pady=10)
    cuadro_binario.pack()

    #Decimal

    texto_decimal = tk.Label(cuadro_decimal, text="Decimal: ", font=("Times New Roman",12))
    texto_decimal.pack(side=tk.LEFT)
    decimal_salida =tk.Entry(cuadro_decimal,text="",font="Arial 12",width=40)
    decimal_salida.pack(side=tk.RIGHT,padx=10,pady=10)
    cuadro_decimal.pack()

    #octal

    texto_octal = tk.Label(cuadro_octal, text="octal: ", font=("Times New Roman",12))
    texto_octal.pack(side=tk.LEFT)
    octal_salida = tk.Entry(cuadro_octal,text="",font="Arial 12",width=40)
    octal_salida.pack(side=tk.RIGHT,padx=10,pady=10)
    cuadro_octal.pack()

    #hex

    texto_hex = tk.Label(cuadro_hex, text="hex: ", font=("Times New Roman",12))
    texto_hex.pack(side=tk.LEFT)
    hex_salida = tk.Entry(cuadro_hex,text="",font="Arial 12",width=40)
    hex_salida.pack(side=tk.RIGHT,padx=10,pady=10)
    cuadro_hex.pack()
    ventana.mainloop()