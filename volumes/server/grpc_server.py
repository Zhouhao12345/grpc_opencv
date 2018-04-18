from concurrent import futures
import time

import grpc
import base64
from io import BytesIO
from PIL import Image
import numpy

import data_pb2
import data_pb2_grpc
from face_detect import detect_face

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(data_pb2_grpc.GreeterServicer):

    def CheckImageFace(self, request, context):
        img_str = base64.b64decode(request.name)
        buffer = BytesIO(img_str)
        image = Image.open(buffer)
        checked = detect_face(numpy.array(image))
        return data_pb2.CheckReply(checkResult=str(checked))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()