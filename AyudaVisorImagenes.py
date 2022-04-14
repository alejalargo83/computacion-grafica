""" Desarrollado por: Francisco Alejandro Medina. 
e-mail: famedina@utp.edu.co

---------------------------------------
Visor de Imágenes
---------------------------------------
"""

from ctypes import alignment
from tkinter import *

from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import tkinter as tk

# Crear ventana Tk
Window = Tk()
Window.geometry("1024x720")
Window.resizable(False, False)
Window.title("Visor de imagenes")

# Variables de Control
Seleccion = IntVar(value=1)


# Caja para ruta del Archivo
txtImage = Entry(Window, width=90)
txtImage.grid(row=2, column=1, columnspan=3, sticky=W)


# Label para mostrar Imagen
LbImage = Label(
    image="",
    text="<< Imagen >>",
    foreground="white",
    anchor=CENTER,
    justify=CENTER,
    font=("Arial black", 50),
    pad=0,
)
LbImage.place(x=0,y=30)


# Procedimiento para cargar imágen en la ventana Tk
def CargarImagen():
    if txtImage.get() == "":
        path = OpenFile()
    else:
        path = txtImage.get()
    Imagen = Image.open(path)
    Imagen = Imagen.resize((650, 500), Image.ADAPTIVE)
    Imagen = ImageTk.PhotoImage(Imagen)
    LbImage.configure(image=Imagen)
    Window.mainloop()

# Función para explorar sistema de ficheros
# Retorna: ruta del fichero seleccionado
def OpenFile():
    file = filedialog.askopenfilename(
        filetypes=[
            ("Image Files JPG/JPEG", "*jpg"),
            ("Image Files JPG/JPEG", "*jpeg"),
            ("Image Files PNG", "*png"),
            ("Image Files GIF", "*gif"),
        ]
    )
    if file != None and file != "":
        txtImage.delete(0, END)
        txtImage.insert(0, file)
        CargarImagen()
    return file

# Boton para explorar ficheros

btnExplorarArchivos = Button(Window, text="Cargar Imagen", width=20, command=lambda: OpenFile())
btnExplorarArchivos.grid(row=2, column=0, sticky=W)


"""Se crea un marco en el cual se colocan los botones para minipular la imagen""" 

frame_2 = Frame(Window)
frame_2.grid(column=4, row=5)


"""Se crea el boton par elegir el tipo de imagen deseada"""

Seleccion = IntVar()
LbOperacion = Label(frame_2, text="Tipo:     ", font=("Arial Bold", 10))
LbOperacion.grid(column=0, row=0, sticky=W)
CbOperacion = Combobox(frame_2, values=("", "", "", ""))
CbOperacion.grid(column=1, row=0, sticky=W)
CbOperacion.current(0)



"""Se crean los botones para los diferentes canales RGB (rojo, verde, azul)"""

ChkOpcion1 = Label(frame_2, text="Canales RGB:", font=("Arial Bold", 10))
ChkOpcion1.grid(column=0, row=8, sticky=W)

ChkOpcion2 = Button(frame_2, text="Red", width=20, command=lambda: OpenFile())
ChkOpcion2.grid(column=1, row=7, sticky=W)
ChkOpcion3 = Button(frame_2, text="Green", width=20, command=lambda: OpenFile())
ChkOpcion3.grid(column=1, row=8, sticky=W)
ChkOpcion4 = Button(frame_2, text="Blue", width=20, command=lambda: OpenFile())
ChkOpcion4.grid(column=1, row=9, sticky=W)

"""Se crean los botones para los diferentes canales CMYK (cian, magenta, amarillo)"""

ChkOpcion5 = Label(frame_2, text="Canales CMYK:", font=("Arial Bold", 10))
ChkOpcion5.grid(column=0, row=12, sticky=W)

ChkOpcion6 = Button(frame_2, text="Cian", width=20, command=lambda: OpenFile())
ChkOpcion6.grid(column=1, row=11, sticky=W)
ChkOpcion7 = Button(frame_2, text="Magenta", width=20, command=lambda: OpenFile())
ChkOpcion7.grid(column=1, row=12, sticky=W)
ChkOpcion8 = Button(frame_2, text="Amarillo", width=20, command=lambda: OpenFile())
ChkOpcion8.grid(column=1, row=13, sticky=W)

# Se cre el boton para el brillo

Opcion1 = Label(frame_2, text="Brillo ", font=("Arial Bold", 10))
Opcion1.grid(column=0, row=15, sticky=W)
w = Scale(frame_2, from_=0, to=200, orient=HORIZONTAL)
w.grid(column=1, row=15, sticky=W)

# Se cre el boton para el contraste

Opcion2 = Label(frame_2, text="Contraste ", font=("Arial Bold", 10))
Opcion2.grid(column=0, row=16, sticky=W)
w = Scale(frame_2, from_=0, to=200, orient=HORIZONTAL)
w.grid(column=1, row=16, sticky=W)


# Espacios en blanco para mejor visulizacion

ChkOpcion = Label(frame_2, text="  ", font=("Arial Bold", 10))
ChkOpcion.grid(column=0, row=6, sticky=W)
ChkOpcion0 = Label(frame_2, text="  ", font=("Arial Bold", 10))
ChkOpcion0.grid(column=0, row=10, sticky=W)
Opcion0 = Label(frame_2, text="  ", font=("Arial Bold", 10))
Opcion0.grid(column=0, row=14, sticky=W)




Window.mainloop()

