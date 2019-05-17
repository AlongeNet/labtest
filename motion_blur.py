import cv2
import argparse
import numpy as np 

'''
#handle cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
'''
path = 'tree.jpg'
#Normal window 
cv2.namedWindow("Motion Blur", cv2.WINDOW_NORMAL)
#cv2.resizeWindow('0', 600, 600)

#open image 
image = cv2.imread(path)

size = 15

kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size 

img_output = cv2.filter2D(image, -1, kernel_motion_blur)

#Write to file 
cv2.imwrite(path, img_output)
#show an image
cv2.imshow('Motion Blur', img_output)
cv2.waitKey(0)