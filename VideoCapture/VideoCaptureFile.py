# Instead of providing WebCam index in videoCapture, video file is provided.
# Notes:
# 1. Writing a video requires slightly more work than just imwrite()
#   we need to create a videoWriter object

import cv2
import numpy as np

c = cv2.VideoCapture("F:\Anime\One_Piece1\One Piece 311.mkv")  # 0 is the index of the camera


fourcc = cv2.cv.FOURCC('M', 'J', 'P', 'G')
out = cv2.VideoWriter("test.mkv", fourcc, 23, (704, 400))

while c.isOpened():
    ret, frame = c.read()

    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)
        cv2.imshow("f", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord ('Q'):
            break
    else:
        break  # if videoCapture object failed to read the frame in c.read(), break
c.release()
out.release()
cv2.destroyAllWindows()
