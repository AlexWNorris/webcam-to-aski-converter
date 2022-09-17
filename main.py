from time import sleep
import cv2
from numpy import round, uint8 ,zeros
import numpy

#ascii darkness list
ascii='Ñ@#W$9876543210?!abc;:+=-,._ '
indexShift=255/len(ascii)

#ranges from 0-->1
pixelationConstant=0.02
pw,ph=64,64
w,h=1920,1080
pws=int(w*pixelationConstant)
phs=int(h*pixelationConstant)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (0, 0)
fontScale = 0.4
color = (255, 255, 255)
thickness = 1

wc=cv2.VideoCapture(0)
codec = 0x47504A4D  # MJPG
wc.set(cv2.CAP_PROP_FPS, 60.0)
wc.set(cv2.CAP_PROP_FOURCC, codec)
wc.set(cv2.CAP_PROP_FRAME_WIDTH, w)
wc.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

if wc.isOpened():
    rval,frame=wc.read()
    frame=cv2.flip(frame,1)
else:
    rval = False
#0.5625
scaler=1/1.5
sw,sh=int(w*scaler),int(h*scaler)
while rval:
    blackImage=zeros((w,h,3),numpy.uint8)
    asciiImageSymbols=[]
    resized=cv2.resize(frame,(pw,ph),interpolation=cv2.INTER_LINEAR)
    pixelation=cv2.resize(resized,(sw,sh),interpolation=cv2.INTER_NEAREST)
    grayscalePixalation=cv2.cvtColor(pixelation,cv2.COLOR_BGR2GRAY)
    image=''
    for i in range(int(ph)):
        temp=''
        for x in range(int(pw)):
            samplePixel=grayscalePixalation[(i*int(len(grayscalePixalation)/pw))][int(x*(len(grayscalePixalation[0])/ph))]
            character=ascii[len(ascii)-int(round(samplePixel/indexShift,0))-1]
            cv2.putText(blackImage,character,(int(x*(w/pw)/(1/scaler)),int((i-1)*(h/ph)/(1/scaler))), font,fontScale,color, thickness, cv2.LINE_AA)
    cv2.imshow("Window",blackImage)
    rval,frame=wc.read()
    frame=cv2.flip(frame,1)
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyAllWindows()
