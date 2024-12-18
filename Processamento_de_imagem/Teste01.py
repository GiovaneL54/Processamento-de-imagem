import cv2
import numpy as np
import matplotlib.pyplot as plt
from docutils.nodes import image


def main():
    cv2.imread('C:/Users/Giovane/Downloads/Pandas/pinheiros-lindos-nas-montanhas-1.png',c2.IMREAD_GRAYSCALE)

    if imagem is None:
        print('Erro ao carregar a imagem.')
        return
    bordas = cv2.Canny(imagem, 100,200)

    plt.figure(figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.title('Imagem Original')
    plt.imshow(image,cmap = 'gray')

    plt.subplot(1,2,2)
    plt.title('Bordas Detectadas')
    plt.imshow(bordas,cmap='gray')

    plt.show()

    if __name__ == '__main__':
        main()