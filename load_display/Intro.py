# Basic Load and display and copy code Using cv2 functions imread, imshow and imwrite
# --------------------------------------------------------------------------------------------------------------
# Notes:
# 1. Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. So color images will
# not be displayed correctly in Matplotlib if image is read with OpenCV. Please see the exercises for more details.
# 2. If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows :
# cv2.waitKey(0) & 0xFF


import cv2
import os


parent = os.pardir
img_file = os.path.join(parent, "test.jpg")
img = cv2.imread(img_file, 0)
cv2.namedWindow("Demo")
cv2.imshow("Demo", img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("replica.jpg", img)
    cv2.destroyAllWindows()
