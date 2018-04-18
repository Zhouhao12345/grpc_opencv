FROM zhouhao123/opencv_python:latest
MAINTAINER zhouhao <zhouhao19931002@hotmail.com>

CMD python /usr/src/app/grpc/server/grpc_server.py
