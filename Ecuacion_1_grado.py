#Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox

# funciones de la app

def ejecutar():
    if int(b.get())>0:
        x =-int(b.get())/int(m.get())
        print("x=" +str(x))
    else:
        x = int(b.get())/int(m.get())
        print("x=" +str(x))
      
    
    t_resultados.insert(INSERT, "El valor de es X = "+str(x)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    m.set("")
    b.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

m = StringVar()
b  = StringVar()

#frame entrada datos

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "green2", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Logo de la app
logo = PhotoImage(file="img/download.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=61,y=61)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Ecuacion de primer grado (mx + b = 0)")
titulo.config(bg = "green2", fg = "white", font = ("Arial",16))
titulo.place(x = 80, y = 10)

# Etiqueta para m
lb_m = Label(frame_entrada, text = "m = ")
lb_m.config(bg="green2", fg="white", font=("Arial",16))
lb_m.place(x=240, y=50, width=115, height=30)

# Entry para m
entry_m = Entry(frame_entrada, textvariable=m)
entry_m.config(font=("Arial",20), justify=LEFT,fg="black")
entry_m.focus_set()
entry_m.place(x=335, y=50, width=115, height=30)

# Etiqueta para b
lb_b = Label(frame_entrada, text = "b = ")
lb_b.config(bg="green2", fg="white", font=("Arial",16))
lb_b.place(x=240, y=90, width=115, height=30)

# Entry para b
entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(font=("Arial",20), justify=LEFT,fg="black")
entry_b.place(x=335, y=90, width=115, height=30)

#frame operaciones

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "green2", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Boton para resolver
bt_ejecutar = Button(frame_operaciones, text="Resolver", command=ejecutar)
bt_ejecutar.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_borrar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()