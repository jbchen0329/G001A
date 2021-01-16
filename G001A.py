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

# 父进程创建缓冲栈，并传给各个子进程：
q_pic = Manager().list()
rio = Array('f', [])
threshold_brk = Value('f', )
threshold_mater = Value('f', )
conn = grpc.insecure_channel(_HOST + ':' + _PORT)
client_algorithm = G001A_pb2_grpc.AlgorithmStub(channel=conn)

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
    # while True:
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

    image_detect()


def image_detect():
    deviat_result= Process(target=DeviatPred, args=(q_pic,))
    metar_result=Process(target=MetarPred, args=(q_pic,))
    brk_result = Process(target=BrkPred, args=(q_pic,))
    p_algorithm_serve = Process(target=serve_algorithm, )

    deviat_result.start()
    metar_result.start()
    brk_result.start()
    p_algorithm_serve.start()
    deviat_result.join()
    metar_result.join()
    brk_result.join()
    p_algorithm_serve.join()

def DeviatPred(stack):
    while 1:
        frame = stack.pop()
        process_an_image(frame, rio)
        client_algorithm.DeviatPred(G001A_pb2.Inspt_Req())

def MetarPred(stack):
    while 1:
        frame = stack.pop()
        yolo_param = {
            "model_path": 'logs/posun_1.38.pth',
            "anchors_path": 'model_data/yolo_anchors.txt',
            "classes_path": 'model_data/posun_classes.txt',
            "model_image_size": (608, 608, 3),
            "confidence": threshold_mater,
            "cuda": True,
        }
        detect(frame, yolo_param)

def BrkPred(stack):
    while 1:
        frame = stack.pop()
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
    grpc_client(flag, r_image, YOLO)

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
    response = client_algorithm.BrkPred(
        G001A_pb2.Inspt_Req(number=7, break_bool=True, img_bin=img_bin))

class SystemServicer(G001A_pb2_grpc.SystemServicer):
    def __init__(self):
        pass
    def SystemGetter(self, request, context):
        gpuLoadFile = "/sys/devices/gpu.0/load"
        with open(gpuLoadFile, 'r') as gpuFile:
          fileData = gpuFile.read()
        gpu = fileData/10
        mem = psutil.virtual_memory().percent
        dsk = psutil.disk_usage("/").percent
        cpu = psutil.cpu_percent(0)
        tempt = psutil.sensors_temperatures()['thermal-fan-est'][0].current
        return  G001A_pb2.System_Info(
            cpu_info = cpu,
            gpu_info = gpu,
            mem_info = mem,
            tmpt_info =  tempt,
            hd = dsk
        )
    def Restart(self, request, context):
        os.system('reboot')
def serve_system():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  G001A_pb2_grpc.add_SystemServicer_to_server(
      SystemServicer(), server)
  server.add_insecure_port(_HOST + ':' + _PORT)
  server.start()
  server.wait_for_termination()

# class AlgorithmServicer(G001A_pb2_grpc.AlgorithmServicer):
#     def __init__(self):
#         pass
#     # 客户端
#     # def DeviatPred(self):
#     #     pass
#     # def MetarPred(self):
#     #     pass
#     # def BrkPred(self):
#     #     pass
#
#     # 服务端
#     def CoordnGetter(self, request, context):
#         return G001A_pb2.Coordn(
#             x = request.x,
#             y = request.y,
#             w = request.w,
#             h = request.h
#         )
#     def CoordnSetter(self, request, context):
#         l = [request.x, request.y, request.w, request.h]
#         global rio
#         rio = l
#         return G001A_pb2.Ack_Res(ack = True)
#     def ThresGetter(self, request, context):
#         return G001A_pb2.Threshold(
#             threshold = threshold_brk if request.sign == 'brk' else threshold_mater,
#             sign = request.sign
#         )
#     def ThresSetter(self, request, context):
#         if request.sign == 'brk':
#              global threshold_brk
#              threshold_brk = request.threshold
#         else:
#             global threshold_mater
#             threshold_mater = request.threshold
#         return G001A_pb2.Ack_Res(ack = True)
# def serve_algorithm():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     G001A_pb2_grpc.add_AlgorithmServicer_to_server(
#         AlgorithmServicer(),server)
#     server.add_insecure_port(_HOST + ':' + _PORT)
#     server.start()
#     server.wait_for_termination()

if __name__ == '__main__':

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
    pw.join()
    p_system_serve.join()