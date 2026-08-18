import cv2
import numpy as np
import os
import sqlite3

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # to detect the face from the camera
cam=cv2.VideoCapture(0) #open camera

recognizer = cv2.face.LBPHFaceRecognizer_create() # to recognize endd that capture from the camera
recognizer.read("recognizer/trainningData.yml") # read the training data from yml file

def getprofile(id):
    conn=sqlite3.connect("database.db")
    cursor=conn.execute("SELECT * FROM Student WHERE Id=?",(id,))
    profile=None # there will vbe no profile created in our sqlite database

    for row in cursor:
        profile=row
    conn.close()
    return profile

while(True):
    ret,img = cam.read() # opening the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert the colored image to black & white image
    faces = facedetect.detectMultiScale(gray,1.3,5) # detect the face from the camera
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # create green color rectangle around the face
        id,conf = recognizer.predict(gray[y:y+h,x:x+w]) # using trained yml file and predicting what will be the values display in the output
        profile = getprofile(id)
        print(profile)
        if(profile != None):
            cv2.putText(img,"Name: "+str(profile[1]),(x,y+h+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,127),2) # display the name of the user [ 1 for font scale ,,, 2 thickness]
            cv2.putText(img,"Age: "+str(profile[2]),(x,y+h+60),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,127),2) # display the roll number of the user
            cv2.putText(img,"Faculty: "+str(profile[3]),(x,y+h+90),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) # display the course of the user
           # cv2.putText(img,"Year: "+str(profile[4]),(x,y+h+120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2) # display the year of the user
    cv2.imshow("Face",img) # display the image in the window

    if(cv2.waitKey(1)== ord('q')):     # if user hit 'q' button on the desktop it will be exit the output 
        break
cam.release()
cv2.destroyAllWindows()