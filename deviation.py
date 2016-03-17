import cv2
import numpy as np

def deviation(source,target):
    
     source,target = rgb_to_lab(source,target)
     
     l,a,b = cv2.split(source)
     
     lMeanSrc,aMeanSrc,bMeanSrc  = mean(l,a,b)
     lStdSrc,aStdSrc,bStdSrc     = std_deviation(l,a,b)  
     
     l,a,b = cv2.split(target)
     
     lMeanTar,aMeanTar,bMeanTar = mean(l,a,b)      
     lStdTar,aStdTar,bStdTar    = std_deviation(l,a,b)
     
     tranformedImage = transformation(l,a,b,lMeanSrc,aMeanSrc,bMeanSrc,lStdSrc,aStdSrc,bStdSrc,lMeanTar,aMeanTar,bMeanTar,lStdTar,aStdTar,bStdTar)
     
     return tranformedImage

def  rgb_to_lab(source,target):
    
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")
    return (source,target)

def mean(l,a,b):
    
     return (l.mean(),a.mean(),b.mean())
     

def std_deviation(l,a,b):
    
     return (l.std(), a.std(),b.std())


def transformation(l,a,b,lMeanSrc,aMeanSrc,bMeanSrc,lStdSrc,aStdSrc,bStdSrc,lMeanTar,aMeanTar,bMeanTar,lStdTar,aStdTar,bStdTar):
      
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    l = (lStdTar/lStdSrc) * l
    a = (aStdTar/aStdSrc) * a
    b = (bStdTar/bStdSrc) * b

	
    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

	# clip the pixel intensities to [0, 255]
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

	# convert back to the RGB color
    tranformedImage = cv2.merge([l, a, b])
    tranformedImage = cv2.cvtColor(tranformedImage.astype("uint8"), cv2.COLOR_LAB2BGR)
	
    return tranformedImage