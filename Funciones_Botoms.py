import tkinter as tk
from tkinter import*
import json
import os

def Agregar():
    Ventan_Agred_Prod = tk.Tk()
    Ventan_Agred_Prod.geometry("400x400")
    Ventan_Agred_Prod.title("Sistema de Ventas")
    Ventan_Agred_Prod.configure(bg="snow3")

    
    celda_Producto = tk.Label(Ventan_Agred_Prod, text="Producto", font="bold")
    celda_Producto.configure(bg="ivory3")
    celda_Cantida = tk.Label(Ventan_Agred_Prod, text="Cantidad", font="bold")
    celda_Cantida.configure(bg="ivory3")
    celda_Precio = tk.Label(Ventan_Agred_Prod, text="Precio", font="bold")
    celda_Precio.configure(bg="ivory3")

    
    celda_Producto.place(x=50, y=10)
    celda_Cantida.place(x=50, y=55)
    celda_Precio.place(x=50, y=100)

    
    entradaNota1 = tk.Entry(Ventan_Agred_Prod)
    entradaNota2 = tk.Entry(Ventan_Agred_Prod) 
    entradaNota3 = tk.Entry(Ventan_Agred_Prod)

    
    entradaNota1.place(x=130, y=10, width=225, height=20)
    entradaNota2.place(x=130, y=55, width=225, height=20)
    entradaNota3.place(x=130, y=100, width=225, height=20)
    
    return