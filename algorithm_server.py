# -*- coding:utf8 -*-
import G001A_pb2_grpc
import G001A_pb2
import grpc
from concurrent import futures

_HOST = '172.16.0.15'
_PORT = '123457'

threshold_brk = 0
threshold_mater = 0

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
    def CoordnGetter(self, request, context):
        print('call CoordnGetter()')
        return G001A_pb2.Coordn(
            # x = request.x,
            # y = request.y,
            # w = request.w,
            # h = request.h
            x = 0.0,
            y = 0.0,
            w = 0.0,
            h = 0.0
        )
    def CoordnSetter(self, request, context):
        print('call CoordnSetter()')
        l = [request.x, request.y, request.w, request.h]
        global rio
        rio = l
        return G001A_pb2.Ack_Res(ack = True)
    def ThresGetter(self, request, context):
        print('call %s ThresGetter()' %request.sign)
        global threshold_brk
        return G001A_pb2.Threshold(
            threshold = threshold_brk if request.sign == 'brk' else threshold_mater,
            sign = request.sign
        )
    def ThresSetter(self, request, context):
        print('call %s ThresSetter()' % request.sign)
        if request.sign == 'brk':
             global threshold_brk
             threshold_brk = request.threshold
        else:
            global threshold_mater
            threshold_mater = request.threshold
        return G001A_pb2.Ack_Res(ack = True)
def serve_algorithm():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    G001A_pb2_grpc.add_AlgorithmServicer_to_server(
        AlgorithmServicer(),server)
    server.add_insecure_port(_HOST + ':' + _PORT)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('启动服务 监听%s端口' % _PORT)
    serve_algorithm()
