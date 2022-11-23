import cv2

img = cv2.imread("solar-system.jpg")

#SUN
cv2.putText(img,"sun",(70,100),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,255,255),)


#MERCURY
cv2.putText(img,"mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.4,(225,225,255),)


#VENUS
cv2.putText(img,"Venus",(195,270),cv2.FONT_HERSHEY_COMPLEX,0.4,(225,255,255),)



#Earth
cv2.putText(img,"Earth",(295,270),cv2.FONT_HERSHEY_COMPLEX,0.4,(225,225,255),)


#Mars
cv2.putText(img,"mars",(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,255,255),)


#Jupiter
cv2.putText(img,"Jupiter",(580,370),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,255,255),)


#saturn
cv2.putText(img,"saturn",(800,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,255,255),)


#Uranus
cv2.putText(img,"Uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,255,255),)


#neptune
cv2.putText(img,"Neptune",(1110,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,255,255),)



img = cv2.imshow("Display Image",img)




cv2.waitKey(0)