import G001A_pb2_grpc
import G001A_pb2
import grpc

_HOST1 = '10.61.100.105'
_PORT1 = '123456'
conn1 = grpc.insecure_channel(_HOST1 + ':' + _PORT1)  # 监听频道
client1 = G001A_pb2_grpc.gRPCStub(channel=conn1)


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = G001A_pb2_grpc.gRPCStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)