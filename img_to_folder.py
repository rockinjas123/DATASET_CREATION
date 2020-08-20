#ORIGINAL FOLDER WHERE IMAGE IS KEPT is "folder1"
#new folder is "folder2"

import os
import cv2
import matplotlib.pyplot as plt

path = "./folder1"
pathx = "./folder2"

for ix in os.listdir(path):
  names.append(ix)
names = set(names) #UNIQUE IMAGE NAME
names = list(names)

for ix in names: 
    path_img = os.path.join(path,ix)
    m = ix.find(".jpg") # WHATEVER THE EXTENSION MAY BE eg. image_xyz.jpg
    new_folder = ix[:m] # NEW FOLDER NAME eg image_xyz
    path_new_img = os.path.join(pathx,new_folder) 
    
    os.mkdir(path_new_img) # Creating a new folder with name image_xyz inside folder2
    
    img= cv2.imread(path_img) # reading image, from folder 1
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # BGR --> RGB
    image_path = os.path.join(path_new_img,ix) 
    plt.imsave(image_path,img) # saving image_xyz.jpg in folder image_xyz in folder folder 2
