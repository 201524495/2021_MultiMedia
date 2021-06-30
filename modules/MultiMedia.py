import numpy as np
import cv2

names = ['../video/build_airplane.mp4', '../video/build_bed.mp4', '../video/build_bird.mp4']
window_titles = ['airplane', 'bed', 'bird']

cap = [cv2.VideoCapture(i) for i in names]

frames = [None] * len(names);
gray = [None] * len(names);
ret = [None] * len(names);

while True:

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read();

    for i,f in enumerate(frames):
        if ret[i] is True:
            gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2BGRA) # convert videos color to gray
            cv2.imshow(window_titles[i], gray[i]); # show converted color videos
            cv2.imshow(window_titles[i], frames[i]);

    if cv2.waitKey(1) & 0xFF == ord('q'): # click the UI & press 'q' key
        break

for c in cap:
    if c is not None:
        c.release();

# need permission : python3 -m pip install --user opencv-contrib-python
cv2.destroyAllWindows()