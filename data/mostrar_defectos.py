import cv2
import matplotlib.pyplot as plt

#Cargar la imagen con openCV

imgBGR = cv2.imread('C:/Users/Gbravove/PycharmProjects/tfg-gbv/data/gdxray/Castings/C0001/C0001_0001.png')

#Cambiar esacio de color BGR a RGB
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

#Mostrar imagen
plt.xticks([]), plt.yticks([])
plt.imshow(imgBGR)
plt.show()