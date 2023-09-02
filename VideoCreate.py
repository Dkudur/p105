import os
import cv2

print(os.getcwd)

path = "c:/Users/Anike/Downloads/Python/Projects/p105/Images"

Images = []

for file in os.listdir(path):

    root, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        print(file_name)
        Images.append(file_name)

        count = len(Images)

        frame = cv2.imread(Images[0])

        height, width, channels = frame.shape

        size = (width, height)

        print(size)

        out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
    
    for i in range(0, count-1):
        f = cv2.imread(Images[i])
        out.write(f)
        