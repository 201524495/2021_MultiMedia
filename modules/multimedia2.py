import numpy as np
import cv2

name1 = 'build_airplane.mp4'
name2 = 'build_bed.mp4'
name3 = 'build_bird.mp4'

path_dir = '../video/'

window_title = 'airplane'

cap1 = cv2.VideoCapture(path_dir + name1)
cap2 = cv2.VideoCapture(path_dir + name2)
cap3 = cv2.VideoCapture(path_dir + name3)

width = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('original size  w : %d, h: %d ' % (width, height))
print(type(width), type(height))


def run():
    while True:

        if cap1.grab():
            flg1, frame1 = cap1.retrieve()
            if flg1:
                cv2.moveWindow('video1', 10, 10)
                cv2.namedWindow('video1', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video1", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video1', frame1)

        if cap2.grab():
            flg2, frame2 = cap2.retrieve()
            if flg2:
                cv2.moveWindow('video2', 1000, 10)
                cv2.namedWindow('video2', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video2", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video2', frame2)

        if cap3.grab():
            flg3, frame3 = cap3.retrieve()
            if flg3:
                cv2.moveWindow('video3', 10, 500)
                cv2.namedWindow('video3', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video3", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video3', frame3)

        InfiniteLoop()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # keystroke latency (1ms)
            # click the UI & press 'q' key
            break

    cv2.destroyAllWindows()


def InfiniteLoop():
    if cap1.get(cv2.CAP_PROP_POS_FRAMES) == cap1.get(cv2.CAP_PROP_FRAME_COUNT):
        cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if cap2.get(cv2.CAP_PROP_POS_FRAMES) == cap2.get(cv2.CAP_PROP_FRAME_COUNT):
        cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if cap3.get(cv2.CAP_PROP_POS_FRAMES) == cap3.get(cv2.CAP_PROP_FRAME_COUNT):
        cap3.set(cv2.CAP_PROP_POS_FRAMES, 0)

# class main:
#     run()
