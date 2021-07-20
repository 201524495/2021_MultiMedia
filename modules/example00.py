import cv2

from basi import *


def SplitEnter(res):
    return res.split()  # split Enter symbol "\n"


def Length(length):
    return len(length)


def WidthHeight(cap):
    return cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


def run(res1, i_1):  # Videos path (type str)
    x1, y1, x2, y2, x3, y3 = initial()  # 지워질 내용
    result1 = SplitEnter(res1)  # split string with new line : Videos path (str to array)
    len_res1 = Length(result1)  # length of each array : Number of Videos  (type is int)
    cap1 = cv2.VideoCapture(result1[i_1])  #
    width, height = WidthHeight(cap1)

    while True:
        if CheckVideoEnding_1(cap1):  # 동영상이 종료되면
            i_1 += 1  # 번호를 1단계 올리고
            i_1 %= len_res1  # 비디오 수 만큼 재생한다.
            run(res1, i_1)  # 적용한다.
        if cap1.grab():  #
            flg1, frame1 = cap1.retrieve()  # 영상을 한 frame씩 읽어오기
            if flg1:
                x1, y1 = drone_1(x1, y1)  # 지워질 내용
                cv2.moveWindow('video1', x1, y1)  # Location of Drone
                cv2.namedWindow('video1', cv2.WINDOW_NORMAL)  # custom size or full size
                cv2.resizeWindow("video1", int(width / 3), int(height / 3))  # size
                cv2.setWindowProperty('video1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video1', frame1)

        # InfiniteLoop(cap1)  #
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
    x1 -= 1;    y1 -= 1
    if x1 < 10 or y1 < 10:
        x1 = 1000;        y1 = 700
    return x1, y1


def InfiniteLoop(cap):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # 현재 프레임과 총 프레임이 같으면 ( 동영상이 종료 되면)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 현재 프레임을 0번째 프레임으로 설정한다.


def CheckVideoEnding_1(cap):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # 동영상이 종료되면
        return True  # True return


# class main:
#     run()
