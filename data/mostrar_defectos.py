import cv2
import matplotlib.pyplot as plt
import pandas as pd


# cargar groundthruth en dataframe
df = pd.read_fwf('C:/Users/Gbravove/PycharmProjects/tfg-gbv/data/gdxray/Castings/C0001/ground_truth.txt',header=None)
df.columns=["imagen", "x1", "x2", "y1","y2"]
print(df)

# Cargar la imagen con openCV
imagenBGR = cv2.imread('C:/Users/Gbravove/PycharmProjects/tfg-gbv/data/gdxray/Castings/C0001/C0001_0001.png')
# Cambiar esacio de color BGR a RGB
imagenRGB = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2RGB)
# Mostrar imagen
#plt.xticks([]), plt.yticks([])
plt.imshow(imagenRGB)
#plt.show()

#Dibujando un rectangulo
x1=int(df['x1'].values[0])
y1=int(df.iloc[0]['y1'])
x2=int(df.iloc[0]['x2'])
y2=int(df.iloc[0]['y2'])

cv2.rectangle(imagenRGB,(x1,y1),(x2,y2),(255,255,255),3)

cv2.imshow('imagen',imagenRGB)
cv2.waitKey(0)





