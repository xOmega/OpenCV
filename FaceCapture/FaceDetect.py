import cv2
# import numpy as np


def faceDetect(sourceIndex):
    """
    This is the first block in the facial recognition pipeline.
    :param sourceIndex: Index of input video source. 0 is the index of the webcam
    :return:
    """
    s = sourceIndex
    c = cv2.VideoCapture(s)
    face_cascade = cv2.CascadeClassifier("Haarcascade-Frontalface.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    # fourcc = cv2.cv.FOURCC('M', 'J', 'P', 'G')
    # out = cv2.VideoWriter("test.mkv", fourcc, 23, (704, 400))

    while c.isOpened():
        ret, frame = c.read()

        if ret:
            maxNumberOfFaces = 5
            grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grey_frame,
                                                  scaleFactor=1.2,
                                                  minNeighbors=maxNumberOfFaces,
                                                  minSize=(30, 30),
                                                  flags=cv2.CASCADE_SCALE_IMAGE)

            # out.write(frame)
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    face_grey = grey_frame[y: y+h, x: x+w]
                    face_color = frame[y: y+h, x: x+w]
                    eyes = eye_cascade.detectMultiScale(face_grey)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(face_color, (ex, ey), (ew, eh), (0, 0, 255), 2)

            cv2.imshow("frame1", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
                break
        else:
            break  # if videoCapture object failed to read the frame in c.read(), break
    c.release()
    # out.release()
    cv2.destroyAllWindows()


def main():
    faceDetect(0)


if __name__ == '__main__':
    main()
