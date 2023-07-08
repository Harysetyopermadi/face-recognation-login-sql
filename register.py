
from connect import *
from function import *
import cv2
import numpy as np




id_user=input('Enter User Id : ')
nama_user=input('Enter User Name : ')
umur=input('Enter User umur : ')
email=input('Enter User email : ')
password=input('Enter Password : ')
try:
    insertOrUpdate(id_user,nama_user,umur,email,password)
    take_face(id_user)
    getImagesWithID(id_user)
    train_data(id_user)
except Exception as e:
    print("gagal ",e)

