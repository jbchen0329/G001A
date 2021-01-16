# -*- coding:utf8 -*-
import G001A_pb2_grpc
import G001A_pb2
import grpc
from concurrent import futures
import os
import psutil
import time

_HOST = '172.16.0.15'
_PORT = '123456'

class SysServicer(G001A_pb2_grpc.SysServicer):
    def __init__(self):
        pass
    def SystemGetter(self, request, context):
        gpuLoadFile = "/sys/devices/gpu.0/load"
        with open(gpuLoadFile, 'r') as gpuFile:
          fileData = gpuFile.read()
        gpu = float(fileData)/10.0
        mem = psutil.virtual_memory().percent
        dsk = psutil.disk_usage("/").percent
        cpu = psutil.cpu_percent(0)
        tempt = psutil.sensors_temperatures()['thermal-fan-est'][0].current
        print('call SystemGetter()')
        return  G001A_pb2.System_Info(
            cpu_info = cpu,
            gpu_info = gpu,
            mem_info = mem,
            tmpt_info =  tempt,
            hd = dsk
        )
    def Restart(self, request, context):
        print('call Restart')
        time.sleep(2)
        os.system('reboot')

def serve_system():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  G001A_pb2_grpc.add_SysServicer_to_server(
      SysServicer(), server)
  server.add_insecure_port(_HOST + ':' + _PORT)
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    print('启动服务 监听%s端口' % _PORT)
    serve_system()
