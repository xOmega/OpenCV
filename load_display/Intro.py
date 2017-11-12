# Basic Load and display and copy code Using cv2 functions imread, imshow and imwrite

import cv2
import os


parent = os.pardir
img_file = os.path.join(parent, "test.jpg")
# print img_file
img = cv2.imread(img_file, 0)
cv2.namedWindow("Demo")
# cv2.resizeWindow("Demo", 300, 300)
cv2.imshow("Demo", img)
cv2.imwrite("replica.jpg", img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()


