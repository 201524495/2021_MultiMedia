# -*- coding: utf-8 -*-
import cv2
from basi import *


def SplitEnter(res):
    return res.split()  # split Enter symbol "\n"


def Length(length):
    return len(length)


def WidthHeight(cap):
    return cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


# calibration 했을 때 나온 결과가 숫자로 들어가야 한다.
# 그것에 비례해 동영상의 크기를 조절해야 한다.
def Inside(xLocation, yLocation):  # , xOrigin, yOrigin, xMax, yMax):  # (zero, zero) ~ (xMax, yMax)
    if (xLocation > -425 and yLocation > -240) and (xLocation < 1919 and yLocation < 1040):
        return True


def StopRestart(value):
    if value == 0:  # Run
        return True
    if value == 1:  # Stop
        return False


def run(res1, res2, res3):  # Videos path (type str)
    x1, y1, x2, y2, x3, y3 = initial()  # 지워질 내용
    i_1 = i_2 = i_3 = 0
    result1 = SplitEnter(res1)  # split string with new line : Videos path (str to array)
    result2 = SplitEnter(res2)
    result3 = SplitEnter(res3)
    len_res1 = Length(result1)  # length of each array : Number of Videos  (type is int)
    len_res2 = Length(result2)
    len_res3 = Length(result3)
    cap1 = cv2.VideoCapture(result1[i_1])  #
    cap2 = cv2.VideoCapture(result2[i_2])
    cap3 = cv2.VideoCapture(result3[i_3])
    width, height = WidthHeight(cap1)
    print(width, height)  # 1280 720

    while True:
        x1, y1 = drone_1(x1, y1)  # 지워질 내용
        x2, y2 = drone_2(x2, y2)  # 지워질 내용
        x3, y3 = drone_3(x3, y3)  # 지워질 내용


        # if StopRestart(val_1):
        if CheckVideoEnding(cap1):  # 동영상이 종료되면
            i_1 += 1  # 번호를 1단계 올리고
            i_1 %= len_res1  # 비디오 수 만큼 재생한다.
            cap1 = cv2.VideoCapture(result1[i_1])  # 새로운 path로 적용한다.
        if Inside(x1, y1):  # drone_1의 위치
            if cap1.grab():  #
                flg1, frame1 = cap1.retrieve()  # 영상을 한 frame씩 읽어오기
                if flg1:
                    cv2.moveWindow("video_1", x1, y1)  # Location of Drone
                    cv2.namedWindow("video_1", cv2.WINDOW_NORMAL)  # custom size or full size
                    cv2.resizeWindow("video_1", int(width / 3), int(height / 3))  # size
                    cv2.setWindowProperty("video_1", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow("video_1", frame1)


        # if StopRestart(val_2):
        if CheckVideoEnding(cap2):  # 동영상이 종료되면
            i_2 += 1  # 번호를 1단계 올리고
            i_2 %= len_res2  # 비디오 수 만큼 재생한다.
            cap2 = cv2.VideoCapture(result2[i_2])  # 적용한다.
        if Inside(x2, y2):  # drone_2의 위치
            if cap2.grab():  #
                flg2, frame2 = cap2.retrieve()  # 영상을 한 frame씩 읽어오기
                if flg2:
                    cv2.moveWindow('video2', x2, y2)  # Location of Drone
                    cv2.namedWindow('video2', cv2.WINDOW_NORMAL)  # custom size or full size
                    cv2.resizeWindow("video2", int(width / 3), int(height / 3))  # size
                    cv2.setWindowProperty('video2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('video2', frame2)


        # if StopRestart(val_3):
        if CheckVideoEnding(cap3):  # 동영상이 종료되면
            i_3 += 1  # 번호를 1단계 올리고
            i_3 %= len_res3  # 비디오 수 만큼 재생한다.
            cap3 = cv2.VideoCapture(result3[i_3])  # 새로운 path로 적용한다.
        if Inside(x3, y3):  # drone_3의 위치
            if cap3.grab():  #
                flg3, frame3 = cap3.retrieve()  # 영상을 한 frame씩 읽어오기
                if flg3:
                    cv2.moveWindow('video3', x3, y3)  # Location of Drone
                    cv2.namedWindow('video3', cv2.WINDOW_NORMAL)  # custom size or full size
                    cv2.resizeWindow("video3", int(width / 3), int(height / 3))  # size
                    cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('video3', frame3)

        stopVideos()  #

        if cv2.waitKey(10) & 0xFF == 27:  # q 보다는 ESC가 더 직관적이고 깔끔하게 잘라짐
            # keystroke latency (10ms)
            # click the UI & press 'ESC' key
            print("press the ESC")
            break

        #
        # if cv2.waitKey(1) & ord('p'):
        #     cv2.waitKey(0)
    cap1.release()
    cap2.release()
    cap3.release()
    cv2.destroyAllWindows()


def stopVideos():
    if cv2.waitKey(10) == 32:
        # click the Space bar to Stop Videos
        print("press the Space bar")
        cv2.waitKey(0)


def initial():
    x1 = 1990;    y1 = 700  # drone 1
    x2 = 10;    y2 = 10  # drone 2
    x3 = 800;    y3 = 10  # drone 3
    return x1, y1, x2, y2, x3, y3


def printLocation(x1, x2, x3, y1, y2, y3):
    print("drone1 X Location : %d , Y Location : %d" % (x1, y1))
    print("drone2 X Location : %d , Y Location : %d" % (x2, y2))
    print("drone3 X Location : %d , Y Location : %d" % (x3, y3))


# 1280:720 = 425:240
# Video Size 1280 720
# my Monitor Size (0,0) ~ (1919,1039)
def drone_3(x3, y3):
    y3 += 2
    if y3 > 1039:
        x3 = 800;        y3 = 10
    return x3, y3


def drone_2(x2, y2):
    x2 += 2;    y2 += 2
    if x2 > 2500 :
        x2 = 10;        y2 = 10
    if y2 > 1039-240:
        y2 = 1039-240
    return x2, y2


def drone_1(x1, y1):
    x1 -= 2;    y1 -= 2
    if x1 < -425 :
        x1 = 1990;        y1 = 1039-240
    if y1 < 10:
        y1 = 10
    return x1, y1


def InfiniteLoop(cap):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # 현재 프레임과 총 프레임이 같으면 ( 동영상이 종료 되면)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 현재 프레임을 0번째 프레임으로 설정한다.


def CheckVideoEnding(cap):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # 동영상이 종료되면
        return True  # True return


# class main:
#     run()
