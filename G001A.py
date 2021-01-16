import os
import gc
from multiprocessing import Process, Manager
from PIL import Image
import numpy as np
import cv2
import psutil
import grpc
from libs.yolo import YOLO
import G001A_pb2_grpc
import G001A_pb2
from concurrent import futures
from BeltDeviation import process_an_image
from multiprocessing import Array, Value
from algorithm_server import serve_algorithm

_HOST = '172.16.0.9'
_PORT = '123456'

# 向共享缓冲栈中写入数据:
def write(stack, q_pic, top: int) -> None:
    stack.append(q_pic)
    # 每到一定容量清空一次缓冲栈
    # 利用gc库，手动清理内存垃圾，防止内存溢出
    if len(stack) >= top:
        del stack[:50]
        gc.collect()


def DeviatPred(q_pic):
    while 1:
        frame = q_pic.pop()
        process_an_image(frame, rio)
        stub.DeviatPred(G001A_pb2.Inspt_Req(number=7, break_bool=True, img_bin=img_bin))

def MetarPred(q_pic):
    while 1:
        frame = q_pic.pop()
        yolo_param = {
            "model_path": 'logs/posun_1.38.pth',
            "anchors_path": 'model_data/yolo_anchors.txt',
            "classes_path": 'model_data/posun_classes.txt',
            "model_image_size": (608, 608, 3),
            "confidence": threshold_mater,
            "cuda": True,
        }
        detect(frame, yolo_param)

def BrkPred(q_pic):
    while 1:
        frame = q_pic.pop()
        yolo_param = {
            "model_path": 'logs/posun_1.38.pth',
            "anchors_path": 'model_data/yolo_anchors.txt',
            "classes_path": 'model_data/posun_classes.txt',
            "model_image_size": (608, 608, 3),
            "confidence": threshold_brk,
            "cuda": True,
        }
        detect(frame, yolo_param)

def detect(frame, yolo_param):
    yolo = YOLO()
    YOLO.set_defaults(yolo_param)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))
    save_frame = Image.fromarray(np.uint8(frame))
    # 进行检测
    r_image, flag = yolo.detect_image(frame, )
    stub.BrkPred(G001A_pb2.Inspt_Req(number=7, break_bool=True, img_bin=img_bin))

def grpc_client(flag, r_image, YOLO):
    if flag != 'break' or "Yes" or "No":
        return
    r_image.save('./image/img.jpg')
    with open('./image/img.jpg', 'rb') as f:
        img_bin = f.read()
    if YOLO.get_defaults("sign") == 'Brk':
        pass
    else:
        pass
    stub.BrkPred(G001A_pb2.Inspt_Req(number=7, break_bool=True, img_bin=img_bin))

if __name__ == '__main__':
    q_pic = Manager().list()
    # q_pic = []
    rio = Array('f', [])
    threshold_brk = Value('f', )
    threshold_mater = Value('f', )

    channel = grpc.insecure_channel(_HOST +":"+_PORT)
    stub = G001A_pb2_grpc.AlgorithmStub(channel)

    pic = cv2.imread('image/0001.jpeg')
    pw = Process(target=write, args=(q_pic, pic, 100))
    deviat_result= Process(target=DeviatPred, args=(q_pic,))
    metar_result=Process(target=MetarPred, args=(q_pic,))
    brk_result = Process(target=BrkPred, args=(q_pic,))
    # p_algorithm_serve = Process(target=serve_algorithm, )
    pw.start()
    # 启动子进程pr，读取:
    deviat_result.start()
    metar_result.start()
    brk_result.start()
    # p_algorithm_serve.start()
    deviat_result.join()
    metar_result.join()
    brk_result.join()
    pw.join()
    # p_algorithm_serve.join()
    