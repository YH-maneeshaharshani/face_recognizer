import cv2  # for camera
import numpy as np # used to define arrays
import sqlite3  # database

faceDetecter= cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #to detect faces using camera
cam=cv2.VideoCapture(0) # 0 is the default camera (open web cam)

def insertorupdate(Id,Name,age,faculty): #function is for squlite database

    conn=sqlite3.connect('database.db')
    cmd = "SELECT * FROM STUDENT WHERE ID="+str(Id)
    cursor = conn.execute(cmd) # run the cmd query
    isRecordExist=0 # assume there is no record in our table

    for row in cursor: # if there is a record in the table then set isRecordExist=1
        isRecordExist =1
    
    if(isRecordExist==1): # if there is a record exist in our table
        conn.execute("UPDATE STUDENT SET Name=? WHERE Id=?", (Name,Id)) # update the record
        conn.execute("UPDATE STUDENT SET age=? WHERE Id=?", (age,Id)) # update the record
        conn.execute("UPDATE STUDENT SET faculty=? WHERE Id=?", (faculty,Id))


    else: # if there is no recrd exist we insert the value
        conn.execute("INSERT INTO STUDENT(Id,Name,age,faculty) VALUES(?,?,?,?)",(Id,Name,age,faculty)) # insert the value in the table

    conn.commit() # close all the  connection created in the sqlite 3
    conn.close() #save all th changes

Id=input("Enter user Id:")
Name = input ("Enter user Name: ")
age= input("Enter user Age: ")
faculty= input("Enter user faculty: ")

insertorupdate(Id,Name,age,faculty)

SampleNum = 0 # assume there is no sample dataset
while(True):
    ret,img = cam.read() #open camera
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert colored image to black & white images
    faces=faceDetecter.detectMultiScale(gray,1.3,5) #scale faces 1.3 scale factor , 5 is for  minimum neighbrs

    for (x,y,w,h) in faces:
        SampleNum=SampleNum +1
        cv2.imwrite("dataset/user."+str(Id)+"."+str(SampleNum)+".jpg",gray[y:y+h,x:x+w]) 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) # draw rectangle around the face
        cv2.waitKey(100) # wait for 100ms to capture next face

    cv2.imshow("Face",img) 
    cv2.waitKey(1)

    if(SampleNum>40): # if we have 20 sample dataset then break the loop
        break
cam.release() # close the camera
cv2.destroyAllWindows() #quite

