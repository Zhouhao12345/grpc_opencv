from __future__ import print_function

import grpc
import data_pb2_grpc
import data_pb2
from PIL import Image
import cStringIO
import base64

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = data_pb2_grpc.GreeterStub(channel)
    buffer = cStringIO.StringIO()
    image = Image.open('./3.jpg')
    image.save(buffer, format='JPEG')
    img_str = base64.b64encode(buffer.getvalue())
    response = stub.CheckImageFace(data_pb2.ImageRequest(imageBuffer=img_str))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()