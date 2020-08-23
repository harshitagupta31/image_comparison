from PIL import Image, ImageChops
import cv2

import glob
import numpy as np 
all_imgs_to_compare=[]
for f in glob.iglob("C:\\Users\\HARSHITA GUPTA\\Desktop\\images\\*") :
    image=Image.open(f)
    all_imgs_to_compare.append(image)

    
cap = cv2.VideoCapture(0)
while True:
    ret,test_img=cap.read()
    
    if not ret :
        continue
    
    cv2.imwrite("frame%d.jpg", test_img) 
    
    cap_img=Image.open(r"C:\\Users\\HARSHITA GUPTA\\Desktop\\frame%d.jpg")
    
    for img_to_compare in all_imgs_to_compare :
        diff=ImageChops.difference(cap_img, img_to_compare)
        
    if diff.getbbox()==None:
        diff.show()
        print("VERIFIED")
    else:
        print("NOT VERIFIED")



    if cv2.waitKey(1000):
        break

cap.release()
cv2.destroyAllWindows()