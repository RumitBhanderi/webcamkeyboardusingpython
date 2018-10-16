import numpy as np
import cv2
import pyautogui


cap = cv2.VideoCapture(0)
count=0

while(1):
    
    ## Read the image
    ret, frame = cap.read()
    
    ## Do the processing
    frame = cv2.flip(frame,1)
    
    
    global cx
    global cy
    global old_area,new_area
    old_area,new_area=0,0
    #for yellow color idenitfiaction in frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([14,141,140])#change this hsv values if yellow color as per your lighting condition
    upper_yellow = np.array([84,255,255])#same as above    
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    blur = cv2.medianBlur(mask, 15)
    blur = cv2.GaussianBlur(blur , (5,5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    
    cv2.imshow("mask",mask)
    #find contours in frame
    _,contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
    def keyboard_layout():   
        x=50
        y=50
        
        for i in range(1,10):
            cv2.rectangle(frame,(x,y),(x+50,100),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        cv2.rectangle(frame,(500,50),(500+50,100),(0,255,0),2)
        cv2.putText(frame,'0',(x+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        list_1="q w e r t y u i o p"
        list_1=list_1.split(" ")
        x=50
        for i in list_1:
            y=150
            cv2.rectangle(frame,(x,y),(x+50,100),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        list_2='a s d f g h j k l '
        list_2=list_2.split(" ")
        x=50
        for i in list_2:
            y=200
            cv2.rectangle(frame,(x,y),(x+50,150),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        
        
        list_3='z x c v b n m   '
        list_3=list_3.split(" ")
        x=50
        for i in list_3:
            y=250
            cv2.rectangle(frame,(x,y),(x+50,200),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+140),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
    
        x=100
        y=300
        cv2.rectangle(frame,(x-50,y),(x+350,250),(0,255,0),2)
        
        cv2.rectangle(frame,(x+350,250),(x+450,300),(0,255,0),2)
        cv2.putText(frame,"<--",(x+357,285),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    keyboard_layout()
    cv2.imshow('image',frame)
    if cv2.waitKey(1) == 27:  
        break

cap.release()
cv2.destroyAllWindows()