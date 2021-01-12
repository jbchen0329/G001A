import os
import gc
from multiprocessing import Process, Manager
from PIL import Image
import numpy as np
import cv2
import time
import grpc
from libs.yolo import YOLO
import G001A_pb2_grpc
import G001A_pb2
from concurrent import futures
from BeltDeviation import process_an_image


# 向共享缓冲栈中写入数据:
def write(stack, cam, top: int) -> None:
    """
    :param cam: 摄像头参数
    :param stack: Manager.list对象
    :param top: 缓冲栈容量
    :return: None
    """
    print('Process to write: %s' % os.getpid())
    cap = cv2.VideoCapture(cam)
    _HOST1 = '10.61.100.105'
    _PORT1 = '9006'
    conn1 = grpc.insecure_channel(_HOST1 + ':' + _PORT1)  # 监听频道
    client1 = G001A_pb2_grpc.gRPCStub(channel=conn1)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    while True:
        str = "speed"
        response1 = client1.SpeedSwitch(G001A_pb2.GetSpeedSwitchRequest(name=str))  # 返回的结果就是proto中定义的类
        speed_value = response1.message[6:]
        print(float(speed_value))
        #print(type(float(speed_value)))
        try:
            _, img = cap.read()
            if _ and float(speed_value) > 0:
                stack.append(img)
                # 每到一定容量清空一次缓冲栈
                # 利用gc库，手动清理内存垃圾，防止内存溢出
                if len(stack) >= top:
                    del stack[:]
                    gc.collect()
            if not _:
                print("摄像头连接失败")
                cap.release()
                cap = cv2.VideoCapture("rtsp://admin:sjzn2018@10.61.100.106//Streaming/Channels/101")
                continue
        except:
            continue


# 在缓冲栈中读取数据:
def read(stack) -> None:
    while True:
        # try:
        #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     # 转变成Image
        #     frame = Image.fromarray(np.uint8(frame))
        #     save_frame = Image.fromarray(np.uint8(frame))
        #     # 进行检测
        #     r_image, flag = yolo.detect_image(frame, )
        #     if flag == 'break':
        #         t3 = time.time()
        #         print("有破损")
        #         save_frame.save('./image/img.jpg')
        #         with open('./image/img.jpg', 'rb') as f:
        #             img_bin = f.read()
        #         try:
        #             response = client.beltBreak(
        #                 detect_pb2.beltBreakRequest(number=7, break_bool=True, img_bin=img_bin))
        #         except Exception:
        #             print('通信失败')
        #             continue
        #         if response.success == True:
        #             print('通信正常')
        #         else:
        #             print('通信异常')
        # except:
        #     continue
        frame = stack.pop()
        image_detect(frame)

def image_detect(frame):
    DeviatPred= Process(target=DeviatPred1, args=(frame, q_rio))
    MetarPred=Process(target=MetarPred1, args=(frame, q_threshold_mater))
    BrkPred = Process(target=BrkPred1, args=(frame, q_threshold_brk))




def DeviatPred1(frame):
    set rio
    process_an_image(frame)

def MetarPred1(frame):
    set q_threshold_mater
    yolo_param = {
        "model_path": 'logs/posun_1.38.pth',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/posun_classes.txt',
        "model_image_size": (608, 608, 3),
        "confidence": 0.9,
        "cuda": True,
    }
    detect(frame, yolo_param)

def BrkPred1(frame):
    set q_threshold_brk
    yolo_param = {
        "model_path": 'logs/posun_1.38.pth',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/posun_classes.txt',
        "model_image_size": (608, 608, 3),
        "confidence": 0.9,
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
    grpc_client(flag, r_image, YOLO)

def grpc_client(flag, r_image, YOLO):
    if flag != 'break' or "Yes" or "No":
        return
    r_image.save('./image/img.jpg')
    with open('./image/img.jpg', 'rb') as f:
        img_bin = f.read()
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client_algorithm = G001A_pb2_grpc.AlgorithmStub(channel=conn)
    if YOLO.get_defaults("sign") == 'Brk':
        pass
    else:
        pass
    response = client_algorithm.BrkPred(
        G001A_pb2.Inspt_Req(number=7, break_bool=True, img_bin=img_bin))

class SystemServicer(G001A_pb2_grpc.SystemServicer):
    def __init__(self):
        pass
    def SystemGetter(self):
        pass
    def Restart(self):
        pass
def serve_system():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  G001A_pb2_grpc.add_SystemServicer_to_server(
      SystemServicer(), server)
  server.add_insecure_port(_HOST + ':' + _PORT)
  server.start()
  server.wait_for_termination()

class AlgorithmServicer(G001A_pb2_grpc.AlgorithmServicer):
    def __init__(self):
        pass
    # 客户端
    # def DeviatPred(self):
    #     pass
    # def MetarPred(self):
    #     pass
    # def BrkPred(self):
    #     pass

    # 服务端
    def CoordnGetter(self):
        rio = q_rio.pop()
        q_rio.append(rio)
        return q_rio
    def CoordnSetter(self, rio):
        q_rio.pop()
        q_rio.append(rio)
        return
    def ThresGetter(self, sign):
        if sign == 'brk':
            thers = q_threshold_brk.pop()
        else:
            thers = q_threshold_mater.pop()
        return thers
    def ThresSetter(self, sign):
        if sign == 'brk':
            q_threshold_brk.append()
        else:
            q_threshold_mater.append()
        return
def serve_algorithm():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    G001A_pb2_grpc.add_AlgorithmServicer_to_server(
        AlgorithmServicer(),server)
    server.add_insecure_port(_HOST + ':' + _PORT)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    _HOST = ''
    _PORT = ''
    # 父进程创建缓冲栈，并传给各个子进程：
    q_pic = Manager().list()
    q_rio = Manager().list()
    q_threshold_brk = Manager().Queue()
    q_threshold_mater = Manager().Queue()
    pw = Process(target=write, args=(q_pic, "rtsp://admin:sjzn2018@10.61.100.106//Streaming/Channels/101", 100))
    pr = Process(target=read, args=(q_pic,))
    p_system_serve =Process(target=serve_system,)
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    p_system_serve.start()

    # conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    # client_system = G001A_pb2_grpc.SystemStub(channel=conn)
    # channel = grpc.insecure_channel('localhost:50051')
    # stub = helloworld_pb2_grpc.GreeterStub(channel)
    # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    # 等待pr结束:
    pr.join()
    # pw进程里是死循环，无法等待其结束，只能强行终止:
    pw.terminate()