import cv2
import numpy as np

# call the face classifier to extract features of face
face_classsifier = cv2.CascadeClassifier('C:/Users/ARPITA/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


#function for face extractor and convert the image in grayscale
def face_extractor(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # using multiscale we scale the image with scaling value and neighbouring value
    faces=face_classsifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    #then we cropped the image using for loop
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face
#open camera
cap= cv2.VideoCapture(0)
count=0
#then we started the loop and start reading images using camera
while True:
    ret, frame= cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face= cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
#photos will be saved in jpg format using if condition above
        file_name_path= 'F:/faces/user'+str(count)+'.jpg'

        cv2.imwrite(file_name_path,face)
# this is counting value
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        cv2.imshow('Face Cropper',face)

    else:
        print("Face not Found")
        pass
    if cv2.waitKey(1)==13 or count==100:
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Complete!!!")
