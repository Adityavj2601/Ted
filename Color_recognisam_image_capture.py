import cv2   
import numpy as np
from math import sqrt


temp_red = (0,0)
temp_yellow = (0,0)
temp_blue = (0,0)
temp_green=(0,0)


#flag_variable
flag_red = False
flag_yellow = False
flag_blue = False
flag_green = False


def distance( c1, c2):
	dist = sqrt((c2[1]-c1[1])**2+(c2[0]-c1[0])**2)
	temp_red=(0,0)
	temp_yellow=(0,0)
	temp_green=(0,0)
	temp_blue=(0,0)
	return dist

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
    _, img = cap.read()
#converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)

            #definig the range of red color
    red_lower=np.array([160,140,133],np.uint8)
    red_upper=np.array([179,255,255],np.uint8)

            #defining the Range of Blue color
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
            
            #defining the Range of yellow color
    yellow_lower=np.array([20,120,200],np.uint8)
    yellow_upper=np.array([52,255,255],np.uint8)

        #defining the Range of yellow color
    green_lower=np.array([45,100,100],np.uint8)
    green_upper=np.array([60,255,255],np.uint8)

        #finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    green=cv2.inRange(hsv,green_lower,green_upper)
            
      #Morphological transformation, Dilation  	
    kernal = np.ones((7 ,7), "uint8")

    eroded = cv2.erode( red, kernal, iterations=1)    
    red=cv2.dilate(red, kernal)
    res=cv2.bitwise_and(img, img, mask = red)
    
    eroded = cv2.erode( blue, kernal, iterations=1)    
    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img, img, mask = blue)

    eroded = cv2.erode( yellow, kernal, iterations=1)    
    yellow=cv2.dilate(yellow,kernal)
    res2=cv2.bitwise_and(img, img, mask = yellow)    

    eroded = cv2.erode( green, kernal, iterations=1)    
    green=cv2.dilate(green,kernal)
    res3=cv2.bitwise_and(img, img, mask = green)

    

            #Tracking the Red Color
    (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300 and area < 1000):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            temp_red = (cX,cY)
            flag_red=True
            if(flag_yellow == False and flag_red==True):
                temp_yellow = (0,0)
                temp_red = (0,0)
                    

        else:
                #temp_yellow = (0,0)
                #temp_red = (0,0)
                flag_red=False
            #    print(temp_red)   
                            
            #Tracking the Blue Color
    (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300  and area < 1000):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            temp_blue=(cX,cY)
            flag_blue=True
            if(flag_green == False and flag_blue==True):
                temp_green = (0,0)
                temp_blue = (0,0)
                    

        else:
                #temp_yellow = (0,0)
                #temp_red = (0,0)
                flag_blue=False
    
    
           #Tracking the yellow Color
    (contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300  and area < 1000):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255))
            temp_yellow = (x,y)
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            
            flag_yellow=True
            temp_yellow = (cX,cY)
            if(flag_yellow == True and flag_red==False ):
                    
                    temp_yellow = (0,0)
                    temp_red = (0,0)

           # print(temp_yellow)
        else:
                flag_yellow=False
                #temp_yellow = (0,0)
                #print(temp_yellow)    
    
        #Tracking the Green Color
    (contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300  and area < 1000):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            temp_green=(cX,cY)    
            flag_green=True
            if(flag_blue == False and flag_green==True):
                temp_blue = (0,0)
                temp_green = (0,0)
                    

        else:
                #temp_yellow = (0,0)
                #temp_red = (0,0)
                flag_green=False

    #print("YR :" + str(distance(temp_yellow,temp_red)))
    #print("GB :" + str(distance(temp_green,temp_blue)))
    YR= distance(temp_yellow, temp_red)
    BG= distance(temp_blue, temp_green)
    if((YR >  5 and YR< 70) and (BG >5 and BG<70)):
            print("clicked")
    #cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking",img)
    #cv2.imshow("red",res) 	
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break  
