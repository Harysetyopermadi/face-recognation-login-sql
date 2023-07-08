from connect import *
import cv2
import numpy as np
import os
from PIL import Image
import time


def insertOrUpdate(id_user,nama_user,umur,email,password):

    cursor.execute("SELECT * FROM users WHERE id_user="+str(id_user))
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        print("id user sudah ada")
        cnxn.commit()
        cnxn.close()
        exit()
        
    else:
        params = (id_user,nama_user,umur,email,password)
        cursor.execute("INSERT INTO users(id_user,nama_user,umur,email,password) Values(?, ?, ?, ?, ?)",params)
        print("berhasil insert")
       

    cnxn.commit()
    cnxn.close()

def take_face(id_user):
    faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    sampleNum=0
    
    try:
        os.chdir("D:/Python/face_recognation/face-match_with-sql/dataset/"+id_user)
        print("Folder Sudah Ada")
    except:
        print("Folder tidak ada")
        path=os.path.join("D:/Python/face_recognation/face-match_with-sql/dataset/",id_user)
        os.mkdir(path)
        print("Berhasil Create Folder")
    
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("D:/Python/face_recognation/face-match_with-sql/dataset/"+id_user+"/User."+str(id_user)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(100)
        cv2.imshow("Face",img)
        cv2.waitKey(1)
        if(sampleNum>50):
            break
    cam.release()
    cv2.destroyAllWindows()
    
def getImagesWithID(id_user):
    
    path='D:/Python/face_recognation/face-match_with-sql/dataSet/'+id_user+'/'


    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagepath in imagepaths:
        if ".DS_Store" in imagepath:
            print("Junk!")
        else:
            faceImg=Image.open(imagepath).convert('L')
            faceNp=np.array(faceImg,'uint8')
            ID=int(os.path.split(imagepath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training",faceNp)
            cv2.waitKey(10)
    return np.array(IDs),faces
    
def train_data(id_user):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #pathz='D:/Python/face_recognation/face-match_with-sql/'+id_user
    try:
        os.chdir("D:/Python/face_recognation/face-match_with-sql/recognizer/"+id_user)
        print("folder train Sudah Ada")
    except:
        print("folder train tidak ada")
        pathz=os.path.join("D:/Python/face_recognation/face-match_with-sql/recognizer/",id_user)
        os.mkdir(pathz)
        print("Berhasil Create folder train")
    
    IDs,faces=getImagesWithID(id_user+'/')
    recognizer.train(faces,IDs)
    recognizer.save('D:/Python/face_recognation/face-match_with-sql/recognizer/'+id_user+'/trainningData.yml')
    cv2.destroyAllWindows()

def auth_login(id_user,password):
    try:
        cursor.execute("SELECT * FROM users WHERE id_user="+str(id_user))
        isRecordExist=0
        for row in cursor:
            isRecordExist=1
            id_user=row[0]
            nama=row[1]
            password_user=row[4]
        if(isRecordExist==1):
            if (password_user==password):
                print("Data Ada ",nama)
                auth_face(id_user,nama)
            else:
                print("Password Salah")
                
            
            cnxn.commit()
            cnxn.close()
            exit()
        
        else:
            print("Data Tidak Ada")
       

        cnxn.commit()
        cnxn.close()
    except Exception as e:
        print("gagal login ",e)
        
def auth_face(id_user,nama):
    faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    #rec=cv2.createLBPHFaceRecognizer();
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read('D:/Python/face_recognation/face-match_with-sql/recognizer/'+id_user+'/trainningData.yml')
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX,0.4,1,0,1)

    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (0, 0, 0)
    f_fc=0
    fc=f_fc
    id_fc_auth=str(id_user)
    name_fc_auth=nama
    while(True):
        
        
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        int(fc)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            # str(id)
            #print(id)
            # print(id)
            # profile=getProfile(id)
            # if(profile!=None):
            #     #print("match")
            #     cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),fontface, fontscale, fontcolor)
            #     cv2.putText(img,"Age : "+str(profile[2]),(x,y+h+45),fontface, fontscale, fontcolor)
            #     cv2.putText(img,"Gender : "+str(profile[3]),(x,y+h+70),fontface, fontscale, fontcolor); 
            #     cv2.putText(img,"Criminal Records : "+str(profile[4]),(x,y+h+95),fontface, fontscale, fontcolor)
          
            if (fc==100):
                print("Wajah Match")
                print(name_fc_auth)
                time.sleep(10)
                exit()
            if (str(id)==str(id_fc_auth)):
                int(fc)
                fc=fc+1
                str(fc)
                print("mirip")
            if (str(id)!=str(id_fc_auth)):
                fc=0
                print("tidak mirip")
            # else:
            #     print("h") 
                #fc=0    
                #cv2.putText(img,"Name : Unknown",(x,y+h+20),fontface, fontscale, fontcolor);
                #cv2.putText(img,"Age : Unknown",(x,y+h+45),fontface, fontscale, fontcolor);
                #cv2.putText(img,"Gender : Unknown",(x,y+h+70),fontface, fontscale, fontcolor);
                #cv2.putText(img,"Criminal Records : Unknown",(x,y+h+95),fontface, fontscale, fontcolor);
        cv2.imshow("Face",img)
    
    
        if(cv2.waitKey(1)==ord('q')):
            break
    
  
    cam.release()
    cv2.destroyAllWindows()
    