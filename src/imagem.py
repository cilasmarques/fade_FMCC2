import cv2
import numpy
import os.path as caminho

img = cv2.imread("../input/imagem.jpeg")
img2 = cv2.imread("../input/imagem2.jpeg")
saida = "s"

def fadeIn (img1, img2, len):
	for IN in range(0,len):
	    fadein = IN/float(len)
	    dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)
	    cv2.imshow('window', dst)
	    cv2.waitKey(1)
	    cv2.imwrite(caminho.join("../output/", saida+str(IN)+".jpeg") , dst)

fadeIn(img, img2, 100)


