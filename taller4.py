import numpy as np
import matplotlib.pyplot as plt

#1. Elaborar un procedimiento que diseñe la matriz de colores

def MatrizDeColores():
    plt.subplot(3,3,1)
    MiMatrizCyan=np.zeros((50,50,3))
    MiMatrizCyan[:, :, 1]= 1  # Capa Magenta
    MiMatrizCyan[:, :, 2]= 1  # Capa Amarilla
    plt.imshow(MiMatrizCyan)
    plt.subplot(3,3,2)
    MiMatrizBlanca=np.ones ((50,50,3))
    plt.imshow(MiMatrizBlanca)
    plt.subplot(3,3,3)
    MiMatrizRoja=np.ones((50,50,3))
    MiMatrizRoja[:,:,1]=0
    MiMatrizRoja[:,:,2]=0
    plt.imshow(MiMatrizRoja)
    plt.subplot(3,3,4)
    MiMatrizMangenta=np.zeros((50,50,3))
    MiMatrizMangenta[:, :, 0]= 1  # Capa Magenta
    MiMatrizMangenta[:, :, 2]= 1  # Capa Amarilla
    plt.imshow(MiMatrizMangenta)
    plt.subplot(3,3,5)
    MiMatrizGris=np.ones ((50,50,3))*0.5
    plt.imshow(MiMatrizGris)
    plt.subplot(3,3,6)
    MiMatrizVerde=np.ones((50,50,3))
    MiMatrizVerde[:, :, 0] = 0  # Capa Roja
    MiMatrizVerde[:, :, 2] = 0  # Capa Azul
    plt.imshow( MiMatrizVerde)
    plt.subplot(3,3,7)
    MiMatrizAmarrilla=np.zeros((50,50,3))
    MiMatrizAmarrilla[:, :, 0]= 1  # Capa Magenta
    MiMatrizAmarrilla[:, :, 1]= 1  # Capa Amarilla
    plt.imshow(MiMatrizAmarrilla)
    plt.subplot(3,3,8)
    MiMatriz=np.zeros ((50,50,3))
    plt.imshow(MiMatriz)
    plt.subplot(3,3,9)
    MiMatrizAzul=np.ones((50,50,3))
    MiMatrizAzul[:, :, 0] = 0  # Capa Roja
    MiMatrizAzul[:, :, 1] = 0  # Capa Azul
    plt.imshow(MiMatrizAzul)
    plt.show()

"""2. Realizar un procedimiento que diseñe la siguiente imagen a través una matriz"""

def MatrizPorEscalar(NewMatriz,Escalar):
        Tam=np.shape(NewMatriz)
        Fila = Tam[0]
        Columna = Tam[1]
        for i in range(Fila): 
            for x in range(Columna):
                NewMatriz[i,x] = NewMatriz[i,x]*Escalar
        return NewMatriz

#3. Elaborar una función que invierta los colores de una imagen

def InvertirColores(MyImagen):
    Imagen = plt.imread(MyImagen)
    ImgInvert = 255-Imagen
    plt.subplot(1,2,1)
    plt.title("Imagen Original")
    plt.imshow(Imagen)
    plt.subplot(1,2,2)
    plt.title("Imagen Invertida")
    plt.imshow(ImgInvert)
    plt.show()

#4. Elaborar una función a la que se le envie de una imagen retorne su capa Roja

def ImagenCapaRoja(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    ImagenCapaRoja = np.copy(MyImagen)
    ImagenCapaRoja[:, :, 1] = 0  # Capa Verde
    ImagenCapaRoja[:, :, 2] = 0  # Capa Azul
    return ImagenCapaRoja

#5. Elaborar una función a la que se le envie de una imagen retorne su capa Verde

def ImagenCapaVerde(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    ImagenCapaVerde = np.copy(MyImagen)
    ImagenCapaVerde[:, :, 0] = 0  # Capa Roja
    ImagenCapaVerde[:, :, 2] = 0  # Capa Azul
    return ImagenCapaVerde

#6. Elaborar una función a la que se le envie de una imagen retorne su capa Azul

def ImagenCapaAzul(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    ImagenCapaAzul = np.copy(MyImagen)
    ImagenCapaAzul[:, :, 0] = 0  # Capa Roja
    ImagenCapaAzul[:, :, 1] = 0  # Capa Verde
    return ImagenCapaAzul

#7. Elaborar una función a la que se le envie de una imagen retorne su capa Magenta

def ImagenCapaMangenta(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255
    plt.subplot(1, 2, 1)
    plt.title("Imagen Original")
    plt.imshow(MyImagen)

    plt.subplot(1, 2, 2)
    plt.title("Capa Magenta")
    ImagenCapaMangenta = np.copy(MyImagen)
    ImagenCapaMangenta[:, :, 0] = 1  # Capa Cian
    ImagenCapaMangenta[:, :, 2] = 1  # Capa Amarilla
    plt.imshow(ImagenCapaMangenta)

    plt.show()

#8. Elaborar una función a la que se le envié de una imagen y retorne la imagen en Cyan

def ImagenCapaCian(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255

    plt.subplot(1, 2, 1)
    plt.title("Imagen Original")
    plt.imshow(MyImagen)

    plt.subplot(1, 2, 2)
    plt.title("Capa Cian")
    ImagenCapaCian = np.copy(MyImagen)
    ImagenCapaCian[:, :, 1] = 1  # Capa Magenta
    ImagenCapaCian[:, :, 2] = 1  # Capa Amarilla
    plt.imshow(ImagenCapaCian)

    plt.show()

#9. Elaborar una función a la que se le envié de una imagen y retorne la imagen en Amarillo

def ImagenCapaAmarrillo(MyImagen):
    MyImagen = plt.imread(MyImagen) / 255

    plt.subplot(1, 2, 1)
    plt.title("Imagen Original")
    plt.imshow(MyImagen)

    plt.subplot(1, 2, 2)
    plt.title("Capa Amarilla")
    ImagenCapaCian = np.copy(MyImagen)
    ImagenCapaCian[:, :, 1] = 1  # Capa Magenta
    ImagenCapaCian[:, :, 0] = 1  # Capa Cian
    plt.imshow(ImagenCapaCian)

    plt.show()

"""10. Elaborar una función en la que le envie por separado las capas RGB y
    con base en ellas reconstruya la imagen en colores"""


def ImagenPorCapas(MyImaganRoja,MyImagenVerde,MyImagenAzul):
    ImagenPorCapas =  (MyImaganRoja+MyImagenVerde+MyImagenAzul)
    plt.imshow(ImagenPorCapas)

    plt.show()

"""11. Elaborar una función a la que se le envié 2 imágenes y que me retorne
    la fusión de las dos imágenes sin ecualizar"""

def FusionImgSinEcualizar(MyImagan1,MyImagan2):
    plt.figure("Punto 11")
    Imagen1 = plt.imread(MyImagan1) / 255
    Imagen2 = plt.imread(MyImagan2) / 255
    plt.subplot(1, 3, 1)
    plt.title("Imagen Uno")
    plt.imshow(Imagen1)
    plt.subplot(1, 3, 2)
    plt.title("Imagen Dos")
    plt.imshow(Imagen2)


    FusionImgSinEcualizar = Imagen1+Imagen2
    plt.subplot(1, 3, 3)
    plt.title("Imagenes Fusionadas")
    plt.imshow(FusionImgSinEcualizar)

    plt.show()

"""12.Elaborar una función a la que se le envié 2 imágenes y que me retorne
    la fusión de las dos imágenes ecualizadas"""

def FusionImgEcualizar(MyImagan1,MyImagan2,Factor1,Factor2):
    plt.figure("Punto 12")
    Imagen1 = plt.imread(MyImagan1) / 255
    Imagen2 = plt.imread(MyImagan2) / 255
    plt.subplot(1, 3, 1)
    plt.title("Imagen Uno")
    plt.imshow(Imagen1)
    plt.subplot(1, 3, 2)
    plt.title("Imagen Dos")
    plt.imshow(Imagen2)
    Factor1 = 3
    Factor2 = 2

    FusionImgEcualizar = Imagen1*Factor1 * Imagen2*Factor2
    plt.subplot(1, 3, 3)
    plt.title("Imagenes Fusionadas")
    plt.imshow(FusionImgEcualizar)

    plt.show()

"""13.Elaborar una función a la que se le envie una imagen y un factor y
    retorne la imagen ecualizada según el factor"""

def FusionImgEcualizarFactor(MyImagen,Factor):
    plt.figure("Punto 13")
    Imagen = plt.imread(MyImagen)/255
    plt.subplot(1,2,1)
    plt.title("Imagen Original")
    plt.imshow(Imagen)
    plt.subplot(1,2,2)
    plt.title("Imagen Ecualizada")
    ImagenEcualizada = Imagen*Factor
    plt.imshow(ImagenEcualizada)

    plt.show()

"""14. Elaborar una función a la que se le envie una imagen y que retorne la
    imagen con la Técnica de promedio (Average)
    15.Elaborar una función a la que se le envié una imagen y que retorne la
    imagen en escala de grises con la técnica de promedio (Average)"""

def ImagenEnGrisAverage(MyImagen):
    plt.figure("Punto 14")
    plt.rcParams['image.cmap'] = 'gray'
    MyImagen = plt.imread(MyImagen)/255
    plt.title("Imagen Gris con average")
    CapaRoja = MyImagen[:, :, 0]
    CapaVerde = MyImagen[:, :, 1]
    CapaAzul = MyImagen[:, :, 2]
    ImagenGrisAverage = (CapaRoja + CapaAzul + CapaVerde) / 3  
    return ImagenGrisAverage

"""16.Elaborar una función a la que se le envié una imagen y que retorne la
imagen en escala de grises con la técnica de Luminosidad (Luminosity)"""

def ImagenEnGrisLuminosity(MyImagen):
    plt.figure("Punto 16")
    plt.rcParams['image.cmap'] = 'gray'
    plt.title("Imagen Gris con Luminosity")
    MyImagen = plt.imread(MyImagen)/255
    CapaRoja = MyImagen[:, :, 0]
    CapaVerde = MyImagen[:, :, 1]
    CapaAzul = MyImagen[:, :, 2]
    ImagenEnGrisLuminosity = CapaRoja * 0.299 + CapaVerde * 0.587+ CapaAzul * 0.114
    return ImagenEnGrisLuminosity
    
'''Punto 1'''
MatrizDeColores()
'''Punto 3'''
InvertirColores("prueba.jpg")
'''Punto 4'''
NewImagen=ImagenCapaRoja("prueba.jpg")
plt.imshow(NewImagen)
plt.show()
'''Punto 5'''
NewImagen=ImagenCapaVerde("prueba.jpg")
plt.imshow(NewImagen)
plt.show()
'''Punto 6'''
NewImagen=ImagenCapaAzul("prueba.jpg")
plt.imshow(NewImagen)
plt.show()
'''Punto 7'''
ImagenCapaMangenta("prueba.jpg")
'''Punto 8'''
ImagenCapaCian("prueba.jpg")
'''Punto 9'''
ImagenCapaAmarrillo("prueba.jpg")
'''Punto 10'''
ImagenPorCapas(ImagenCapaRoja("prueba.jpg"),ImagenCapaVerde("prueba.jpg"),ImagenCapaAzul("prueba.jpg"))
'''Punto 11'''
FusionImgSinEcualizar("prueba.jpg","prueba2.jpg")
"""Punto 12"""
#FusionImgEcualizar("prueba.jpg","prueba2.jpg")
'''Punto 13'''
FusionImgEcualizarFactor("prueba.jpg",0.5)
'''Punto 14 y 15'''
Imagen=ImagenEnGrisAverage("prueba.jpg")
plt.imshow(Imagen)
plt.show()
'''Punto 16'''
Imagen=ImagenEnGrisLuminosity("prueba.jpg")
plt.imshow(Imagen)
plt.show()
