import cv2

img = cv2.imread("test.jpg", 0)
cv2.namedWindow("Demo")
cv2.resizeWindow("Demo", 300, 300)
cv2.imshow("Demo", img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()


