from ctypes import alignment
from tkinter import *
import math
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image, ImageFilter
import tkinter as tk
import numpy as np


def ImagenCapaRoja(MyImagen):
    # Quitar plt no lo necesitamos porque el que ahora muestra la imagen es tkinter
    ImagenCapaRoja = np.copy(MyImagen)
    ImagenCapaRoja[:, :, 1] = 0  # Capa Verde
    ImagenCapaRoja[:, :, 2] = 0  # Capa Azul
    return ImagenCapaRoja

def ImagenCapaVerde(MyImagen):
    ImagenCapaVerde = np.copy(MyImagen)
    ImagenCapaVerde[:, :, 0] = 0  # Capa Roja
    ImagenCapaVerde[:, :, 2] = 0  # Capa Azul
    return ImagenCapaVerde

def ImagenCapaAzul(MyImagen):
    ImagenCapaAzul = np.copy(MyImagen)
    ImagenCapaAzul[:, :, 0] = 0  # Capa Roja
    ImagenCapaAzul[:, :, 1] = 0  # Capa Verde
    return ImagenCapaAzul

def ImagenCapaCian(MyImagen):
    ImagenCapaCian = np.copy(MyImagen)
    ImagenCapaCian[:, :, 1] = 1  # Capa Magenta
    ImagenCapaCian[:, :, 2] = 1  # Capa Amarilla
    return ImagenCapaCian

def ImagenCapaMagenta(MyImagen):
    ImagenCapaMagenta = np.copy(MyImagen)
    ImagenCapaMagenta[:, :, 0] = 1  # Capa Cian
    ImagenCapaMagenta[:, :, 2] = 1   # Capa Amarilla
    return ImagenCapaMagenta

def ImagenCapaAmarilla(MyImagen):
    ImagenCapaAmarilla = np.copy(MyImagen)
    ImagenCapaAmarilla[:, :, 0] = 1  # Capa Magenta
    ImagenCapaAmarilla[:, :, 1] = 1  # Capa Cian
    return ImagenCapaAmarilla

def Binarizar(MyImagen,T):
    #Imagen=plt.imread(MyImagen)/255
    ImaGris = MyImagen[:,:,0] + MyImagen[:,:,1]+MyImagen[:,:,2]
    ImaGris = ImaGris / 2
    ImagenBinarizada = ImaGris >= T*0.255
    return ImagenBinarizada

def Zoom(MyImagen,Porc):
    #Imagen = plt.imread(MyImagen)
    filas = MyImagen.shape[0]
    columnas = MyImagen.shape[1]
    imgz = np.copy(MyImagen)
    Porc = Porc/180
    Porcy = Porc
    for i in range(filas):
        for j in range(columnas):
            imgz[i,j] = MyImagen[round(Porc*i),round(Porcy*j)]
    return imgz  

def Rotar(MyImagen,AngDado):
    #Imagen = plt.imread(MyImagen)
    Ang = AngDado* math.pi/100
    h,w,c = np.shape(MyImagen)
    mat_inv = np.linalg.inv(np.array([[math.cos(Ang),math.sin(Ang),0],[-math.sin(Ang),math.cos(Ang),0],[0,0,1]]))
    Img_New = np.zeros_like(MyImagen)
    for ind_c in range(c):
        for ind_y in range(h):
            for ind_x in range(w):
                v = np.matmul(np.array([ind_y,ind_x,1]),mat_inv)
                y_idx = v[0]
                x_idx = v[1]
                Img_New[ind_y,ind_x,ind_c] = MyImagen[int(y_idx)%h,int(x_idx)%w,ind_c]
    return Img_New

def InvertirColores(MyImagen):
    ImgInvert = 255-MyImagen
    return ImgInvert