from __future__ import print_function

import grpc

import data_pb2_grpc
import data_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = data_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(data_pb2.HelloRequest(name='2'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()