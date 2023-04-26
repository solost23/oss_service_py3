import os, sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/protopb/gen/py3/')

print(sys.path)

from protopb.gen.py3.protos import oss_pb2_grpc as oss

import grpc
from concurrent import futures

class OssService(oss.OssServicer):
    def Upload(self, request, context):
        print('upload')


def run():
    server = grpc.Server(futures.ThreadPoolExecutor(max_workers=10))
    oss.add_OssServicer_to_server(OssService, server)

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()