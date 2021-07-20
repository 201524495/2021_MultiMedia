import cv2

from basi import *
import basi

# name1 = 'build_airplane.mp4'
# name2 = 'build_bed.mp4'
# name3 = 'build_bird.mp4'
#
# path_dir = '../video/'

# cap1 = cv2.VideoCapture(path_dir + name1)
# cap2 = cv2.VideoCapture(path_dir + name2)
# cap3 = cv2.VideoCapture(path_dir + name3)


def SplitEnter(res1, res2, res3):
    return res1.split(), res2.split(), res3.split()  # split Enter symbol "\n"


def Length(len1, len2, len3):
    return len(len1), len(len2), len(len3)


def WidthHeight(cap1):
    return cap1.get(cv2.CAP_PROP_FRAME_WIDTH), cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)


def run(res1, res2, res3):  # Videos path (type str)
    x1, x2, x3, y1, y2, y3 = initial()  # initialize videos location
    i_1 = 0;    i_2 = 0;    i_3 = 0
    result1, result2, result3 = SplitEnter(res1, res2, res3)  # split string with new line (type is array)
    len_res1, len_res2, len_res3 = Length(result1, result2, result3)  # length of each array  (type is int)

    cap1 = cv2.VideoCapture(result1[i_1])
    cap2 = cv2.VideoCapture(result2[i_2])
    cap3 = cv2.VideoCapture(result3[i_3])
    width, height = WidthHeight(cap1)

    print(result1[i_1], result2[i_2], result3[i_3])
    print('original size  w : %d, h: %d ' % (width, height))
    print(type(width), type(height))

    while True:
        if cap1.grab():  #
            flg1, frame1 = cap1.retrieve()  # 영상을 한 frame씩 읽어오기
            if flg1:
                x1, y1 = drone_1(x1, y1)
                cv2.moveWindow('video1', x1, y1)  # Location of Drone
                cv2.namedWindow('video1', cv2.WINDOW_NORMAL)  # custom size or full size
                cv2.resizeWindow("video1", int(width / 3), int(height / 3))  # size
                cv2.setWindowProperty('video1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video1', frame1)

        if cap2.grab():  #
            flg2, frame2 = cap2.retrieve()
            if flg2:
                x2, y2 = drone_2(x2, y2)
                cv2.moveWindow('video2', x2, y2)
                cv2.namedWindow('video2', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video2", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video2', frame2)

        if cap3.grab():  #
            flg3, frame3 = cap3.retrieve()
            if flg3:
                x3, y3 = drone_3(x3, y3)
                cv2.moveWindow('video3', x3, y3)
                cv2.namedWindow('video3', cv2.WINDOW_NORMAL)
                cv2.resizeWindow("video3", int(width / 3), int(height / 3))
                cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video3', frame3)

        # InfiniteLoop(cap1, cap2, cap3)  #
        # printLocation(x1, x2, x3, y1, y2, y3)
        stopVideos()  #

        if cv2.waitKey(10) & 0xFF == ord('q'):
            # keystroke latency (10ms)
            # click the UI & press 'q' key
            print("press the q")
            break

        #
        # if cv2.waitKey(1) & ord('p'):
        #     cv2.waitKey(0)

    cv2.destroyAllWindows()


def stopVideos():
    if cv2.waitKey(10) == 32:
        # click the Space bar to Stop Videos
        print("press the Space bar")
        cv2.waitKey(0)


def initial():
    x1 = 1000;    y1 = 700  # drone 1
    x2 = 10;    y2 = 10  # drone 2
    x3 = 800;    y3 = 10  # drone 3
    return x1, x2, x3, y1, y2, y3


def printLocation(x1, x2, x3, y1, y2, y3):
    print("drone1 X Location : %d , Y Location : %d" % (x1, y1))
    print("drone2 X Location : %d , Y Location : %d" % (x2, y2))
    print("drone3 X Location : %d , Y Location : %d" % (x3, y3))


def drone_3(x3, y3):
    x3 -= 7;    y3 += 5
    if y3 > 700:
        x3 = 800;        y3 = 10
    return x3, y3


def drone_2(x2, y2):
    x2 += 5;    y2 += 2
    if x2 > 930:
        x2 = 10;        y2 = 10
    return x2, y2


def drone_1(x1, y1):
    x1 -= 3;    y1 -= 7
    if x1 < 10 or y1 < 10:
        x1 = 1000;        y1 = 700
    return x1, y1


def InfiniteLoop(cap1, cap2, cap3):
    if cap1.get(cv2.CAP_PROP_POS_FRAMES) == cap1.get(cv2.CAP_PROP_FRAME_COUNT):  # 현재 프레임과 총 프레임이 같으면 ( 동영상이 종료 되면)
        cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 현재 프레임을 0번째 프레임으로 설정한다.
    if cap2.get(cv2.CAP_PROP_POS_FRAMES) == cap2.get(cv2.CAP_PROP_FRAME_COUNT):
        cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if cap3.get(cv2.CAP_PROP_POS_FRAMES) == cap3.get(cv2.CAP_PROP_FRAME_COUNT):
        cap3.set(cv2.CAP_PROP_POS_FRAMES, 0)


def CheckVideoEnding_1(cap1, i_1):
    if cap1.get(cv2.CAP_PROP_POS_FRAMES) == cap1.get(cv2.CAP_PROP_FRAME_COUNT):
        return True


def CheckVideoEnding_2(cap2, i_2):
    if cap2.get(cv2.CAP_PROP_POS_FRAMES) == cap2.get(cv2.CAP_PROP_FRAME_COUNT):
        return True


def CheckVideoEnding_3(cap3, i_3):
    if cap3.get(cv2.CAP_PROP_POS_FRAMES) == cap3.get(cv2.CAP_PROP_FRAME_COUNT):
        return True

# class main:
#     run()
