
import cv2
from numpy import round, uint8 ,zeros
import numpy

#ascii darkness list
ascii='Ñ@#W$9876543210?!abc;:+=-,._'
indexShift=255/len(ascii)

cv2.namedWindow('webcam')
cv2.namedWindow("asciiWindow")

wc=cv2.VideoCapture(0)

pw,ph=64,64
w,h=512,512

font = cv2.FONT_HERSHEY_SIMPLEX
org = (0, 0)
fontScale = 0.22
color = (255, 255, 255)
thickness = 1
if wc.isOpened():
    rval,frame=wc.read()
else:
    rval = False

while rval:
    blackImage=zeros((w,h,3),numpy.uint8)
    asciiImageSymbols=[]
    resized=cv2.resize(frame,(pw,ph),interpolation=cv2.INTER_LINEAR)
    pixelation=cv2.resize(resized,(w,h),interpolation=cv2.INTER_NEAREST)
    grayscalePixalation=cv2.cvtColor(pixelation,cv2.COLOR_BGR2GRAY)
    image=''
    for i in range(int(pw)):
        temp=''
        for x in range(int(ph)):
            samplePixel=grayscalePixalation[(i*int((w/pw)))][(x*int((h/ph)))]
            character=ascii[len(ascii)-int(round(samplePixel/indexShift,0))-1]
            cv2.putText(blackImage,character,(int((x+1)*(w/pw)),int(h/ph*(i+0.5))), font,fontScale,color, thickness, cv2.LINE_AA)
    cv2.imshow("webcam",frame)
    cv2.imshow("asciiWindow",blackImage)
    rval,frame=wc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
wc.release()