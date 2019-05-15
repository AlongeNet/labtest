import argparse
import cv2
import numpy as np 

#handle arguments of cmd
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the file")
args = vars(ap.parse_args())

#Normal window for start
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Output", 600, 600)
cv2.namedWindow("Input", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Input", 600, 600)

#open image with cv2
image = cv2.imread(args["image"])

rows, cols = image.shape[:2]

src_points = np.float32([[0, 0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
dst_points = np.float32([[0, 100], [cols-1, 0], [int(0.33*cols), rows-1], [int(0.66*cols), rows-1]])

projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(image, projective_matrix, (cols, rows))

#Show images and wait press 's' for end program
cv2.imshow('Input', image)
cv2.imshow('Output', img_output)
cv2.waitKey(0)
