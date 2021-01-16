import G001A_pb2_grpc
import G001A_pb2
import grpc

_HOST= '172.16.0.15'
_PORT_SYSTEM = '123456'

def run_system():
  channel = grpc.insecure_channel('172.16.0.15:123456')
  stub = G001A_pb2_grpc.SysStub(channel=channel)
  response = stub.SystemGetter(G001A_pb2.Req(sign = 'sys'))
  print(response)

def run_algorithm():
    channel = grpc.insecure_channel('172.16.0.15:123457')
    stub = G001A_pb2_grpc.AlgorithmStub(channel=channel)
    response = stub.CoordnGetter(G001A_pb2.Req(sign='brk'))
    print(response)
    print('coordn:\n x:%s\n y:%s\n w:%s\n h:%s\n' %(response.x,response.y,response.w,response.h))

if __name__ == '__main__':
    run_algorithm()
    run_system()