import numpy as np
import cv2
import random

name1 = 'build_airplane.mp4'
name2 = 'build_bed.mp4'
name3 = 'build_bird.mp4'

path_dir = '../video/'

cap1 = cv2.VideoCapture(path_dir + name1)
cap2 = cv2.VideoCapture(path_dir + name2)
cap3 = cv2.VideoCapture(path_dir + name3)

width = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('original size  w : %d, h: %d ' % (width, height))
print(type(width), type(height))


def run():  # 가로 x축   세로 y축
    x1 = 1000;    y1 = 700  # drone 1
    x2 = 10;    y2 = 10     # drone 2
    x3 = 800;    y3 = 10    # drone 3
    while True:

        if cap1.grab():  # 비행기
            flg1, frame1 = cap1.retrieve()
            if flg1:
                x1, y1 = drone_1(x1, y1)
                cv2.moveWindow('video1', x1, y1)
                cv2.namedWindow('video1', cv2.WINDOW_NORMAL)  # custom size or full size
                cv2.resizeWindow("video1", int(width / 3), int(height / 3))  # size
                cv2.setWindowProperty('video1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video1', frame1)

        if cap2.grab():  # 침대
            flg2, frame2 = cap2.retrieve()
            if flg2:
                x2, y2 = drone_2(x2, y2)
                cv2.moveWindow('video2', x2, y2)
                cv2.namedWindow('video2', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video2", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video2', frame2)

        if cap3.grab():  # 새
            flg3, frame3 = cap3.retrieve()
            if flg3:
                x3, y3 = drone_3(x3, y3)
                cv2.moveWindow('video3', x3, y3)
                cv2.namedWindow('video3', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video3", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video3', frame3)

        InfiniteLoop()

        if cv2.waitKey(10) == 32:
            # click the Space bar to Stop Videos
            print("press the Space bar")
            cv2.waitKey(0)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            # keystroke latency (10ms)
            # click the UI & press 'q' key
            print("press the q")
            break

        #
        # if cv2.waitKey(1) & ord('p'):
        #     cv2.waitKey(0)

    cv2.destroyAllWindows()


def drone_3(x3, y3):
    x3 -= 7; y3 += 10
    if y3 > 700:
        x3 = 800; y3 = 10
    return x3, y3


def drone_2(x2, y2):
    x2 += 5; y2 += 2
    if x2 > 930:
        x2 = 10; y2 = 10
    return x2, y2


def drone_1(x1, y1):
    x1 -= 3; y1 -= 7
    if x1 < 10 or y1 < 10:
        x1 = 1000; y1 = 700
    return x1, y1


def InfiniteLoop():
    if cap1.get(cv2.CAP_PROP_POS_FRAMES) == cap1.get(cv2.CAP_PROP_FRAME_COUNT):
        cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if cap2.get(cv2.CAP_PROP_POS_FRAMES) == cap2.get(cv2.CAP_PROP_FRAME_COUNT):
        cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if cap3.get(cv2.CAP_PROP_POS_FRAMES) == cap3.get(cv2.CAP_PROP_FRAME_COUNT):
        cap3.set(cv2.CAP_PROP_POS_FRAMES, 0)


# class main:
#     run()
