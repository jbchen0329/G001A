# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math
import glob
import os
import time
import grpc
import detect_pb2
import detect_pb2_grpc
# from moviepy.editor import VideoFileClip
# 高斯滤波核大小
_HOST = '10.61.100.105'
_PORT = '9007'

blur_ksize =5

canny_lth = 150
canny_hth = 300

rho = 1
theta = np.pi / 180
threshold = 5
min_line_len = 10
max_line_gap = 80
def process_an_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 1)
    edges = cv2.Canny(blur_gray, 100, 150)
    rows, cols = edges.shape
    points = np.array([[(1455, 497), (1610, 439), (1630, 480), (1490, 561)]])
    roi_edges = roi_mask(edges, points)
    drawing, lines = hough_lines(roi_edges, rho, theta, threshold, min_line_len, max_line_gap)
    result = draw_lanes(drawing, lines)
    return result

def roi_mask(img, corner_points):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, corner_points, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)
    # 新建一副空白画布
    drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # 画出直线检测结果
    draw_lines(drawing, lines)
    return drawing, lines
def draw_lines(img, lines, color=[0, 255, 0], thickness=2):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def draw_lanes(img, lines, color=[255, 0, 0], thickness=3):
    need_lines = []
    need_y2 = []
    need_dis = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            k = (y2 - y1) / (x2 - x1)
            if k < 0:
                need_y2.append(y2)
                need_lines.append(line)
                dis = math.sqrt(math.pow(line[0][0] - line[0][2], 2) + math.pow(line[0][1] - line[0][3], 2))
                need_dis.append(dis)
    if len(need_y2)>0:
        id_max = np.argmax(need_dis)  # 求出下端最大值的线段的索引值()
        line_max = need_lines[id_max][0]
        cv2.line(img, (line_max[0], line_max[1]), (line_max[2], line_max[3]),  (0, 0, 255), 8)
        result_dis = int(need_dis[id_max])
        result_dis =int(1.28*0.77*result_dis)
        # cv2.putText(img, "Distance:"+str(result_dis)+"mm", (1280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        # cv2.imwrite("img.jpg", img)
        return(result_dis, line_max)
if __name__ == '__main__':
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = detect_pb2_grpc.ModelServerStub(channel=conn) 
    cap = cv2.VideoCapture("rtsp://admin:sjzn2018@10.61.100.107//Streaming/Channels/101")
    _, img = cap.read()
    while cap.isOpened():
        try:
            _, img = cap.read()
            if _ == False:
                cap.release()
                cap = cv2.VideoCapture("rtsp://admin:sjzn2018@10.61.100.107//Streaming/Channels/101")
                print('重连摄像头')
            try:
                dis, line_max = process_an_image(img)
                cv2.imwrite('img.jpg',img)
            except:
                print("设备无法检测")
                continue
                
            with open("img.jpg", "rb") as f:
                img_bin = f.read()
            try:
                print('距离：%d'%dis)
                response = client.beltDeviation(detect_pb2.beltDeviationRequest(number=6, deviationlength=dis, img_bin=img_bin))  # 返回的结果就是proto中定义的类
                if response.success == True:
                    print('通信正常')
                else:
                    print('通信异常')
            except:
                print("通信失败")
            
            time.sleep(10)
        except:
            continue
