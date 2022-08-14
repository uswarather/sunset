import cv2 
import os 
images = []
path ="PRO-105-Reference-Code-Student-Activity-main/Images"
allimages = os.listdir(path)
for i in allimages:
    filename="PRO-105-Reference-Code-Student-Activity-main/Images/"+ i
    images.append(filename)
image = cv2.imread(images[0])
hieght,width,channels=image.shape
size=(width,hieght)
newvideo=cv2.VideoWriter("sunset.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in reversed(images):
    frame=cv2.imread(i)
    newvideo.write(frame)
newvideo.release()
cv2.destroyAllWindows()