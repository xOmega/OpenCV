import cv2
# import numpy as np

c = cv2.VideoCapture(0)  # 0 is the index of the camera
face_cascade = cv2.CascadeClassifier("Haarcascade-Frontalface.xml")

# fourcc = cv2.cv.FOURCC('M', 'J', 'P', 'G')
# out = cv2.VideoWriter("test.mkv", fourcc, 23, (704, 400))

while c.isOpened():
    ret, frame = c.read()

    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame,
                                              scaleFactor=1.2,
                                              minNeighbors=5,
                                              minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        # out.write(frame)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        cv2.imshow("f", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
            break
    else:
        break  # if videoCapture object failed to read the frame in c.read(), break
c.release()
# out.release()
cv2.destroyAllWindows()

