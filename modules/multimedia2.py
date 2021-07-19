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


def SplitEnter(result_1, result_2, result_3):
    return result_1.split(), result_2.split(), result_3.split()  # split Enter symbol "\n"


def run(result_1, result_2, result_3):  # 가로 x축   세로 y축    examples
    x1, x2, x3, y1, y2, y3 = initial()

    result1, result2, result3 = SplitEnter(result_1, result_2, result_3)

    for i in range(0, 2):
        print(i)
        cap1 = cv2.VideoCapture(result1[i])
        cap2 = cv2.VideoCapture(result2[i])
        cap3 = cv2.VideoCapture(result3[i])
        print(result1[i], result2[i], result3[i])
        width = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('original size  w : %d, h: %d ' % (width, height))
        print(type(width), type(height))

        while True:
            if cap1.grab():  # 비행기
                flg1, frame1 = cap1.retrieve()
                if flg1:
                    x1, y1 = drone_1(x1, y1)
                    cv2.moveWindow('video1', x1, y1)  # Location of Drone
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
    print("drone1 X Location : %d , Y Location : %d \n" % (x1, y1))
    print("drone2 X Location : %d , Y Location : %d \n" % (x2, y2))
    print("drone3 X Location : %d , Y Location : %d \n" % (x3, y3))


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


def CheckVideoEnding(cap1, cap2, cap3):
    if cap1.get(cv2.CAP_PROP_POS_FRAMES) == cap1.get(cv2.CAP_PROP_FRAME_COUNT):
        pass
    if cap2.get(cv2.CAP_PROP_POS_FRAMES) == cap2.get(cv2.CAP_PROP_FRAME_COUNT):
        pass
    if cap3.get(cv2.CAP_PROP_POS_FRAMES) == cap3.get(cv2.CAP_PROP_FRAME_COUNT):
        pass

# class main:
#     run()
