# Notes
# 1. To capture a video, you need to create a VideoCapture object. Its argument can be either the device index
#   or the name of a video file. Device index is just the number to specify which camera.
# 2. c.read() returns 2 things:
#   1st a boolean value telling if VideoCapture object was able to read frame or not
#   2nd the actual frame
# 3. cv2.cvtColor converts frame's color scheme if called
# 4. For video applications do not keep cv2.waitKey argument 0, it ill indefinitely hang on to a single frame
# 5. Each videoCapture object has 19 properties (0 to 18)
#   c.get(property_ID) property id can be any value between 0 to 18
#   c.set(property_ID) property id can be any value between 0 to 18

import cv2

c = cv2.VideoCapture(0)  # 0 is the index of the camera
while c.isOpened():
    ret, frame = c.read ()

    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("f", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord ('Q'):
            break
    else:
        break  # if videoCapture object failed to read the frame in c.read(), break
c.release ()
cv2.destroyAllWindows ()
