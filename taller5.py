import math
import numpy as np
import matplotlib.pyplot as plt

"""1.Elaborar una función a la que se le envié de una imagen y un factor de
    ajuste (permite aumentar o disminuir el brillo), la función debe
    retornar la imagen con el brillo deseado de acuerdo al factor de ajuste
"""

def BrilloImagen(MyImagen,FactBrillo):
    Imagen = plt.imread(MyImagen) / 255
    BrilloImagen=MatrizPorEscalar(Imagen,FactBrillo)
    return BrilloImagen

def MatrizPorEscalar(NewMatriz,Escalar):
        Tam=np.shape(NewMatriz)
        Fila = Tam[0]
        Columna = Tam[1]
        for i in range(Fila): 
            for x in range(Columna):
                NewMatriz[i,x] = NewMatriz[i,x]*Escalar
        return NewMatriz

def BrilloImagenCapa(MyImagen,FactorBrillo):    
    BrilloCapaImagen=MatrizPorEscalar(MyImagen,FactorBrillo)
    return BrilloCapaImagen

def ImagenCapaRoja(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    ImagenCapaRoja = np.copy(MyImagen)
    ImagenCapaRoja[:, :, 1] = 0  # Capa Verde
    ImagenCapaRoja[:, :, 2] = 0  # Capa Azul
    return ImagenCapaRoja


def ImagenCapaVerde(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    ImagenCapaVerde = np.copy(MyImagen)
    ImagenCapaVerde[:, :, 0] = 0  # Capa Roja
    ImagenCapaVerde[:, :, 2] = 0  # Capa Azul
    return ImagenCapaVerde

def ImagenCapaAzul(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255

    ImagenCapaAzul = np.copy(MyImagen)
    ImagenCapaAzul[:, :, 0] = 0  # Capa Roja
    ImagenCapaAzul[:, :, 1] = 0  # Capa Verde
    return ImagenCapaAzul

"""3.Elaborar una función a la que se le envié de una imagen y un factor de
    contraste, la función debe retornar la imagen con el contraste
    deseado de acuerdo al factor de contraste
"""

def ContrasteImagen(MyImagen,FactContraste):
    Imagen = plt.imread(MyImagen)/255
    ImgContraste = FactContraste*np.log10(1+Imagen)
    return ImgContraste

"""5. Elaborar una función que permita binarizar una imagen"""

def Binarizar(MyImagen,T):
    Imagen=plt.imread(MyImagen)/255
    ImaGris = Imagen[:,:,0] + Imagen[:,:,1]+Imagen[:,:,2]
    ImaGris = ImaGris / 2
    ImagenBinarizada = ImaGris >= T*0.255
    return ImagenBinarizada

"""4. Elaborar una función que permita realizarle un zoom a una parte de la imagen"""

def Zoom(MyImagen,Porc):
    Imagen = plt.imread(MyImagen)
    filas = Imagen.shape[0]
    columnas = Imagen.shape[1]

    imgz = np.copy(Imagen)

    Porc = Porc/180
    Porcy = Porc

    for i in range(filas):
        for j in range(columnas):
            imgz[i,j] = Imagen[round(Porc*i),round(Porcy*j)]

    return(imgz)

"""6. Elaborar una función que permita rotar una imagen"""

def Rotar(MyImagen,AngDado):
    Imagen = plt.imread(MyImagen)
    Ang = AngDado* math.pi/100
    h,w,c = np.shape(Imagen)
    mat_inv = np.linalg.inv(np.array([[math.cos(Ang),math.sin(Ang),0],[-math.sin(Ang),math.cos(Ang),0],[0,0,1]]))
    Img_New = np.zeros_like(Imagen)
    for ind_c in range(c):
        for ind_y in range(h):
            for ind_x in range(w):
                v = np.matmul(np.array([ind_y,ind_x,1]),mat_inv)
                y_idx = v[0]
                x_idx = v[1]
                Img_New[ind_y,ind_x,ind_c] = Imagen[int(y_idx)%h,int(x_idx)%w,ind_c]
    return Img_New

"""7. Elaborar un procedimiento que permita sacar el histograma de cada
una de las capas de una imagen"""

def Histograma(MyImagen):
    Imagen=plt.imread(MyImagen)
    ImagenGris = Imagen[:,:,0]+Imagen[:,:,1]+Imagen[:,:,2]
    ImagenGris = ImagenGris/3
    ImagenHistograma = np.trunc(np.around(ImagenGris*255,0))
    plt.figure("Histograma")
    plt.hist(ImagenHistograma.ravel(),256,[0,256])
    plt.show()

"""Punto 1"""

brillo=BrilloImagen("prueba.jpg",3)
plt.imshow(brillo)
plt.show()

"""Punto2"""

BrilloCapa=BrilloImagenCapa(ImagenCapaRoja("prueba.jpg"),0.5)
plt.subplot(1,3,1)
plt.imshow(BrilloCapa)
BrilloCapa=BrilloImagenCapa(ImagenCapaVerde("prueba.jpg"),3)
plt.subplot(1,3,2)
plt.imshow(BrilloCapa)
BrilloCapa=BrilloImagenCapa(ImagenCapaAzul("prueba.jpg"),6)
plt.subplot(1,3,3)
plt.imshow(BrilloCapa)
plt.show()

'''Punto 3'''

Contraste=ContrasteImagen("prueba.jpg",8)
plt.imshow(Contraste)
plt.show()

'''Punto 4'''

plt.title("Imagen con Zoom")
plt.imshow(Zoom("prueba.jpg",80))
plt.show()

'''Punto 5'''

plt.title("Imagen Binarizada")
plt.imshow(Binarizar("prueba.jpg",2))
plt.show()

'''Punto 6'''

plt.title("Imagen rotada")
plt.imshow(Rotar("prueba.jpg",30))
plt.show()

'''Punto 7'''

Histograma("prueba.jpg")
